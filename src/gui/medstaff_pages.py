import streamlit as st
from gui.daily_notes_page import show_daily_notes_page
from gui.appointment_page import show_appointment_page

def show_medstaff_page(manager):
    """Renders all components for the medstaff (staff) page."""
    st.header("Hospital Staff")

    # Find patient
    st.subheader("Find a Patient")
    with st.form("find_form"):
        patient_id = st.text_input("Patient ID")
        submitted = st.form_submit_button("Search")

        if submitted:
            try:
                patient_id = int(patient_id)
                found = manager.find_patient_by_id(patient_id)
                if found:
                    st.success(f"Patient {patient_id}: {found}")
                else:
                    st.error("Could not find patient. Double check entered ID.")
            except ValueError:
                st.warning("Please enter a valid numeric patient ID.")

    st.divider()

    # Add patient
    st.subheader("Add New Patient")
    st.write("Register a new patient into the system.")
    with st.form("add_patient_form"):
        name = st.text_input("Full Name")
        dob = st.text_input("Date of Birth (e.g., 2000-05-16)")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        allergies = st.text_area("Allergies (comma-separated)")
        contact_name = st.text_input("Emergency Contact Name")
        contact_number = st.text_input("Emergency Contact Number")
        password = st.text_input("Set Patient Password", type="password")
        submitted_add = st.form_submit_button("Add Patient")

        if submitted_add:
            if name.strip():
                new_patient = manager.add_new_patient(
                    name=name.strip(),
                    dob=dob.strip(),
                    gender=gender,
                    allergies=[a.strip() for a in allergies.split(",") if a.strip()],
                    contact={"name": contact_name.strip(), "contact": contact_number.strip()},
                    password=password.strip()
                )
                st.success(f"Added new patient: {new_patient.name} (ID {new_patient.id})")
            else:
                st.warning("Please enter a patient name.")

    st.divider()

    # Daily Notes
    show_daily_notes_page(manager)

    st.divider()

    # Appointments 
 
    st.subheader("Appointments")
    st.write("View, schedule, or manage patient appointments.")
    show_appointment_page(manager, user_type="staff", user_id=None)