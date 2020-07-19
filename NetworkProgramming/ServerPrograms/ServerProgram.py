import socket

#myHostName = socket.gethostname()
port = 9999
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket,bind(  ('192.168.43.231',9090) )
#serverSocket.bind((myHostName,port))
serverSocket.listen(5)

while (True):
	print('Served Program Started and Waiting for Client to Connect...')
	clientSocket,address = serverSocket.accept()
	print(str(clientSocket))
	print("Got Connection from %s"%str(address))
	msg='Thank you for connecting'+ "\r\n"
	clientSocket.send(msg.encode('ascii'))
	clientSocket.close()