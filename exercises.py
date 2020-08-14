import time
import math


from text_to_speech import say_text
from speech_rec import listen_text
from default_preferences import user_preferences as p, exercises_name
from commands import ask_new_value, menu_text


def start_exercise(exercise_name, exercises_duration):

	exercise_start = time.time()
	exercise_end = exercise_start + exercises_duration

	ex_text = exercise_name + " " + str(round(exercises_duration)) + " secondes."
	say_text(ex_text)
	
	while time.time() <= exercise_end:
		
		nbr_sec = round(exercise_end - time.time())

		if p["countdown_frequency"] != 0 and nbr_sec % p["countdown_frequency"] == 0 and nbr_sec > 0:
			say_text(str(nbr_sec))

	say_text("Stop.")


def end_exercises(session_start):
    p["session_duration_min"] = round((time.time()-session_start)/60)
    
    bravo_text = "Bravo vous avez fait "
    #bravo_text = "Well done you did "
    bravo_text += str(p["session_duration_min"])
    bravo_text += " minutes de sport."
    #bravo_text += " minutes of sport."

    say_text(bravo_text)


def do_exercises():
    warm_up_text = "échauffement"
    #warm_up_text = "warm up"

    stretching_text = "étirements"
    #stretching_text = "stretching"

    session_start = time.time()
    session_end = session_start + p["session_duration_min"]*60

    start_exercise(warm_up_text, p["warm_up_duration"])

    while time.time() + p["exercises_duration"] <= session_end :
        
        for ex in exercises_name:
            if time.time() + p["exercises_duration"] + p["mini_stretching_duration"] <= session_end :
                start_exercise(ex, p["exercises_duration"])
                if time.time() + p["break_duration"] + p["mini_stretching_duration"] <= session_end and p["break_duration"] > 0 :
                    start_exercise("pause", p["break_duration"])
            else:
                break
        
        stretching_duration = session_end - time.time()
        start_exercise(stretching_text, stretching_duration)

    end_exercises(session_start)


def checking_exercises(error_text, repeat_text):
    quit = False
    
    removed_text = "La valeur a été supprimée."
    #removed_text = "The value has been deleted."
    
    no_exercises_text = "Il n'y a pas d'exercice dans votre liste."
    #no_exercises_text = "There is no exercise on your list."
    
    list_text = "Voici la liste de vos exercices : "
    #list_text = "Here is the list of your exercises :"
    
    exit_text = "Sortie du menu."
    #exit_text = "Exit the menu."
    
    menu_key_words = [
        "d'accord", # "O K",
        "modifier", # "modify",
        "supprimer", # "remove",
        "quitter", # "quit",
    ]
    check_text = menu_text(menu_key_words)

    if len(exercises_name) > 0:
        say_text(list_text)
        for ex in range(len(exercises_name)):
            if quit:
                say_text(exit_text)
                break
            
            else:
                say_text(exercises_name[ex])
                preferences_checked = False
                
                while not preferences_checked:
                    say_text(check_text)
                    text = listen_text()
                    
                    #Don't change value :
                    if menu_key_words[0] in text :
                        preferences_checked = True

                    #Modify value :
                    elif menu_key_words[1] in text :
                        value = ask_new_value(error_text, repeat_text, exercises_name[ex], "string")
                        exercises_name[ex] = value
                        preferences_checked = True

                    #Remove Value :
                    elif menu_key_words[2] in text :
                        exercises_name[ex] = ""
                        preferences_checked = True
                        say_text(removed_text)

                    #Leave menu :
                    elif menu_key_words[3] in text :
                        preferences_checked = True
                        quit = True

                    elif "error" in text:
                        say_text(error_text)

                    else:
                        say_text(repeat_text)

    if len(exercises_name) == 0:
        say_text(no_exercises_text)

    add_an_exercise(error_text, repeat_text)

    for ex in exercises_name:
        if ex == "":
            exercises_name.remove(ex)

    
def add_an_exercise(error_text, repeat_text):
    quit = False
    
    ask_text = "Voulez-vous ajouter un exercice ?"
    #ask_text = "Do you want to add an exercise?"
    
    menu_key_words = [
        "ajouter", # "add",
        "quitter", # "quit",
    ]
    add_text = menu_text(menu_key_words)

    say_text(ask_text)

    while not quit:
        
        say_text(add_text)
        text = listen_text()

        # Add an exercise :
        if menu_key_words[0] in text :
            text = ask_new_value(error_text, repeat_text, "", "string")
            exercises_name.append(text)
        
        # Leave the menu :
        elif menu_key_words[1] in text :
            quit = True

        elif "error" in text:
            say_text(error_text)
        
        else:
            say_text(repeat_text)