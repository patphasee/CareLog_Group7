import streamlit as st
from app.manager import Manager
def show_patient_page(manager):
    st.header("Patient Page")

    user = st.text_input("Enter patient ID:")
    password = st.text_input("Enter patient password:", type="password")

    r = None
    for r in manager.patients:
        if user != "":
            if int(user) == r["id"]:
                specific_user = r
    if r is None:
        password = "INVALID"

    if password == "password":
        st.session_state.admin_authenticated = True
        st.sidebar.success(f"You are logged in as {user}.")

        page = st.sidebar.radio(
            "Navigation",
            ["Patient Info", "Edit Info", "Add Notes"]
        )

        if page == "Patient Info":
            st.subheader("Patient Info")
            st.info(f"Name: {specific_user["name"]}  \n  DOB: {specific_user["dob"]}  \n  Gender: {specific_user["gender"]}")
        elif page == "Edit Info":
            st.subheader("Edit Info")
            st.info("Feature not implemented yet.")
        elif page == "Add Notes":
            st.subheader("Add Notes")
            st.info("Feature not implemented yet.")

    elif password != "":
        st.sidebar.warning("Wrong password. Please try again.")
        st.session_state.admin_authenticated = False