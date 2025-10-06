import streamlit as st
from gui.daily_notes_page import show_daily_notes_page

def show_medstaff_page(manager):
    """Renders all components for the medstaff page."""
    st.header("Hospital Staff")

    # Patient Search Section
    st.subheader("Find a Patient")
    with st.form("find_form"):
        patient_id = st.text_input("Patient ID")
        submitted = st.form_submit_button("Search")
        
        if submitted:
            try:
                patient_id = int(patient_id)
                find_patient = manager.find_patient_by_id(patient_id)
                if find_patient:
                    st.success(f"Patient {patient_id}: {find_patient}")
                else:
                    st.error("Could not find patient. Double check entered ID.")
            except ValueError:
                st.warning("Please enter a valid numeric patient ID.")

    st.divider()

    # Daily Notes Section
    st.subheader("Daily Notes")
    st.write("Record and review notes for patients.")
    show_daily_notes_page(manager)
