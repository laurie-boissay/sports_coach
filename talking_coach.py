#!/usr/bin/python3.8
# coding:u8

import time
import math


from text_to_speech import say_text
from speech_rec import listen_text
from commands import *
from exercices import *


def main_loop():
    session_duration_min = 20
    session_duration_sec = session_duration_min*60
    exercices_duration = 30 #secondes
    break_duration = 30 #secondes
    error_text = "Je n'ai pas compris."
    
    quitter = False
    
    while not quitter:
        text = listen_text()

        if "error" in text :
                say_text(error_text)

        else :
            if "démarrer" in text :
                session_start = cmd_go()
                session_end = session_start + session_duration_sec
                
                start_exercice("échauffement", 60)

                while time.time() + exercices_duration <= session_end :
                    
                    for ex in exercices_name:
                        if time.time() + exercices_duration*3 <= session_end :
                            start_exercice(ex, exercices_duration)
                            if time.time() + exercices_duration*2 <= session_end :
                                start_exercice("pause", break_duration)
                        else:
                            break
                    
                stretching_duration = session_end - time.time()
                start_exercice("étirements", stretching_duration)
                    
                quitter = True

    session_duration_sec = round((time.time()-session_start)/60)
    bravo_text = "Bravo vous avez fait "
    bravo_text += str(session_duration_sec)
    bravo_text += " minutes de sport."
    say_text(bravo_text)
    

if __name__ == '__main__':
    main_loop()





# cd /home/jaenne/Python/coach
# ./talking_coach.py