import time
import math


from text_to_speech import say_text


def start_exercice(exercice_name, exercices_duration, warning_frequency):

	exercice_start = time.time()
	exercice_end = exercice_start + exercices_duration

	ex_text = exercice_name + " " + str(round(exercices_duration)) + " secondes."
	say_text(ex_text)
	
	while time.time() <= exercice_end:
		
		nbr_sec = round(exercice_end - time.time())

		if warning_frequency != 0 and nbr_sec % warning_frequency == 0 and nbr_sec > 0:
			say_text(str(nbr_sec))

	say_text("Stop.")


exercices_name = [
	"montez les genoux",
	"squatte", # This word doesn't exist. It's for pronunciation.
	"patineur",
]



	
