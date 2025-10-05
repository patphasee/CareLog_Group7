import streamlit as st
from app.manager import Manager
def show_admin_page(manager):
    st.header("Admin Page")
    password = st.text_input("Enter admin password:", type="password")
    if password == "password":  # Example password check
        st.session_state.admin_authenticated = True
        st.sidebar.success("You are logged in as admin.")
        #  View patient logs
        data = Manager()
        st.dataframe(data)
        page = st.sidebar.radio("Navigation", ["Patient Logs", "Manage Staff"])
        if page == "Patient Logs":
            st.header("Patient Logs")
            st.sidebar.title("Patient Logs")
        elif page == "Manage Staff":
            st.header("Manage Staff")
            st.sidebar.title("Manage Staff")
    elif password != "":
        st.sidebar.warning("Wrong password. Please try again.")
        st.session_state.admin_authenticated = False
    
        
    
        



show_admin_page(None)
