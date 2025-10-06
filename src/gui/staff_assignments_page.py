"""
Author: Pitipat Phasee
Last Modified: 2025-10-06
Version: 1.0

Streamlit interface for staff assignment management
"""

import streamlit as st
from app.staff_assignments.controllers.staff_assignments_controller import StaffAssignmentsController

def show_staff_assignments_page(manager):
    """Display and manage staff assignments from the admin view."""
    controller = StaffAssignmentsController(manager)
    st.header(" Staff Assignments")

    # Create new assignment 
    st.subheader("Assign Staff to Resident")

    if not manager.medstaff or not manager.patients:
        st.warning("No staff or residents found. Please add them first.")
        return

    staff_options = {f"{s['name']} (ID {s['id']})": s["id"] for s in manager.medstaff}
    resident_options = {f"{r['name']} (ID {r['id']})": r["id"] for r in manager.patients}

    staff_selection = st.selectbox("Select Staff", list(staff_options.keys()))
    resident_selection = st.selectbox("Select Resident", list(resident_options.keys()))
    date = st.date_input("Assignment Date")
    shift = st.selectbox("Shift", ["Morning", "Afternoon", "Night"])

    if st.button("Assign"):
        new_assignment = controller.assign_staff(
            staff_id=staff_options[staff_selection],
            resident_id=resident_options[resident_selection],
            date=str(date),
            shift=shift
        )
        st.success(f" Assigned {staff_selection} to {resident_selection} for {shift} shift on {date}")
        st.session_state.last_assignment = new_assignment

    # View Assignments
    st.divider()
    st.subheader("View Existing Assignments")
    if st.button("🔄 Refresh Assignments"):
        all_assignments = controller.service.assignments
        if all_assignments:
            st.dataframe(
                [
                    {
                        "Assignment ID": a.id,
                        "Staff ID": a.staff_id,
                        "Resident ID": a.resident_id,
                        "Date": a.date,
                        "Shift": a.shift,
                    }
                    for a in all_assignments
                ]
            )
        else:
            st.info("No assignments found yet.")
