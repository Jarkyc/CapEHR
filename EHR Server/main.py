# Make the database request ON the server, and send only the data to the client, not the parsed request itself

import socket
import pickle
import word_analysis
import mysql.connector
import database_funcs

s = None

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="test_db"
)


def open_socket():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 8080))
    s.listen(5)
    print("Waiting for connection")
    listen()


def listen():
    conn, addr = s.accept()
    print(f"Establishing connection with: {addr}")
    full_msg = b''
    while True:
        msg = conn.recv(8)
        if msg.endswith(b'~'):
            msg.replace(b'~', b'')
            full_msg += msg
            break
        if not msg:
            break
        full_msg += msg

    parcel = pickle.loads(full_msg)
    type = parcel["type"]
    if type == "LOGIN":
        userLine = parcel["content"]
        userLs = userLine.split(" ")
        username = userLs[0]
        password = userLs[1]

        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM loginusers WHERE username = \'" + username + "\' AND password = \'" + password + "\'")

        rows = cursor.fetchall()
        if (len(rows) == 0):
            conn.send((b'FALSE'))
            conn.close()
        else:
            conn.send((b'TRUE'))
            conn.close()

    elif type == "AUDIO":
        string = parcel["content"]
        print(string)
        word_analysis.analyze_command(string)
        print("connection terminated")

    listen()


# open_socket()
database_funcs.create_procedure("789", "987", "This is a test procedure")
