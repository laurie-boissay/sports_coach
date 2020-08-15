import sys
from math import *


from text_to_speech import say_text
from speech_rec import listen_text
from default_parameters import user_language, supported_languages
from file_management import read_an_object, save_an_object


def user_language_preference(argv):
    if len(sys.argv) != 1:
        language = sys.argv[1].strip("-")
        if language.lower() in supported_languages:
            user_language.append(language.lower())
    else:
        user_language.append("en")


def menu_text(key_words_list):
    if user_language[0] == "fr":
        text = "Dîtes : \n"
        or_text = "ou "

    else: #user_language[0] == "en":
        text = "Say : \n"
        or_text = "or "

    for word in range(len(key_words_list)):
        if word == len(key_words_list) - 1:
            text += or_text + key_words_list[word] + "\n" 
        else:
            text +=  key_words_list[word] + ", \n"
    return text


def checking_user_parameters(error_text, repeat_text):
    quit = False
    user_parameters = read_an_object("durations")

    if user_language[0] == "fr":
        exit_text = "Sortie du menu."
        
        menu_key_words = [
            "d'accord",
            "modifier",
            "quitter",
        ]

        parameters_names = {
            "session_duration_min" : ["Durée de la session de sport", "minutes."],
            "exercises_duration" : ["Durée de chaque exercice", "secondes"],
            "break_duration" : ["Durée des pauses", "secondes"],
            "warm_up_duration" : ["Durée de l'échauffement", "secondes"],
            "mini_stretching_duration" : ["Durée minimum des étirements", "secondes"],
            "countdown_frequency" : ["Fréquence du compte à rebours", "secondes"],
        }

    else: #user_language[0] == "en":
        exit_text = "Exit the menu."
        
        menu_key_words = [
            "O K",
            "modify",
            "quit",
        ]

        parameters_names = {
            "session_duration_min" : ["Duration of the sports session", "minutes"],
            "exercises_duration" : ["Duration of each exercise", "seconds"],
            "break_duration" : ["Duration of breaks", "seconds"],
            "warm_up_duration" : ["Warm-up time", "seconds"],
            "mini_stretching_duration" : ["Minimum stretching time", "seconds"],
            "countdown_frequency" : ["Countdown frequency", "seconds"],
        }
    
    check_text = menu_text(menu_key_words)

    for k, v in user_parameters.items():
        for key, value in parameters_names.items():
            if quit:
                say_text(exit_text)
                break
            
            elif k == key:
                pref_text = value[0] + " : " + str(round(v)) + " " + value[1]
                say_text(pref_text)
                parameters_checked = False
                
                while not parameters_checked:
                    say_text(check_text)
                    text = listen_text()
                    
                    # Don't change value :
                    if menu_key_words[0] in text :
                        parameters_checked = True

                    # Modify value :
                    elif menu_key_words[1] in text :
                        value = ask_new_value(error_text, repeat_text, v, "integer")
                        user_parameters[k] = int(value)
                        parameters_checked = True

                    # Leave menu :
                    elif menu_key_words[2] in text :
                        parameters_checked = True
                        quit = True

                    elif "error" in text:
                        say_text(error_text)
                    
                    else:
                        say_text(repeat_text)
   
        if quit:
            break

    check_text = checking_duration(user_parameters)
    say_text(check_text)


def ask_new_value(error_text, repeat_text, old_value, value_type):
    value_set = False

    if user_language[0] == "fr":
        ask_text = "Quelle est la nouvelle valeur ?"
        not_changed_text = "la valeur ne sera as modifiée."
        ok_text = "La valeur a bien été modifiée."
        cancel_text = "annuler"

    else: #user_language[0] == "en":
        ask_text = "What's the new value ?"
        not_changed_text = "the value will not be changed."
        ok_text = "The value has been changed."
        cancel_text = "cancel"

    while not value_set:
        say_text(ask_text)
        text = listen_text()
        
        if "error" in text:
            say_text(error_text)
        
        elif "IDNU" in text:
            say_text(repeat_text)
        
        elif cancel_text in text:
            value_set = True
            text = old_value
            say_text(not_changed_text)
        
        else:
            if value_type == "integer":
                value_set, result_text = checking_value(text)
                say_text(result_text)
            else :
                value_set = True
                say_text(ok_text)
    
    return text


def checking_value(value):
    if user_language[0] == "fr":
        prb_text = "La durée doit être un nombre entier."
        ok_text = "La durée a bien été modifiée."

    else: #user_language[0] == "en":
        prb_text = "The duration must be an integer."
        ok_text = "The duration has been changed."
    
    try:
        int(value)
    except ValueError:
        return False, prb_text

    return True, ok_text


def checking_duration(user_parameters):
    if user_language[0] == "fr":
        text = "Vos paramètres sont correctes."
        prb_text = "La durée de votre session de sport est de : "
        end_prb_text = " minutes."

    else: #user_language[0] == "en":
        text = "Your settings are correct."
        prb_text = "The duration of your sports session is : "
        end_prb_text = " minutes."
    
    mini_duration = user_parameters["exercises_duration"]
    mini_duration += user_parameters["break_duration"]
    mini_duration += user_parameters["warm_up_duration"]
    mini_duration += user_parameters["mini_stretching_duration"]
    mini_duration = mini_duration/60

    if user_parameters["session_duration_min"] < mini_duration:
        text = prb_text
        text += str(round(mini_duration)) + end_prb_text
        user_parameters["session_duration_min"] = mini_duration

    save_an_object(user_parameters, "durations")
    return text