

class Appointment:
    """A base class for all appointments in the system."""
    def __init__(self, appointment_id, patient, staff, time, notes, location):
        self.id = appointment_id
        self.patient = patient
        self.staff = staff
        self.time = time
        self.notes = notes
        self.location = location
