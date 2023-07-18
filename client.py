import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER,PORT)

#create client socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def sendMessage(msg):
    message = msg.encode('utf-8')
    msg_length = len(message)
    send_length = str(msg_length).encode('utf-8')
    send_length += b' ' * (64-len(send_length))
    client.send(send_length)
    client.send(message)

sendMessage("Hello devshehan!!!")
sendMessage("!DISCONNECT")