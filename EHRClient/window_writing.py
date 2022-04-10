from tkinter import *
from tkinter.ttk import *
import audio_processing
import main as hub

master = None

def create_master():
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
                 text="Click to start recording")
    btn.bind('<Button-1>', start_recording)
    btn.pack()

    # mainloop, runs infinitely
    mainloop()


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
    widget['text']="Click to start recording"
    widget.bind('<Button-1>', start_recording)
    audio_processing.stop_recording()
    print("activated")
