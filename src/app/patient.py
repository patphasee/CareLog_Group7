from app.user import User

class Patient(User):
    """Represents a patient, inheriting from the base User class."""
    def __init__(self, user_id, name, dob=None, gender=None,
                 allergies=None, contact=None, assigned_staff_ids=None, 
                 preferences=None,notes=None):
        super().__init__(user_id, name)
        self.dob = dob
        self.gender = gender
        self.allergies = allergies if allergies is not None else {}
        self.contact = contact if contact is not None else {}
        self.preferences = preferences if preferences is not None else {}
        self.notes = notes if notes is not None else {}
        self.assigned_staff_ids = assigned_staff_ids if assigned_staff_ids is not None else []