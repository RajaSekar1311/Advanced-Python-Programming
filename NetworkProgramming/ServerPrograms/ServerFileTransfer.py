import socket
import threading
import os

def RetrFile(name,sock):
	print('control is before receiving the file name from client')
	filename = sock.recv(1024).decode()
	print('control is after receving the file name from client')
	print('The file name received from the client is :'+filename)
	if os.path.isfile(filename):
		print('Inside the IF of server code')
		msg = "EXISTS:"+str(os.path.getsize(filename))
		print(msg)
		sock.send(msg.encode())
		userResponse = sock.recv(1024).decode()
		print("The client responsed as :"+userResponse[:2])
		if userResponse[:2] == 'OK':
			with open(filename,'rb') as f:
				bytesToSend = f.read(1024)
				sock.send(bytesToSend)
				while (bytesToSend):
					bytesToSend = f.read(1024)
					sock.send(bytesToSend)
		else:
			sock.send("ERROR".encode())
		
	else:
		sock.send("File Does not Exist".encode())
	sock.close()
	
def Main():
	host = socket.gethostname()
	port = 5000
	
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#Creating the Server socket
	s.bind((host,port)) #bind the host and port
	
	s.listen(5)
	
	print ('Server Started')
	while True:
		c,addr = s.accept()
		print ('client connected ip:<'+str(addr)+'>')
		#threading.Thread() method initiate a thread, the object is t
		t = threading.Thread(target=RetrFile, args=('retrThread',c))
		print('thread about to initiate')
		#thread object.start() method starts the thread, execution of the thread starts
		t.start()
	s.close()

if __name__ == '__main__':
	Main()













	