import audio_processing

#receive request via file
#note: move voice recording to the client application
#transcribe voice file via audio_processing.transcribe_file()
#Find a good universal structure for the response packet and send it to the client.
#Make the database request ON the server, and send only the data to the client, not the parsed request itself
#Dont close server after request

#audio_processing.record_to_file("test.wav")
#audio_processing.transcribe_file("test.wav")

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
print("Waiting for connection")

full_msg = ''
while True:
    conn, addr = s.accept()
    print(f"Establishing connection with: {addr}")

    msg = conn.recv(8)
    print(msg.decode("utf-8"))
    if(len(msg) <= 0):
        break
    full_msg += msg.decode("utf-8")
print(full_msg)
