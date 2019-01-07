import os
import subprocess

command="whoami"

def run(**args):
  print("[*] In ExecuteCmd module.") #Todelete
  global command
  command = command.rstrip() #command devient tuple with args
  print(command)
  try:
  	output = subprocess.check_output(command,stderr=subprocess.STDOUT, shell=True)
  except:
  	output = "Failed to execute command: command not found, Permission denied or dpkg error (no internet,...)."

  return str(output)




def getUser():
	if os.name == 'posix':
		userName = os.getenv("USER")
	elif os.name == 'nt':
		userName = os.getenv("USERNAME")
