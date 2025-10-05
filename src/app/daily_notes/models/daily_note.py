"""
Author: Pitipat Phasee
Last Modified: 2025-10-05
Version: 1.0

Daily note object
"""

class DailyNote:
    """Data model for a daily note."""

    def __init__(self, id, resident_id, staff_id, date, note_content):
        """
        Initialize a DailyNote object.

        Args:
            id (int): Unique ID for the note
            resident_id (int): Resident associated with the note
            staff_id (int): Staff member who created the note
            date (str): Date of the note (YYYY-MM-DD)
            note_content (str): Text content of the note
        """
        self.id = id
        self.resident_id = resident_id
        self.staff_id = staff_id
        self.date = date
        self.note_content = note_content
