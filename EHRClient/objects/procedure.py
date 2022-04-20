class Procedure:

    patientid = None
    doctor = None
    details = None

    def __init__(self, patientid, doctor, details):
        self.patientid = patientid
        self.doctor = doctor
        self.details = details