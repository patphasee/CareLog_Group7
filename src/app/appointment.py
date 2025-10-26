class Appointment:
    def __init__(self, id, patient_id, staff_id, date, time, purpose, status="Scheduled", location=""):
        self.id = id
        self.patient_id = patient_id
        self.staff_id = staff_id
        self.date = date       
        self.time = time        
        self.purpose = purpose
        self.status = status
        self.location = location
