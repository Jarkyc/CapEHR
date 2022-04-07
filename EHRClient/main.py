import socket
import audio_processing
import pickle
import subprocess
from tkinter import *
from tkinter.ttk import *

master = None
recording_win = None

def make_request():
    # create interface code. Look up the basics for application processes and making sure the application loop doesnt close.
    # create a temporary socket connection with the server. recieve in a universal packet. Find way to make sure application does not close after packet is received.


    parcel = {
        "senderAccount": "",
        "content": audio_processing.transcribe_file("audio.wav"),
    }

    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 65432  # The port used by the server

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:
        s.send(pickle.dumps(parcel))
        s.close()


# function to open a new window
# on a button click
def openNewRecordingWindow():
    # Toplevel object which will
    # be treated as a new window
    global master
    global recording_win
    newWindow = Toplevel(master)
    recording_win = newWindow

    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")

    # sets the geometry of toplevel
    newWindow.geometry("200x200")

    # A Label widget to show in toplevel
    stop = Button(newWindow,
                 text="Click to stop recording",
                 command=stop_recording)
    stop.pack(pady=10)

    newWindow.update()
    audio_processing.start_recording()

def stop_recording():
    audio_processing.stop_recording()
    recording_win.destroy()


def main():
    global master
    master = Tk()

    # sets the geometry of main
    # root window

    width = master.winfo_screenwidth()
    height = master.winfo_screenheight()
    master.geometry("%dx%d" % (width, height))

    label = Label(master,
                  text="This is the main window")

    label.pack(pady=10)

    # a button widget which will open a
    # new window on button click
    btn = Button(master,
                 text="Click to start recording",
                 command=openNewRecordingWindow)
    btn.pack(pady=10)

    # mainloop, runs infinitely
    mainloop()


if __name__ == "__main__":
    main()
