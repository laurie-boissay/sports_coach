###### RESSOURCES #################################################
#https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/232431-utilisez-des-fichiers
#https://www.guru99.com/python-check-if-file-exists.html


import pickle
from os import path, mkdir, chdir#, listdir, getcwd


from default_parameters import *


def read_an_object(target_file):
    """
    This function open the target_file and return
    the oject inside.

    """
    with open(target_file, "rb") as backup_file:
        pick = pickle.Unpickler(backup_file)
        return pick.load()
        

def save_an_object(object, destination_file):
    """
    This function save the object in the destination_file.

    """    
    with open(destination_file, "wb") as backup_file:
        pick = pickle.Pickler(backup_file)
        pick.dump(object)


def create_default_pref():
    """
    If it doesn't exist, this function creates
    a folder "preferences" with two files inside.

    else, the folder exist but one file or more is missing,
    this function creates the missing file(s) :
        - durations : default parameters durations,
        - exercises : default exercises name.

    """
    if not path.exists("preferences"):
        mkdir("preferences")
        chdir("preferences")
        save_an_object(user_parameters, "durations")
        create_default_exercises()

    else:
        chdir("preferences")
        if not path.exists("durations"):
            save_an_object(user_parameters, "durations")

        if not path.exists("exercises"):
            create_default_exercises()


def create_default_exercises():
    """
    This function generate a file who contains a list
    of exercises name by default according to the user
    favorite language.

    """
    if user_language[0] == "fr":
        exercises_name = exercises_name_fr
        save_an_object(exercises_name, "exercises")
    
    else: #user_language[0] == "en":
        exercises_name = exercises_name_en
        save_an_object(exercises_name, "exercises")