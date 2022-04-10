import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="test_db"
)


def analyze_command(sentence):
    sentence = sentence.lower()
    sentence = sentence.split("-")
    sentence = " ".join(sentence)
    print("Altered Sentence: " + sentence)
    if "open" in sentence or "get" in sentence:
        name = sentence.split(" ")[1]
        cursor = db.cursor()
        cursor.execute("SELECT * FROM user WHERE username = \'" + name + "\'")

        result = cursor.fetchall()

        for x in result:
            print(x)
        #<open the patient file>
        #user can say commands in form of file sections
        #mode for just saying the string of requests? i.e. "open 123 birthday" or "open 321 procedure 41 doctor"