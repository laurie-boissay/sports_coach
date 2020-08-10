# RESSOURCES
# https://pypi.org/project/pyttsx3/
# https://sonsuzdesign.blog/2020/06/07/building-a-speech-translator-in-python/


import pyttsx3


def say_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 100)
    fr_voice_id = "french"
    engine.setProperty('voice', fr_voice_id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()