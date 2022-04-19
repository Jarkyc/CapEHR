import tkinter
from tkinter import *
from tkinter.ttk import *
import audio_processing
import main as hub
import winsound

master = None
username = None
password = None


def create_master():
    global master
    global username
    global password
    master = Tk()
    master.title("CapEHR")

    # sets the geometry of main
    # root window

    width = master.winfo_screenwidth()
    height = master.winfo_screenheight()
    master.geometry("%dx%d" % (width, height))

    label = Label(master,
                  text="Enter in login information")
    label.pack
    label.place(x=(master.winfo_screenwidth() / 2) - 20)
    label.update()

    # a button widget which will open a
    # new window on button click

    userLabel = Label(master, text="Username:")
    userLabel.pack()
    userLabel.place(x=(master.winfo_screenwidth() / 2) - 40, y=label.winfo_height())

    userLabel.update()

    username = StringVar()
    usernameEntry = Entry(master, textvariable=username)
    usernameEntry.pack()
    usernameEntry.place(x=(master.winfo_screenwidth() / 2) + userLabel.winfo_width() / 2, y=userLabel.winfo_height())

    passLabel = Label(master, text="Password:")
    passLabel.pack()
    passLabel.update()
    passLabel.place(x=(master.winfo_screenwidth() / 2) - 40, y=userLabel.winfo_height() + passLabel.winfo_height() + 5)

    password = StringVar()
    passwordEntry = Entry(master, textvariable=password, show="*")
    passwordEntry.pack()
    passLabel.update()
    passwordEntry.place(x=(master.winfo_screenwidth() / 2) + passLabel.winfo_width() / 2,
                        y=passLabel.winfo_rooty() - passLabel.winfo_width() / 2)

    passwordEntry.update()
    btn = Button(master,
                 text="Login")
    btn.bind('<Button-1>', login)
    btn.pack()
    btn.update()
    btn.place(x=(master.winfo_screenwidth() / 2), y=passwordEntry.winfo_height() + btn.winfo_height() * 2)

    # mainloop, runs infinitely
    master.iconbitmap(r'C:\Users\chuck\Downloads\capehr-icon.ico')
    mainloop()


def login(event):
    global username
    global password

    user = username.get()
    passw = password.get()

    x = "test"
    y = "password"

    request = hub.make_request("LOGIN", user + " " + passw)

    if request != "TRUE":
        error = Label(master, text="Please enter valid login credentials")

        error.pack()
        widget = event.widget
        error.update()
        error.place(x=widget.winfo_rootx() - (error.winfo_width() / 2), y=widget.winfo_rooty() + error.winfo_height())
    else:
        create_hub()



def create_hub():
    global master
    for widget in master.winfo_children():
        widget.destroy()

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
                 text="Click to start recording")
    btn.bind('<Button-1>', start_recording)
    btn.pack()


# function to open a new window
# on a button click
def start_recording(event):
    widget = event.widget
    widget['text'] = "Click to stop recording"
    widget.bind('<Button-1>', stop_recording)

    root = widget.winfo_toplevel()
    root.update()
    audio_processing.start_recording()


def stop_recording(event):
    widget = event.widget
    widget['text'] = "Click to start recording"
    widget.bind('<Button-1>', start_recording)
    audio_processing.stop_recording()
    print("activated")


def error_window(err):
    newWindow = Toplevel(master)
    newWindow.title("Error")

    newWindow.geometry("600x100")

    if err == "SERVER":
        label = Label(newWindow, text="Trouble contacting server. Make sure it is online.")
        label.pack()

    newWindow.update()
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
