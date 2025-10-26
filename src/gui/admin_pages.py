import streamlit as st
from app.manager import Manager
from gui.staff_assignments_page import show_staff_assignments_page

def show_admin_page(manager):
    st.header("Admin Page")

    password = st.text_input("Enter admin password:", type="password")

    if password == "password":
        st.session_state.admin_authenticated = True
        st.sidebar.success("You are logged in as admin.")

        page = st.sidebar.radio(
            "Navigation",
            ["Patient Logs", "Manage Staff", "Staff Assignments", "System Statistics"]
        )

        if page == "Patient Logs":
            st.subheader("Patient Logs")
            st.info("Feature not implemented yet.")
        elif page == "Manage Staff":
            st.subheader("Manage Staff")
            st.markdown("#### Add Staff")
            st.write("Register a new staff into the system.")
            with st.form("add_staff_form"):
                name = st.text_input("Full Name")
                speciality = st.text_input("Enter Role")
                submitted_add = st.form_submit_button("Add Staff")
            if submitted_add:
                if name.strip():
                    new_staff = manager.add_new_staff(
                        name=name.strip(),
                        speciality=speciality.strip()
                    )
                    st.success(f"Added new staff!")
            else:
                st.warning("Please enter a staff name.")
        elif page == "Staff Assignments":
            show_staff_assignments_page(manager)
        elif page == "System Statistics":
            st.subheader("System Statistics")
            stats = manager.get_system_stats()

            st.metric("Total Patients", stats["total_patients"])
            st.metric("Total Staff", stats["total_medstaff"])
            st.metric("Total Appointments", stats["total_appointments"])
            st.metric("Total Daily Notes", stats["total_daily_notes"])

    elif password != "":
        st.sidebar.warning("Wrong password. Please try again.")
        st.session_state.admin_authenticated = False
