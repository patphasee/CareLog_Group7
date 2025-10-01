from app.user import User

class MedStaff(User):
    """Represents a teacher."""
    def __init__(self, user_id, name, speciality):
        super().__init__(user_id, name)
        self.speciality = speciality
