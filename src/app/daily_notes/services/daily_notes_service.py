"""
Author: Pitipat Phasee
Last Modified: 2025-10-05
Version: 1.0

Daily notes service object
"""

from app.daily_notes.models.daily_note import DailyNote

class DailyNotesService:
    """Service handling Daily Notes CRUD logic."""

    def __init__(self):
        self.notes = []
        self.next_id = 1

    def create_note(self, resident_id, staff_id, date, note_content, prescription, patient_instructions):
        note = DailyNote(self.next_id, resident_id, staff_id, date, note_content, prescription, patient_instructions)
        self.notes.append(note)
        self.next_id += 1
        return note

    def get_notes_by_resident(self, resident_id):
        return [note for note in self.notes if note.resident_id == resident_id]

    def update_note(self, note_id, new_content):
        for note in self.notes:
            if note.id == note_id:
                note.note_content = new_content
                return note
        return None

    def delete_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                self.notes.remove(note)
                return True
        return False
