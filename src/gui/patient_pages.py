import streamlit as st
from datetime import datetime
from app.manager import Manager
from gui.appointment_page import show_appointment_page

def show_patient_page(manager):
    st.header("Patient Page")

    # Login Section 
    user = st.text_input("Enter patient ID:")
    password = st.text_input("Enter patient password:", type="password")

    specific_user = None

    # Try to find matching patient
    if user.strip():
        try:
            uid = int(user)
            for patient in manager.patients:
                if patient["id"] == uid:
                    specific_user = patient
                    break
        except ValueError:
            st.warning("Please enter a valid numeric patient ID.")

    # If login successful
    if specific_user and password == specific_user.get("password"):
        st.session_state.patient_authenticated = True
        st.sidebar.success(f"You are logged in as {specific_user['name']}")

        page = st.sidebar.radio(
            "Navigation",
            ["Patient Info", "Edit Info", "Daily Notes", "Appointments"]
        )

        # Patient Info
        if page == "Patient Info":
            st.subheader("Patient Info")
            st.info(
                f"**Name:** {specific_user.get('name', 'N/A')}  \n"
                f"**DOB:** {specific_user.get('dob', 'N/A')}  \n"
                f"**Gender:** {specific_user.get('gender', 'N/A')}  \n"
                f"**Allergies:** {', '.join(specific_user.get('allergies', [])) or 'None'}  \n"
                f"**Emergency Contact:** {specific_user.get('contact', {}).get('name', 'N/A')} - {specific_user.get('contact', {}).get('contact', 'N/A')}"
            )

        # Edit Info
        elif page == "Edit Info":
            st.subheader("Edit Your Information")
            with st.form("edit_patient_info_form"):
                name = st.text_input("Full Name", value=specific_user.get("name", ""))
                dob = st.text_input("Date of Birth", value=specific_user.get("dob", ""))
                gender = st.selectbox("Gender", ["Male", "Female", "Other"], 
                                      index=["Male", "Female", "Other"].index(specific_user.get("gender", "Other")))
                allergies = st.text_area("Allergies (comma-separated)", 
                                         value=", ".join(specific_user.get("allergies", [])))
                contact_name = st.text_input("Emergency Contact Name", 
                                             value=specific_user.get("contact", {}).get("name", ""))
                contact_number = st.text_input("Emergency Contact Number", 
                                               value=specific_user.get("contact", {}).get("contact", ""))
                new_password = st.text_input("Set New Password", type="password")

                submitted = st.form_submit_button("Save Changes")

                if submitted:
                    specific_user["name"] = name.strip()
                    specific_user["dob"] = dob.strip()
                    specific_user["gender"] = gender
                    specific_user["allergies"] = [a.strip() for a in allergies.split(",") if a.strip()]
                    specific_user["contact"] = {"name": contact_name.strip(), "contact": contact_number.strip()}
                    if new_password.strip():
                        specific_user["password"] = new_password.strip()

                    manager._save_data()
                    st.success(" Your information has been updated successfully!")

# Appointments 

        elif page == "Appointments":
            show_appointment_page(manager, user_type="patient", user_id=specific_user["id"])

        # Daily Notes 
        elif page == "Daily Notes":
            st.subheader("Your Daily Notes")

            # Add a new note 
            with st.form("add_patient_note_form"):
                note_text = st.text_area("Write your note below:")
                submitted = st.form_submit_button("Add Note")

                if submitted and note_text.strip():
                    manager.add_daily_note(
                        staff_id=None,  # None = patient-submitted note
                        resident_id=specific_user["id"],
                        note=note_text.strip(),
                        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M")
                    )
                    st.success("Note added successfully!")

            # View all notes for this patient
            st.markdown("---")
            st.subheader("All Notes")

            patient_notes = [
                n for n in manager.daily_notes
                if n.resident_id == specific_user["id"]
            ]

            if patient_notes:
                for note in sorted(patient_notes, key=lambda n: n.timestamp, reverse=True):
                    author = f"Staff #{note.staff_id}" if note.staff_id else "You (Patient)"
                    st.markdown(
                        f"**{author}** — {note.timestamp}  \n"
                        f"{note.note}"
                    )
                    st.markdown("---")
            else:
                st.info("No notes available yet.")

    # Invalid login
    elif password != "":
        st.sidebar.warning("Wrong password or patient ID. Please try again.")
        st.session_state.patient_authenticated = False
