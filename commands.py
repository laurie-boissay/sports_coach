import time


from text_to_speech import say_text


def cmd_go():
	go = "C'est partit !"
	say_text(go)
	return time.time()