"""
Author: Pitipat Phasee
Last Modified: 2025-10-06
Version: 1.0

Controller for Daily Notes
"""

from app.daily_notes.services.daily_notes_service import DailyNotesService

class DailyNotesController:
    """Controller layer for Daily Notes feature."""

    def __init__(self, manager):
        self.service = DailyNotesService(manager)

    def add_note(self, staff_id, resident_id, note_text):
        return self.service.create_note(staff_id, resident_id, note_text)

    def view_notes_by_staff(self, staff_id):
        return self.service.get_notes_by_staff(staff_id)

    def view_notes_by_resident(self, resident_id):
        return self.service.get_notes_by_resident(resident_id)

    def view_all_notes(self):
        return self.service.get_all_notes()
