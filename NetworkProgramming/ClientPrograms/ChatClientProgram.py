import socket



HOST = socket.gethostname()  
PORT = 2020 
PROTOCOL = socket.AF_INET 
SOC_TYPE = socket.SOCK_STREAM  
ENCODING = 'ascii'
BUFFER = 4096

server = socket.socket(PROTOCOL, SOC_TYPE)
print("Client setup complete.")

server.connect((HOST, PORT))
print("Server connect successfull.\n Waiting for Server to join the conversation.\n")
msg = server.recv(BUFFER)
print("Welcome message from server: \n",msg.decode(ENCODING))
print("Press 'exit' at any time  to exit the chat.")
print("Press 'Enter' at any time to wait for other person's reply!\n (NOTE: If other person is doing this then you will enter an infinte wait!!)")

# Speaks before listening.

while True:
    msg_to_send = input("Me: ")
    if msg_to_send == 'exit':
        server.send("exit".encode(ENCODING))
        server.close()
        print("Closed connection.")
        break
    elif msg_to_send == '':
        pass
    else:
        server.send(msg_to_send.encode(ENCODING))  # Speaking here.
    
    msg = server.recv(BUFFER).decode(ENCODING)  # Listening here.
    if msg == "exit":
        print("Server closed the connection.")
        break
    else:
        print("Server: ",msg)
    

server.close()