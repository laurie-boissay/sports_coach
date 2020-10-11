# RESSOURCES
# https://pypi.org/project/pyttsx3/
# https://sonsuzdesign.blog/2020/06/07/building-a-speech-translator-in-python/


# pip install pyttsx3
# pip install --upgrade wheel
# pip install comtypes
# pip install -Iv pyttsx3==2.6 -U

import pyttsx3


from default_parameters import user_language


def say_text(text):
    """
    This function tell the text.

    """
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)

    if user_language[0] == "fr":
        fr_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0"
        engine.setProperty('voice', fr_voice_id)
    else: #user_language[0] == "en"
        en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        engine.setProperty('voice', en_voice_id)

    engine.say(text)
    engine.runAndWait()
    engine.stop()
