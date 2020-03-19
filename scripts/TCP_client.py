#You should configure PORT forwarding and NO-IP DDNS together#

from __future__ import print_function
import socket
import sys

import os
os.system("sudo /etc/init.d/dns-clean")

# **** !!! Achtung !!!****
# Most probably your router doesn't like connections to the external ip
# from an inside ip. So you'll need a computer which is really outside 
# of your home network to test it. This is quite a normal behaviour 
# for soho routers.
# Sometimes, some routers don't allow to connect using the external 
# address from inside the LAN.
# ************************

host="localhost"  #tapalanganetcat.ddns.net
#host= socket.gethostbyname("saw-dsr.ddns.net")
port=5552
print("Connecting to %s:%s ..."%(host, port))
client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

#The case of The command (-c) option in netcat
print("succesfully connected to %s\n"%host)
try:
	print(client.recv(1024))
except:
	print("exception server is down")
while True:
	#print("new Loop")
	cmd ="jj"
	client.send(cmd.encode())
	terminal=client.recv(1024);
	print(terminal, end='')
	cmd=raw_input() #cmd = sys.stdin.read() then type CTRL+d to send
	if cmd == "exit()":
		break
	cmd = cmd + "\n"
	client.send(cmd.encode())#client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
	file_buffer=""
	data = ""
	while True:
		data = client.recv(1024)
		file_buffer += data
		if len(data) < 1024:
			break
	print(file_buffer,end='')

client.close()


