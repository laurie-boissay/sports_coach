#!/usr/bin/python3.8
# coding:u8


from speech_rec import listen_text
from commands import *
from exercises import *


def menu_loop():
    quit = False
    welcome_text = "Bonjour, je suis votre coach sportif.\n"
    #welcome_text = "Hello I'm your sports coach.\n"

    repeat_text = "Je n'ai pas compris."
    #repeat_text = "I did not understand."

    error_text = "j'ai rencontré une erreur."
    #error_text = "I encountered an error."

    bye_text = "A bientôt !"
    #bye_text = "See you soon !"
    
    menu_key_words = [
        "commencer", # "start",
        "durée", # "duration",
        "exercice", # "exercises",
        "quitter", # "quit",
    ]

    options_text = menu_text(menu_key_words)

    say_text(welcome_text)

    while not quit:
        say_text(options_text)
        text = listen_text()

        # Do sport :
        if menu_key_words[0] in text :
            do_exercises()

        # Manage duration preferences :
        elif menu_key_words[1] in text:
            checking_user_preferences(error_text, repeat_text)

        # Manage exercises names :
        elif menu_key_words[2] in text :
            checking_exercises(error_text, repeat_text)

        # Leave the program :
        elif menu_key_words[3] in text:
            quit = True
            say_text(bye_text)

        # Error :
        elif "error" in text:
            say_text(error_text)
        
        else:
            say_text(repeat_text)
                

if __name__ == '__main__':
    menu_loop()




# cd /home/jaenne/Python/coach
# ./talking_coach.py