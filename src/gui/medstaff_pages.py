
import streamlit as st

def show_medstaff_page(manager):
    """Renders all components for the medstaff page."""
    st.header("Hospital Staff")

    # --- Search Section (remains the same) ---
    st.subheader("Find a Patient")
    with st.form("find_form"):
        student_id = st.text_input("Patient ID")
        submitted = st.form_submit_button("Search")
        
        if submitted:
            try:
                patient_id = int(patient_id)
            except ValueError:
                patient_id = False
            if patient_id:
                find_patient = manager.find_patient_by_id(patient_id)
                if find_patient:
                    st.success(f"Patient {patient_id}: {find_patient}")
                else:
                    st.error("Could not find patient. Double check entered ID.")
            else:
                st.warning("Please enter a patient ID.")