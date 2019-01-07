import os

def run(**args):
	print("[*] In dirlister module.") #Todelete
	files = os.listdir(".")
	return str(files)
