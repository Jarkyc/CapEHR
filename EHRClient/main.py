import socket
import audio_processing
import pickle
from tkinter import *
from tkinter.ttk import *

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


#make_request()
master = Tk()

# sets the geometry of main
# root window
master.geometry("200x200")


# function to open a new window
# on a button click
def openNewWindow():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(master)

    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")

    # sets the geometry of toplevel
    newWindow.geometry("200x200")

    # A Label widget to show in toplevel
    Label(newWindow,
          text="This is a new window").pack()


label = Label(master,
              text="This is the main window")

label.pack(pady=10)

# a button widget which will open a
# new window on button click
btn = Button(master,
             text="Click to open a new window",
             command=openNewWindow)
btn.pack(pady=10)

# mainloop, runs infinitely
mainloop()
