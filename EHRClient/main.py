import socket

#create interface code. Look up the basics for application processes and making sure the application loop doesnt close.
#create voice recording function
#create a temporary socket connection with the server. recieve in a universal packet. Find way to make sure application does not close after packet is received.


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    s.send(bytes("Sally sells seashells by the seashore. She sells seashells on the seashell shore. The seashells she sells are seashore shells, Of that I’m sure. She sells seashells by the seashore. She hopes she will sell all her seashells soon. If neither he sells seashells Nor she sells seashells, Who shall sell seashells? Shall seashells be sold?", "utf-8"))
s.close()
print("Data has been sent")