"""
Author: Pitipat Phasee
Last Modified: 2025-10-05
Version: 1.0

Daily note object
"""
import datetime as dt
class Careplan:
    """Data model for a careplan."""

    def __init__(self, id, resident_id, staff_id, date, note_content, prescription, patient_instructions):
        """
        Initialize a DailyNote object.

        Args:
            id (int): Unique ID for the note
            resident_id (int): Resident associated with the note
            staff_id (int): Staff member who created the note
            date (datetime): Date of the note (YYYY-MM-DD)
            note_content (str): Text content of the note
            prescription (str): Text content of prescriptions
            patient_instructions (str): Text for patient instructions.
        """
        self.id = id
        self.resident_id = resident_id
        self.staff_id = staff_id
        self.date = date
        self.note_content = note_content
        self.prescription = prescription
        self.patient_instructions = patient_instructions
