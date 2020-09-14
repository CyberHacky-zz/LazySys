#! /usr/bin/env python3
#
# Query package state by installation path

import os
import subprocess
import sys
import re




#Title print

logo = ('''

    ██╗      █████╗ ███████╗██╗   ██╗ ██████╗██╗   ██╗ ██████╗
    ██║     ██╔══██╗╚════██║╚██╗ ██╔╝██╔════╝╚██╗ ██╔╝██╔════╝  
    ██║     ███████║  ███╔═╝ ╚████╔╝ ╚█████╗  ╚████╔╝ ╚█████╗
    ██║     ██╔══██║██╔══╝    ╚██╔╝   ╚═══██╗  ╚██╔╝   ╚═══██╗
    ███████╗██║  ██║███████╗   ██║   ██████╔╝   ██║   ██████╔╝
    ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═════╝    ╚═╝   ╚═════╝
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[!] This Tool Must Run As ROOT [!] - Created By : SecFirm Team\n\n''')


# Print Logo on startup
print(logo)


#Main Menu

def mainmenu():
    print ("""
   {1}--Rsyslog Version
   {2}--Install Rsyslog
   {3}--Configuration
   {0}--Exit
 """)
    choice = input("SecFirm~# ")
    if choice == "1":
        rversion()
    elif choice == "2":
        installrsyslog()
    elif choice == "3":
        conrsyslog()
    elif choice == "0":
        print("Thanks for Using SecFirm")
        os.system('clear'), sys.exit()
    elif choice == "":
        print(logo)
        print("\033[1m [+] Kindly Choose One Option \033[0m")
        mainmenu()
    else:
        print(logo)
        mainmenu()

def rversion():

    rc = subprocess.call(['which', 'rsyslogd'])
    if rc == 0:
        print ('Rsyslog installed!\n')
        os.system('rsyslogd -v')
        mainmenu()
    else:
        print ('Rsyslog missing in path!')
        startinstallrsys()

def startinstallrsys():

    installrsys = input("Do You want to Install Rsyslog? [Y/N] = ")

    if installrsys == "Y":
        installrsyslog()
    else:
        print("RSyslog Configuration process is Stoped")
        mainmenu()

def installrsyslog():

    print('Rsyslog Installation Started - Updating Repository')
    os.system('sudo add-apt-repository ppa:adiscon/v8-devel')
    print('Bingo - Repository Updated')

    print('System Update Process Running')
    os.system('sudo apt-get update')
    print('Bingo - System Updated')

    print('Rsyslog Installtion Process Running')
    os.system('sudo apt-get install rsyslog')
    print('Bingo - Rsyslog Installed Succesfully')    

    mainmenu()



def conrsyslog():
    
    print ("""
   {1}--Configure Remote Server - (Log Receiver)
   {2}--Configure Remote Client - (Log Sender)
   {0}--Exit
 """)
    choice = input("LazySys~# ")
    if choice == "1":
        rsysreceiver()
    elif choice == "2":
        rsyssender()
    elif choice == "0":
        print("Thanks for Using SecFirm")
        os.system('clear'), sys.exit()
    elif choice == "":
        print("\033[1m [+] Kindly Choose One Option \033[0m")
        conrsyslog()
    else:
        print(logo)
        mainmenu()
    


def rsyssender():
    print("Under Devlopment")

def rsysreceiver():

    print('\033[1m [+] Rsyslog Server Configuration Process Started \033[0m')
    print('\033[1m [+] Started Rsyslog Service  \033[0m')
    os.system('sudo systemctl start rsyslog')
    os.system('sudo systemctl enable rsyslog')
    
    print('\033[1m [+] Configuring UFW Firewall Rules   \033[0m')
    os.system('sudo ufw allow 514/udp')
    os.system('sudo ufw allow 50514/tcp')

# Server Setup Code is here - it's unstable

def rudpone():
	reading_file = open("rsyslog.conf", "r")
	new_file_content = ""

	for line in reading_file:
		stripped_line = line.strip()
		new_line = stripped_line.replace('#module(load="imudp")', 'module(load="imudp")')
		new_file_content += new_line +"\n"
	
	reading_file.close()
	writing_file = open("rsyslog.conf", "w")
	writing_file.write(new_file_content)
	writing_file.close()


def rudptwo():
	reading_file = open("rsyslog.conf", "r")
	new_file_content = ""

	for line in reading_file:
		stripped_line = line.strip()
		new_line = stripped_line.replace('#input(type="imudp" port="514")', 'input(type="imudp" port="514")')
		new_file_content += new_line +"\n"
	
	reading_file.close()
	writing_file = open("rsyslog.conf", "w")
	writing_file.write(new_file_content)
	writing_file.close()

def rtcpone():
	reading_file = open("rsyslog.conf", "r")
	new_file_content = ""

	for line in reading_file:
		stripped_line = line.strip()
		new_line = stripped_line.replace('#module(load="imtcp")', 'module(load="imtcp")')
		new_file_content += new_line +"\n"
	
	reading_file.close()
	writing_file = open("rsyslog.conf", "w")
	writing_file.write(new_file_content)
	writing_file.close()


def rtcptwo():
	reading_file = open("rsyslog.conf", "r")
	new_file_content = ""

	for line in reading_file:
		stripped_line = line.strip()
		new_line = stripped_line.replace('#input(type="imtcp" port="514")', 'input(type="imtcp" port="514")')
		new_file_content += new_line +"\n"
	
	reading_file.close()
	writing_file = open("rsyslog.conf", "w")
	writing_file.write(new_file_content)
	writing_file.close()


rudpone()
rudptwo()
rtcpone()
rtcptwo()

# Be aware - Don't Touch unneccesory
    

    




#Run Main menu
mainmenu()