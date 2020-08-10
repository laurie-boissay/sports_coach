import time


from text_to_speech import say_text


def start_exercice(exercice_name, exercices_duration):
	exercice_start = time.time()
	exercice_end = exercice_start + exercices_duration

	say_text(exercice_name)
	counter = 0
	
	while time.time()  <= exercice_end:
		if exercice_end - 20 <= time.time() and counter == 0:
			say_text("Encore 20 secondes.")
			counter += 1

		elif exercice_end - 10 <= time.time() and counter == 1:
			say_text("Encore 10 secondes.")
			counter += 1

	say_text("Stop.")


exercices_name = [
	"montez les genoux",
	"squat",
	"patineur",
]



	
