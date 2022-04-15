import socket


def server():

	try:
		username = input('Enter your username: ')
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
		print("Initiated COnnevction as Server [-]");

	except socket.error as err:
		print("Socket creation failed");
		
	port = 12345;

	#we will bind the server to listen for requests
	#since we have used empty string instead of ipaddress
	#server will listen to requests coming from any
	#computer on the network
	s.bind(('', port));
	print("Listening for Incomming Connection on Port No.", port);

	#socket will allow 5 unaccepted connections
	#are kept waiting
	#then it will refuse new connections
	s.listen(5);
	print("Listening...");

	while True:
		#accept the connection
		#it returns socket object and
		#adddress of the client
		conn, add = s.accept();
		with conn:
			print("Got connection from ",add);
			print('Log: Waiting for Message....,')

			while True:
				print('Log: Waiting for Message....,')
				data = conn.recv(1024);
				#if no data i.e. empty string is recieved
				#the connection will be closed
				if not data:
					break;


				print('>> ',data.decode());
				#Enter message you want to send to client
				data_sent = (input("<< You : "))
				msg = username+': '+data_sent
				temp = msg.encode()
				conn.sendall(temp);

			
			print("Connection closed");
	s.close();
