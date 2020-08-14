from math import *


from text_to_speech import say_text
from speech_rec import listen_text
from default_preferences import *


def menu_text(key_words_list):
    text = "Dîtes : \n"
    #text = "Say : \n"
    or_text = "ou "
    #or_text = "or "
    for word in range(len(key_words_list)):
        if word == len(key_words_list) - 1:
            text += or_text + key_words_list[word] + "\n" 
        else:
            text +=  key_words_list[word] + ", \n"
    return text
    

def checking_user_preferences(error_text, repeat_text):
    quit = False

    check_text = "Dîtes : modifier, okay, ou quitter"
    #check_text = "Say : modify, O K or quit"

    for k, v in user_preferences.items():
        for key, value in preferences_fr_names.items():
        #for key, value in preferences_names.items():
            
            if quit:
                say_text("Sortie du menu.")
                #say_text("Exit the menu.")
                break
            
            elif k == key:
                pref_text = value[0] + " : " + str(v) + " " + value[1]
                say_text(pref_text)
                preferences_checked = False
                
                while not preferences_checked:
                    say_text(check_text)
                    text = listen_text()
                    
                    if "okay" in text :
                    #if "O K" in text :
                        preferences_checked = True

                    elif "modifier" in text :
                    #elif "modify" in text :
                        value = ask_new_value(error_text, repeat_text, v, "integer")
                        user_preferences[k] = int(value)
                        preferences_checked = True

                    elif "quitter" in text :
                    #elif "quit" in text :
                        preferences_checked = True
                        quit = True

                    # Error :
                    elif "error" in text:
                        say_text(error_text)
                    
                    else:
                        say_text(repeat_text)
   
        if quit:
            break

    check_text = checking_duration()
    say_text(check_text)


def ask_new_value(error_text, repeat_text, old_value, value_type):
    value_set = False
    ask_text = "Quelle est la nouvelle valeur ?"
    #ask_text = "What's the new duration ?"
    not_changed_text = "la valeur ne sera as modifiée."
    #not_changed_text = "the value will not be changed."
    ok_text = "La valeur a bien été modifiée."
    #ok_text = "The duration has been changed."

    while not value_set:
        say_text(ask_text)
        text = listen_text()
        
        if "error" in text:
            say_text(error_text)
        
        elif "IDNU" in text:
            say_text(repeat_text)
        
        elif "annuler" in text:
        #elif "cancel" in text:
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
    prb_text = "La durée doit être un nombre entier."
    #text = "The duration must be an integer."
    ok_text = "La durée a bien été modifiée."
    #ok_text = "The duration has been changed."
    
    try:
        int(value)
    except ValueError:
        return False, prb_text

    return True, ok_text


def checking_duration():
    text = "Vos paramètres sont correctes."
    #text = "Your settings are correct."
    prb_text = "La durée de votre session de sport est de : "
    #prb_text = "The duration of your sports session is : "
    
    mini_duration = user_preferences["exercises_duration"]
    mini_duration += user_preferences["break_duration"]
    mini_duration += user_preferences["warm_up_duration"]
    mini_duration += user_preferences["mini_stretching_duration"]
    mini_duration = mini_duration/60

    if user_preferences["session_duration_min"] < mini_duration:
        text = prb_text
        text += str(round(mini_duration)) + " minutes."
        user_preferences["session_duration_min"] = mini_duration

    return text