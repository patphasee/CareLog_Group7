"""
Author: Pitipat Phasee
Last Modified: 2025-10-06
Version: 1.0

Daily Note data object
"""

class DailyNote:
    """Data model for a daily note."""

    def __init__(self, id, staff_id, resident_id, note, timestamp):
        """
        Initialize a DailyNote object.

        Args:
            id (int): Unique ID for the note
            staff_id (int): ID of the staff member who wrote it
            resident_id (int): ID of the patient/resident
            note (str): The text of the daily note
            timestamp (str): When the note was created (ISO format)
        """
        self.id = id
        self.staff_id = staff_id
        self.resident_id = resident_id
        self.note = note
        self.timestamp = timestamp
