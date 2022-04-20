class PatientFile:

    usernumber = None
    firstname = None
    middlename = None
    lastname = None
    dob = None
    ssid = None

    procedures = []

    def __init__(self, usernumber, firstname, middlename, lastname, dob, ssid, procedures):
        self.usernumber = usernumber
        self.firstname = firstname
        self.lastname = lastname
        self.middlename = middlename
        self.dob = dob
        self.ssid = ssid
        self.procedures = procedures

    def addprocedure(self, procedure):
        self.procedures.append(procedure)
