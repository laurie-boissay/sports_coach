# LINUX : #!/usr/bin/python3.8
# coding:u8

"""
This program is a tool to help you to do sport.

It's fully voice controlled. 

You can set your own exercises name, set your duration preferences 
and save them.

"""

##### RESSOURCES ############################################
#https://stackoverflow.com/questions/4041238/why-use-def-main
#https://www.pythonforbeginners.com/system/python-sys-argv

import os # WINDOWS
import argparse


from text_to_speech import say_text
from speech_rec import listen_text
from commands import checking_user_parameters, user_language_preference, menu_text
from default_parameters import user_language
from file_management import create_default_pref
from exercises import do_exercises, checking_exercises


def menu_loop():
    """
    Ask the user what he/she wants to do :

    START the exercises,
    Modify DURATIONS,
    Modify EXERCISES,
    QUIT the program.

    """
    
    ########################################
    ##### If launched with a command : #####
    ########################################
    #parser = argparse.ArgumentParser()
    #parser.add_argument("language", help="Supported languages : 'fr', 'en'.")
    #args = parser.parse_args()
    #user_language_preference(args.language)

    ########################################
    ###### If launched with a clic : #######
    ########################################
    user_language_preference("fr")

    
    create_default_pref()

    quit = False

    if user_language[0] == "fr":
        welcome_text = "Bonjour, je suis votre coach sportif.\n"
        repeat_text = "Je n'ai pas compris."
        error_text = "J'ai rencontré une erreur."
        bye_text = "A bientôt !"
        
        menu_key_words = [
        "commencer",
        "durée",
        "exercice",
        "quitter",
        ]

    else: # user_language[0] == "en":
        welcome_text = "Hello I'm your sports coach.\n"
        repeat_text = "I did not understand."
        error_text = "I encountered an error."
        bye_text = "See you soon !"
        
        menu_key_words = [
            "start",
            "durations",
            "exercises",
            "exit",
        ]

    options_text = menu_text(menu_key_words)

    say_text(welcome_text)

    while not quit:
        say_text(options_text)
        text = listen_text()

        # Do sport :
        if menu_key_words[0] in text :
            do_exercises()

        # Manage duration parameters :
        elif menu_key_words[1] in text:
            checking_user_parameters(error_text, repeat_text)

        # Manage exercises names :
        elif menu_key_words[2] in text :
            checking_exercises(error_text, repeat_text)

        # Leave the program :
        elif menu_key_words[3] in text:
            quit = True
            say_text(bye_text)

        elif "error" in text:
            say_text(error_text)
        
        else:
            say_text(repeat_text)
                

if __name__ == '__main__':
    menu_loop()
    os.system("pause") #WINDOWS


# LINUX :
# cd /home/jaenne/Python/coach
# ./talking_coach.py fr

# WINDOWS :
# cd C:\Users\Jaenne\Documents\python3x\coach
# talking_coach.py fr


