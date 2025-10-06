"""
Author: Pitipat Phasee
Last Modified: 2025-10-06
Version: 1.0

Streamlit interface for Daily Notes (Staff View)
"""

import streamlit as st
from app.daily_notes.controllers.daily_notes_controller import DailyNotesController

def show_daily_notes_page(manager):
    controller = DailyNotesController(manager)
    st.header("Daily Notes")

    # Add a new note
    st.subheader("Add New Note")

    if not manager.medstaff or not manager.patients:
        st.warning("Please ensure staff and patients are added first.")
        return

    staff_options = {s["name"]: s["id"] for s in manager.medstaff}
    resident_options = {p["name"]: p["id"] for p in manager.patients}

    staff_name = st.selectbox("Staff Member", list(staff_options.keys()))
    resident_name = st.selectbox("Resident", list(resident_options.keys()))
    note_text = st.text_area("Enter Note")

    if st.button("Save Note"):
        new_note = controller.add_note(
            staff_options[staff_name],
            resident_options[resident_name],
            note_text
        )
        st.success(f"Note saved by {staff_name} for {resident_name} at {new_note.timestamp}")

    st.divider()

    # View Notes
    st.subheader("View Notes")
    view_mode = st.radio("Filter by", ["All Notes", "By Staff", "By Resident"])

    if view_mode == "All Notes":
        notes = controller.view_all_notes()
    elif view_mode == "By Staff":
        name = st.selectbox("Select Staff", list(staff_options.keys()))
        notes = controller.view_notes_by_staff(staff_options[name])
    else:
        name = st.selectbox("Select Resident", list(resident_options.keys()))
        notes = controller.view_notes_by_resident(resident_options[name])

    if notes:
        st.dataframe(
            [
                {
                    "Note ID": n.id,
                    "Staff ID": n.staff_id,
                    "Resident ID": n.resident_id,
                    "Note": n.note,
                    "Timestamp": n.timestamp,
                }
                for n in notes
            ]
        )
    else:
        st.info("No notes available for this selection.")
