
#Find a good universal structure for the response packet and send it to the client.
#Make the database request ON the server, and send only the data to the client, not the parsed request itself
#Dont close server after request

import socket
import pickle
import word_analysis

def server_wait():

    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    print("Waiting for connection")

    conn, addr = s.accept()
    print(f"Establishing connection with: {addr}")
    full_msg = b''
    while True:
        msg = conn.recv(8)
        if len(msg) <= 0:
            break
        full_msg += msg

    parcel = pickle.loads(full_msg)
    string = parcel["content"]
    print(string)
    word_analysis.analyze_command(string)
    print("connection terminated")


server_wait()


