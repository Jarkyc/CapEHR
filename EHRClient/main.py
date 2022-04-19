import socket
import audio_processing
import pickle
import window_writing

def make_request(type, cont):
    # create interface code.
    # create a temporary socket connection with the server. recieve in a universal packet.
    try:
        content = None
        if type == "AUDIO":
            content = audio_processing.transcribe_file("audio.wav")
        elif type == "LOGIN":
            content = cont

        parcel = {
            "type": type,
            "senderAccount": "",
            "content": content,
        }

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 8080))

        s.send(pickle.dumps(parcel) + b'~')
        full_msg = s.recv(1024)
        s.close()

        return full_msg.decode()
    except (ConnectionRefusedError, ConnectionResetError):
        window_writing.error_window("SERVER")


def main():
    window_writing.create_master()


if __name__ == "__main__":
    main()
