import socket
import audio_processing
import pickle


def make_request():
    #create interface code. Look up the basics for application processes and making sure the application loop doesnt close.
    #create a temporary socket connection with the server. recieve in a universal packet. Find way to make sure application does not close after packet is received.


    #audio_processing.record_to_file("audio.wav")

    parcel = {
        "senderAccount": "",
        "content": audio_processing.transcribe_file("audio.wav"),
    }

    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 65432        # The port used by the server


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:

        s.send(pickle.dumps(parcel))
        s.close()


make_request()