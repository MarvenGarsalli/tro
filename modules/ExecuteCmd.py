import os
import subprocess

command="whoami"

def run(**args):
  # trim the newline
  command = command.rstrip() #command devient tuple with args
  try:
  	output = subprocess.check_output(command,stderr=subprocess.STDOUT, shell=True)
  except:
  	output = "Failed to execute command: command not found, Permission denied or dpkg error (no internet,...).\r\n"
  # send the output back to the client
  return output

def getUser():
	if os.name == 'posix':
		userName = os.getenv("USER")
	elif os.name == 'nt':
		userName = os.getenv("USERNAME")
