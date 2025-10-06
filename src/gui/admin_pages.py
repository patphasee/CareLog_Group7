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
            ["Patient Logs", "Manage Staff", "Staff Assignments"]
        )

        if page == "Patient Logs":
            st.subheader("Patient Logs")
            st.info("Feature not implemented yet.")
        elif page == "Manage Staff":
            st.subheader("Manage Staff")
            st.info("Feature not implemented yet.")
        elif page == "Staff Assignments":
            show_staff_assignments_page(manager)

    elif password != "":
        st.sidebar.warning("Wrong password. Please try again.")
        st.session_state.admin_authenticated = False
