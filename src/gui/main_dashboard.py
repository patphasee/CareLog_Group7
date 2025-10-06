# gui/main_dashboard.py
import streamlit as st
from app.manager import Manager
from gui.medstaff_pages import show_medstaff_page
from gui.patient_pages import show_patient_page
from gui.admin_pages import show_admin_page

def launch():
    """Sets up the main Streamlit application window and navigation."""
    st.set_page_config(layout="wide", page_title="CareLog")

    # Instantiate the "brain" of our app ONCE and store it in the session state.
    # This is crucial so the manager object persists as we switch pages.
    if 'manager' not in st.session_state:
        st.session_state.manager = Manager()

    st.sidebar.title("Carelog Navigation")
    # Create a radio button menu in the sidebar for page navigation.
    page = st.sidebar.radio("Go to", ["Patient View", "Staff View", "Admin View"])

    # Use an if/elif block to call the correct function to render the selected page.
    if page == "Patient View":
        show_patient_page(st.session_state.manager)
    elif page == "Staff View":
        show_medstaff_page(st.session_state.manager)
    elif page == "Admin View":
        show_admin_page(st.session_state.manager)