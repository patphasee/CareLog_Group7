from app.user import User

class Patient(User):
    """Represents a patient, inheriting from the base User class."""
    def __init__(self, user_id, name, dob=None, gender=None,
                 allergies=None, contact=None, assigned_staff_ids=None, 
                 preferences=None, current_patient=True):
        super().__init__(user_id, name)
        self.dob = dob
        self.assigned_staff_ids = assigned_staff_ids if assigned_staff_ids is not None else []
        self.gender = gender
        self.allergies = allergies if allergies is not None else []
        self.contact = contact if contact is not None else {
            "name": "",
            "contact": ""
        }
        self.preferences = preferences if preferences is not None else ""
        self.current_patient = current_patient
