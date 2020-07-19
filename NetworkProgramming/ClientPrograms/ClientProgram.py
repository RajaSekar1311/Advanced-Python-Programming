import socket
#Only when Server and Client are running in same machine
#myHosyName = socket.gethostname()
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('10.14.51.65',9999))
msg = clientSocket.recv(1024)
print(msg.decode('ascii'))
clientSocket.close()