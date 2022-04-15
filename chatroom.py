import socket
import os
import reverse_shell
from socket_chatroom_client import client
from socket_chatroom_server import server

def Menu():
    os.system('cls')
    print('[1] INITIATE AS SERVER')
    print('[2] CONNECT TO SERVER')
    print('[3] INITIATE REVERSE SHELL (CMD)')
    print('[4] ACCEPT REVERSE SHELL (CMD)')

    option = int(input('SELECT YOR MODE: '))

    if option == 1:
        os.system('cls')
        server()

    elif option == 2:
        os.system('cls')
        client()

    elif option == 3:
        os.system('cls')
        reverse_shell.initiate_reverse_shell()

    elif option == 4:
        os.system('cls')
        reverse_shell.get_reverse_shell()

    else:
        os.system('cls')
        Menu()
        print('INVALID OPTION')

Menu()