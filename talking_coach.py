#!/usr/bin/python3.8
# coding:u8

import time
import math


from text_to_speech import say_text
from speech_rec import listen_text
from commands import *
from exercices import *
from preferences import user_preferences as p


def main_loop():
    error_text = "Je n'ai pas compris."
    start_text = "Pour commencer dîtes : démarrer."
    
    quitter = False
    
    while not quitter:
        text = listen_text(start_text)

        if "error" in text :
                say_text(error_text)

        else :
            if "démarrer" in text :
                #while text != "C'est partit !":
                    #text = cmd_go()
                    #say_text(text)

                session_start = time.time()
                session_end = session_start + p["session_duration_min"]*60

                start_exercice("échauffement", p["warm_up_duration"], p["warning_frequency"])

                while time.time() + p["exercices_duration"] <= session_end :
                    
                    for ex in exercices_name:
                        if time.time() + p["exercices_duration"] + p["mini_stretching_duration"] <= session_end :
                            start_exercice(ex, p["exercices_duration"], p["warning_frequency"])
                            if time.time() + p["break_duration"] + p["mini_stretching_duration"] <= session_end and p["break_duration"] > 0 :
                                start_exercice("pause", p["break_duration"], p["warning_frequency"])
                        else:
                            break
                    
                    stretching_duration = session_end - time.time()
                    start_exercice("étirements", stretching_duration, p["warning_frequency"])
                    
                quitter = True

    p["session_duration_min"] = round((time.time()-session_start)/60)
    bravo_text = "Bravo vous avez fait "
    bravo_text += str(p["session_duration_min"])
    bravo_text += " minutes de sport."
    say_text(bravo_text)
    

if __name__ == '__main__':
    main_loop()





# cd /home/jaenne/Python/coach
# ./talking_coach.py