import socket
from threading import Thread
'''
from library import method
import random
import will import all the sub-libraries and methods
random.choice(),random.randint(),random.uniform()
from random import choice
choice() directly invoke the method() no need like random.choice()
you cannot use randint or uniform
'''

# refer: https://docs.python.org/3/library/socket.html
NO_OF_PARALLELS = 5  # No of concurrent requests to handle.
HOST = socket.gethostname()  # Can be taken dynamically using input() command. Remember to type convert!
PORT = 2020  # PORT to bind to. Can be taken dynamically using input() command. Remember to type convert!
PROTOCOL = socket.AF_INET  # Address & Protocol family (Change this for IPv6) 
SOC_TYPE = socket.SOCK_STREAM  # Using TCP  
ENCODING = 'ascii'
BUFFER = 4096
WELCOME = "Hello Client \n Welcome to Chat Server! :)"
# ENCRYPTION = None  # These features can be added later if required.
# SLEEP_TIME = 0 
FLAG = True

# Listen before talking
def client_handler(client, addr):
    print("Connection at address:", addr, "started.")
    print("Sending Welcome message.")
    client.send(WELCOME.encode(ENCODING))
    print("Completed welcome!")
    print("Press 'exit' at any time to exit the chat.")
    print("Press 'Enter' at any time to wait for other person's reply!\n (NOTE: If other person is doing this then you will enter an infinte wait!!)")
    while True:
        msg_to_send = input("Me: ")
        if msg_to_send == 'exit':
            client.send("exit".encode(ENCODING))
            client.close()
            print("Closed connection.")
            break
        elif msg_to_send == '':
            pass
        else:
            client.send(msg_to_send.encode(ENCODING))  # Speaking here.
        msg = client.recv(BUFFER).decode(ENCODING)  # Listening here.
        if msg == "exit":
            print("Client closed the connection.")
            break
        else:
            print("Client: ",msg)

    client.close()
    print("Closed:",addr)
    
    
# Setup the server.
server = socket.socket(PROTOCOL,SOC_TYPE)
server.bind((HOST,PORT))
server.listen(NO_OF_PARALLELS)  

print("Server Setup successfull.\nListening for connections on:.",HOST,PORT)

while FLAG:
    x = input("Enter 'shutdown' to kill the server or anything else to continue listening.\n")
    if x == 'shutdown':
        print("Shutdown command recieved. Once you exit current chat sessions server will close.")
        break
    print("\nLooking for connections.")
    client, addr = server.accept()  
    client_handler(client, addr)
    
server.close()  # Cleanup before you leave.
print("Server closed.")