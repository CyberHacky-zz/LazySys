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
        print("Installing Rsyslog...\n")
        os.system('sudo apt install rsyslog -y')
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
    

def rsysreceiver():
    print("Under Devlopment")

def rsyssender():
    print("Under Devlopment")






#Run Main menu
mainmenu()