# Source: https://www.thepythoncode.com/article/make-a-chat-room-application-in-python
import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back

# init colors
init()

#set the available colors
colors = [
	Fore.BLUE,
	Fore.CYAN,
	Fore.GREEN,
	Fore.LIGHTBLACK_EX,
	Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,
	Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX,
	Fore.LIGHTYELLOW_EX, Fore.MAGENTA,
	Fore.RED,
	Fore.WHITE,
	Fore.YELLOW
]

# choose a random color for the client
client_color = random.choice(colors)

#server's IP address
#if the server is not on this machine, put the private(network) IP address
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5002 # server's port
separator_token = "<SEP>" # used to separate client name and message

#initialize TCP socket
s = socket.socket()
print(f"Connecting to {SERVER_HOST}:{SERVER_PORT}...")
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")

#promt the client for a name
name = input("Enter your name: ")

#listens for server messages
def listen_for_messages():
	while True:
		message = s.recv(1024).decode()
		print("\n", + message)

#make a thread that listens for messages to this client & prints them
t = Thread(target=listen_for_messages)
#make the thread daemon so it ends whenever the main thread ends
t.daemon = True
# start the thread
t.start()

# We want 
