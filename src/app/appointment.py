

class Appointment:
    """A base class for all appointments in the system."""
    def __init__(self, appointment_id, patient, staff, time, date, notes, location):
        self.appointment_id = appointment_id
        self.patient = patient
        self.staff = staff
        self.date = date,
        self.time = time
        self.notes = notes
        self.location = location
