# RESSOURCES ______________________________________________________________________________
# https://pypi.org/project/SpeechRecognition/
# https://pythonprogramminglanguage.com/speech-recognition/
# https://stackoverflow.com/questions/62040401/alsa-error-running-a-flask-application-on-linux-ubuntu-using-pyaudio
# https://askubuntu.com/questions/608480/alsa-problems-with-python2-7-unable-to-open-slave
# https://stackoverflow.com/questions/31603555/unknown-pcm-cards-pcm-rear-pyaudio#31729510
# https://bbs.archlinux.org/viewtopic.php?id=245040

import speech_recognition as sr


from text_to_speech import say_text
from default_parameters import user_language


def listen_text():
    if user_language[0] == "fr":
        invitation_text = "J'écoute."
    
    else: # user_language[0] == "en": 
        invitation_text = "I listen."

    # get audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # listen for 1 second to calibrate the energy threshold for ambient noise levels.
        r.adjust_for_ambient_noise(source)
        say_text(invitation_text)
        audio = r.listen(source)

    try:
        if user_language[0] == "fr":
            text = r.recognize_google(audio, language="fr-FR")
        
        else: # user_language[0] == "en":
            text = r.recognize_google(audio)

    except sr.UnknownValueError:
       text = "IDNU"
    except sr.RequestError as e:
       text = "error "

    return text