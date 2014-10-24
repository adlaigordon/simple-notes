# Adlai Jacob Gordon
# notes.py
# simple python script to input and append timestamped notes to a textfile

import time
import datetime

filename = "notes.txt"

while True:
	input_list = []
	while True:
		input_str = input("> ")
		if input_str == "" and len(input_list) > 1 and input_list[-1] == "":
			break
		else:
			input_list.append(input_str)

	newnote = "\n".join(input_list[:-1])
	
	submit = input("Enter to submit | 'n' to trash: ".format(len(newnote)))
	if submit == "":
		now = datetime.datetime.now()
		breakline = "\n-------------------------\n"
		stamp = "{} {} {}, {}{}".format(breakline, time.strftime("%A %b"), now.day, time.strftime("%I:%M %p"), breakline)
		f = open(filename, "a")
		f.write(stamp + newnote + '\n')
		f.close()
		print("-- Note submitted. ({} chars) [{}] --".format(len(newnote), time.strftime("%c")))

	else:
		print("-- Note trashed --")

	print("Begin Typing New Note:")