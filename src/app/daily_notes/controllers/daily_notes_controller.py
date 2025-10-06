"""
Author: Pitipat Phasee
Last Modified: 2025-10-05
Version: 1.0

Daily notes controller object
"""

from app.daily_notes.services.daily_notes_service import DailyNotesService

class DailyNotesController:
    """Controller for Daily Notes."""

    def __init__(self):
        self.service = DailyNotesService()

    def add_daily_note(self, resident_id, staff_id, date, note_content, prescription, patient_instructions):
        return self.service.create_note(resident_id, staff_id, date, note_content, prescription, patient_instructions)

    def view_resident_notes(self, resident_id):
        return self.service.get_notes_by_resident(resident_id)

    def edit_note(self, note_id, new_content):
        return self.service.update_note(note_id, new_content)

    def remove_note(self, note_id):
        return self.service.delete_note(note_id)
