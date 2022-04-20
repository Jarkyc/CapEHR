import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="test_db"
)


def create_procedure(patientid, doctorid, details):
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO procedures(patientid, doctorid, details) VALUES(\'" + patientid + "\', \'" + doctorid + "\', \'" +
        details + "\');")
    db.commit()