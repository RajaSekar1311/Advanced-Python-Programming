import socket

def Main():
	host = socket.gethostname()
	port = 5000
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((host,port))
	
	filename = input("Filename?-> ")
	if filename != 'q':
		s.send(filename.encode())
		data = s.recv(1024).decode()
		if data[:6] == 'EXISTS':
			filesize = (data[7:])
			message = input("File Exists, "+str(filesize)+"Bytes, download? (Y/N)? -> ")
			if message == 'Y':
				s.send('OK'.encode())
				fd = open('Duplicate_From_Server_'+filename,'wb')
				data = s.recv(1024)
				totalRecv = len(data)
				print('The totalRecv has a value: '+str(totalRecv))
				print('The type of totalRecv is: '+str(type(totalRecv)))
				print('The filesize has a value: '+filesize)
				print('The type of filesize is :'+str(type(filesize)))
				print('The type of data is:  '+str(type(data)))
				fd.write(data)
				size = int(filesize)
				print('The value of size is :'+str(size))
				print('The type of size is now converted to :'+str(type(size)))
				while (totalRecv < size):
					data = s.recv(1024)
					totalRecv+=len(data)
					fd.write(data)		
				print('Download Complete!')	
		s.close()

if __name__ == '__main__':
	Main()