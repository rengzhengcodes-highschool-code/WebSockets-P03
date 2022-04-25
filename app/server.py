# Source: https://www.thepythoncode.com/article/make-a-chat-room-application-in-python
import socket
from threading import Thread
from sys import exit
# server's IP address
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5002
separator_token = "<SEP>" # separates client name from the message

#initialize list/set of all connected client's sockets
client_sockets = set()
#create a TCP socket with socket object
s = socket.socket()
#make the port as reusable port -- multiple people can use the same port
"""
SOL_SOCKET -- Defines protocol level (this default is just the socket level, just the socket people)
"""
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind the socket to the address and port specified
s.bind((SERVER_HOST, SERVER_PORT))
# listen for upcoming connections
"""
Argument specifies number of connections allowed before it starts refusing connections
"""
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

def listen_for_client(cs):
	"""
	Keeps listening for a message from the `cs` socket. Whenever a message is received, it broadcasts it to all other connected clients.
	"""
	while True:
		try:
			# keep listening for a message from `cs` socket
			msg = cs.recv(1024).decode()
		except Exception as e:
			# client no longer connected
			# remove it from the set
			print(f"[!] Error: {e}")
			client_sockets.remove(cs)
		else:
			# if we received a message, replace the <SEP> with ": " for nice printing
			msg = msg.replace(separator_token, ": ")
		#iterate over all connected sockets
		for client_socket in client_sockets:
			# and send the message
			client_socket.send(msg.encode())

while True:
	# we keep listening for new connections all the time
	client_socket, client_address = s.accept()
	print(f"[+] {client_address} connected.")
	# add the new connected client to connected sockets
	client_sockets.add(client_socket)
	# start a new thread that listens for each client's messages
	t = Thread(target=listen_for_client, args=(client_socket,)) #question, difference between thread and async?
	# make the thread daemon so it ends whenever the main thread ends (doesn't continue when the program ends)
	t.daemon = True
	# start the thread
	t.start()

# close client sockets
for cs in client_sockets:
	cs.close()
#close server socket
s.close()
exit()
