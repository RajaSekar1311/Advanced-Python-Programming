import socket
import io
import cv2
import numpy

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
				fd = open('new_'+filename,'wb')
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
				print('The downloaded video file is going to play.. please wait...')
				downloadedFile = 'new_'+filename
				print('The downloaded video file name is:  '+downloadedFile)
				video_capture = cv2.VideoCapture(downloadedFile)
				while(video_capture.isOpened()):
					ret_value,frame = video_capture.read()
					cv2.imshow('downloadedFile',frame)
					cv2.waitKey(1)
				video_capture.release()
				cv2.destrolAllWindows()
			else:
				print('File does not exist!')
		s.close()
if __name__ == '__main__':
	Main()