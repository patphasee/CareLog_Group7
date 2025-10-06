"""
Author: Pitipat Phasee
Last Modified: 2025-10-06
Version: 1.0

Service object for daily notes
"""

from datetime import datetime
from app.daily_notes.models.daily_note import DailyNote

class DailyNotesService:
    """Handles creation and retrieval of daily notes."""

    def __init__(self, manager):
        self.manager = manager

    def create_note(self, staff_id, resident_id, note_text):
        timestamp = datetime.now().isoformat(timespec="seconds")
        new_note = DailyNote(
            id=self.manager.next_daily_note_id,
            staff_id=staff_id,
            resident_id=resident_id,
            note=note_text,
            timestamp=timestamp
        )
        self.manager.daily_notes.append(new_note)
        self.manager.next_daily_note_id += 1
        self.manager._save_data()
        return new_note

    def get_notes_by_staff(self, staff_id):
        return [n for n in self.manager.daily_notes if n.staff_id == staff_id]

    def get_notes_by_resident(self, resident_id):
        return [n for n in self.manager.daily_notes if n.resident_id == resident_id]

    def get_all_notes(self):
        return self.manager.daily_notes
