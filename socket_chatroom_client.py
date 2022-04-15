import socket;



def client():

	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
		print("Initiating Connection to Server");
		
	except socket.error as err:
		print("Could not setup socket, Something went Wrong");

	#port  over which the computers are connected	
	port = 12345;

	#Name for Client
	username = input('Enter you username: ')

	#ip address of another computer
	ip = input("Enter the ip address of the server: ");

	with s:
	#connecting to the server
		s.connect((ip,port));
		userdata = 'CONNECTED USERNAME: '+username
		s.sendall(userdata.encode());
		print('Log: Waiting for Message....,')
		#recieving the data from server
		data = s.recv(1024);
		print(">> ",data.decode());
		
		while True:
			#Enter message to be sent to server
			data_sent = (input('<< You : '));
			msg = username+': '+data_sent
			temp = msg.encode()
			s.sendall(temp);
			#if empty string is sent
			#connection closes
			if not data_sent:
				break;
			#recieving data from server
			print('Log: Waiting for Message....,')
			data = s.recv(1024);
			print(">> ",data.decode());

	print("Connection closed");

	#close the connection
	s.close();
