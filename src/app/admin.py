from app.user import User

class Admin(User):
    """Represents an admin, inheriting from the base User class."""
    def __init__(self, user_id, name):
        super().__init__(user_id, name)