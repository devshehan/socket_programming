import socket
#creating multiple tread on one python program
import threading

PORT = 5050

#took by terminal
#this my
SERVERCustom = "127.0.1.1"
# print(f"get using terminal: {SERVERCustom}")

#get host by address
SERVER = socket.gethostbyname(socket.gethostname())
# print(f"Get using sockets: {SERVER}")


#bind port and address
ADDR = (SERVER,PORT)

#create socket
#                           family          type
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
 

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True;
    while connected:
        msg_length = conn.recv(64).decode('utf-8')
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode('utf-8')

            if msg == "!DISCONNECT":
                    connected = False
            
            print(f"[{addr}] {msg}")
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.active_count()-1}")


print("[STARTING] server is starting")
start()