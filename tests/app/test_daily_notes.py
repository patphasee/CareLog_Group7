"""
Author: Pitipat Phasee
Last Modified: 2025-10-05
Version: 1.0

Test script for Daily Notes module
"""

from daily_notes.controllers.daily_notes_controller import DailyNotesController

def main():
    controller = DailyNotesController()

    # Example resident and staff IDs
    resident_id = 101
    staff_id = 5
    date = "2025-10-05"

    print("=== Creating Daily Notes ===")
    note1 = controller.add_daily_note(resident_id, staff_id, date, "Patient feeling better today.")
    note2 = controller.add_daily_note(resident_id, staff_id, date, "Administered morning medication.")

    print("Created Notes:")
    for note in controller.view_resident_notes(resident_id):
        print(f"{note.id}: {note.note_content}")

    print("\n=== Updating a Note ===")
    controller.edit_note(note1.id, "Patient showing full recovery signs.")
    print("Notes after update:")
    for note in controller.view_resident_notes(resident_id):
        print(f"{note.id}: {note.note_content}")

    print("\n=== Deleting a Note ===")
    controller.remove_note(note2.id)
    print("Notes after deletion:")
    for note in controller.view_resident_notes(resident_id):
        print(f"{note.id}: {note.note_content}")

if __name__ == "__main__":
    main()
