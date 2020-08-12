from preferences import user_preferences as p


def cmd_go():
	check_text = checking_values()

	if check_text == "go":
		text = "C'est partit !"
	else :
		text = check_text
	
	return text


def checking_values():
	"""
	user_preferences = {
 	"session_duration_min" : 4,
    "exercices_duration" : 30, #secondes
    "break_duration" : 20, #secondes
    "warm_up_duration" : 60, #secondes
    "mini_stretching_duration" : 60, #secondes
    "warning_frequency" : 10, #secondes
    }
	"""
	try:
		int(p["session_duration_min"])
	except ValueError:
		return "La durée de la session doit être un entier."
	
	min_duratation = p["exercices_duration"] + p["break_duration"]
	min_duratation += p["warm_up_duration"] + p["mini_stretching_duration"]

	if p["session_duration_min"]*60 < min_duratation:
		text = "Vos paramètres ne peuvent pas être appliqués."
	else:
		text = "go"
	return text