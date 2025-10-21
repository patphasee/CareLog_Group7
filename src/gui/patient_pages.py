import streamlit as st
from app.manager import Manager

def show_patient_page(manager):
    st.header("Patient Page")

    # Patient Login
    user = st.text_input("Enter patient ID:")
    password = st.text_input("Enter patient password:", type="password")

    specific_user = None

    # Find the matching patient by ID
    if user.strip():
        try:
            uid = int(user)
            for patient in manager.patients:
                if patient["id"] == uid:
                    specific_user = patient
                    break
        except ValueError:
            st.warning("Please enter a valid numeric patient ID.")

    # Login verification 
    if specific_user and password == specific_user.get("password"):
        st.session_state.patient_authenticated = True
        st.sidebar.success(f"You are logged in as {specific_user['name']}")

        page = st.sidebar.radio(
            "Navigation",
            ["Patient Info", "Edit Info", "Add Notes"]
        )

        if page == "Patient Info":
            st.subheader("Patient Info")
            st.info(
                f"**Name:** {specific_user.get('name', 'N/A')}  \n"
                f"**DOB:** {specific_user.get('dob', 'N/A')}  \n"
                f"**Gender:** {specific_user.get('gender', 'N/A')}"
            )

        elif page == "Edit Info":
            st.subheader("Edit Info")
            st.info("Feature not implemented yet.")

        elif page == "Add Notes":
            st.subheader("Add Notes")
            st.info("Feature not implemented yet.")

    elif password != "":
        st.sidebar.warning("Wrong password or patient ID. Please try again.")
        st.session_state.patient_authenticated = False
