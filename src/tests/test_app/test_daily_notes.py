import pytest
import os
from app.daily_notes.models.daily_note import DailyNote
from app.daily_notes.services.daily_notes_service import DailyNotesService
from app.daily_notes.controllers.daily_notes_controller import DailyNotesController

#create a fake manager to avoid saving data to files during tests
class FakeManager:
    def __init__(self):
        self.daily_notes = []
        self.next_daily_note_id = 1
    def _save_data(self): pass  


def test_daily_note_basic_fields():
    note = DailyNote(
        id=1,
        staff_id=10,
        resident_id=20,
        note="Patient is recovering well",
        timestamp="2025-10-25T09:00:00"
    )
    assert note.id == 1
    assert note.staff_id == 10
    assert note.resident_id == 20
    assert note.note == "Patient is recovering well"
    assert note.timestamp == "2025-10-25T09:00:00"


def test_create_and_get_notes_service():
    manager = FakeManager()
    service = DailyNotesService(manager)

    note = service.create_note(10, 20, "Patient stable")
    assert note.id == 1
    assert note.note == "Patient stable"
    assert note in manager.daily_notes

    notes = service.get_notes_by_resident(20)
    assert len(notes) == 1

def test_controller_add_and_view():
    controller = DailyNotesController(FakeManager())

    note = controller.add_note(10, 20, "Vitals normal")
    assert note.note == "Vitals normal"

    result = controller.view_notes_by_resident(20)
    assert len(result) == 1
    assert result[0].staff_id == 10