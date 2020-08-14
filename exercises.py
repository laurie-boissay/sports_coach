import time
import math


from text_to_speech import say_text
from speech_rec import listen_text
from default_preferences import user_preferences as p, user_language
from commands import ask_new_value, menu_text


def start_exercise(exercise_name, exercises_duration):
    exercise_start = time.time()
    exercise_end = exercise_start + exercises_duration

    if user_language[0] == "fr":
        stop_text = "Stop."
        sec_text = " secondes."

    else: #user_language[0] == "en":
        stop_text = "Stop."
        sec_text = " secondes."
    
    ex_text = exercise_name + " " + str(round(exercises_duration)) + sec_text
    say_text(ex_text)
    
    while time.time() <= exercise_end:
        nbr_sec = round(exercise_end - time.time())

        if p["countdown_frequency"] != 0 and nbr_sec % p["countdown_frequency"] == 0 and nbr_sec > 0:
            say_text(str(nbr_sec))

    say_text(stop_text)


def end_exercises(session_start):
    p["session_duration_min"] = round((time.time()-session_start)/60)

    if user_language[0] == "fr":
        bravo_text = "Bravo vous avez fait "
        bravo_text += str(p["session_duration_min"])
        bravo_text += " minutes de sport."

    else: #user_language[0] == "en":
        bravo_text = "Well done you did "
        bravo_text += str(p["session_duration_min"])
        bravo_text += " minutes of sport."

    say_text(bravo_text)


def do_exercises():
    if user_language[0] == "fr":
        from default_preferences import exercises_name_fr as exercises_name
        warm_up_text = "échauffement"
        stretching_text = "étirements"
        break_text = "pause"

    else: #user_language[0] == "en":
        from default_preferences import exercises_name
        warm_up_text = "warm up"
        stretching_text = "stretching"
        break_text = "break"

    session_start = time.time()
    session_end = session_start + p["session_duration_min"]*60

    start_exercise(warm_up_text, p["warm_up_duration"])

    while time.time() + p["exercises_duration"] <= session_end :
        
        for ex in exercises_name:
            if time.time() + p["exercises_duration"] + p["mini_stretching_duration"] <= session_end :
                start_exercise(ex, p["exercises_duration"])
                if time.time() + p["break_duration"] + p["mini_stretching_duration"] <= session_end and p["break_duration"] > 0 :
                    start_exercise(break_text, p["break_duration"])
            else:
                break
        
        stretching_duration = session_end - time.time()
        start_exercise(stretching_text, stretching_duration)

    end_exercises(session_start)


def checking_exercises(error_text, repeat_text):
    quit = False

    if user_language[0] == "fr":
        removed_text = "La valeur a été supprimée."
        list_text = "Voici la liste de vos exercices : "
        exit_text = "Sortie du menu."
        
        menu_key_words = [
            "conserver",
            "modifier",
            "supprimer",
            "quitter",
        ]

    else: #user_language[0] == "en":
        removed_text = "The value has been deleted."
        list_text = "Here is the list of your exercises :"
        exit_text = "Exit the menu."
        
        menu_key_words = [
            "keep",
            "modify",
            "remove",
            "quit",
        ]

    check_text = menu_text(menu_key_words)
    
    if user_language[0] == "fr":
        from default_preferences import exercises_name_fr as exercises_name
    else: #user_language[0] == "en":
        from default_preferences import exercises_name

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

    clean_up_exercises_name()
    add_an_exercise(error_text, repeat_text)
    clean_up_exercises_name()


def clean_up_exercises_name():
    if user_language[0] == "fr":
        from default_preferences import exercises_name_fr as exercises_name
        no_exercises_text = "Il n'y a pas d'exercice dans votre liste."
        
    else: #user_language[0] == "en":
        from default_preferences import exercises_name
        no_exercises_text = "There is no exercise on your list."
    
    for ex in exercises_name:
        if ex == "":
            exercises_name.remove(ex)

    if len(exercises_name) == 0:
        say_text(no_exercises_text)

    
def add_an_exercise(error_text, repeat_text):
    quit = False

    if user_language[0] == "fr":
        from default_preferences import exercises_name_fr as exercises_name
        ask_text = "Voulez-vous ajouter un exercice ?"

        menu_key_words = [
            "ajouter",
            "quitter",
        ]

    else: #user_language[0] == "en":
        from default_preferences import exercises_name
        ask_text = "Do you want to add an exercise?"
    
        menu_key_words = [
            "add",
            "quit",
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