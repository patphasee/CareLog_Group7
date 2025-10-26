import streamlit as st
from datetime import datetime, timedelta

def show_appointment_page(manager, user_type="staff", user_id=None):
    """
    Displays appointment management page for patients or staff.
    user_type: "patient" or "staff"
    user_id:   ID of the logged-in user (optional for staff)
    """
    st.header("Appointments")


    # Helper function to get attribute from object or dict

    def get_attr(a, key, default=None):
        if isinstance(a, dict):
            return a.get(key, default)
        return getattr(a, key, default)


    # Filter appointments for this user

    if user_type == "patient":
        user_appointments = [a for a in manager.appointment if get_attr(a, "patient_id") == user_id]
    else:
        if user_id:
            user_appointments = [a for a in manager.appointment if get_attr(a, "staff_id") == user_id]
        else:
            user_appointments = manager.appointment

    # Upcoming appointments
 
    upcoming = [a for a in user_appointments if get_attr(a, "status") == "Scheduled"]
    if upcoming:
        st.info(f"You have {len(upcoming)} upcoming appointment(s):")
        for app in upcoming:
            date_str = get_attr(app, "date") or "Unknown"
            time_str = get_attr(app, "time") or "Unknown"
            purpose_str = get_attr(app, "purpose") or "No notes"
            status_str = get_attr(app, "status") or "Unknown"
            st.write(f"- {date_str} at {time_str} | {purpose_str} ({status_str})")
    else:
        st.info("No upcoming appointments.")

    st.markdown("---")
    # Add New Appointment

    st.subheader("Create New Appointment")
    with st.form("add_appointment_form"):
        date_input_val = st.date_input("Date", value=datetime.now().date() + timedelta(days=1))
        time_input_val = st.time_input("Time", value=datetime.now().time())
        purpose_input_val = st.text_input("Purpose / Notes")

        # -Staff selection
        if hasattr(manager, "medstaff") and manager.medstaff:
            staff_options = {
                f"{s['name']} ({s.get('speciality', 'N/A')}) [ID: {s['id']}]": s['id']
                for s in manager.medstaff
            }
            selected_staff_label = st.selectbox("Select Staff for Appointment", list(staff_options.keys()))
            staff_id = staff_options[selected_staff_label]
        else:
            st.warning("No staff found in the system.")
            staff_id = None

        # Patient ID
        if user_type == "staff":
            patient_id = st.number_input("Patient ID", min_value=1, step=1)
        else:
            patient_id = user_id

        submitted = st.form_submit_button("Schedule Appointment")

        if submitted:
            if not staff_id:
                st.error("Please select a valid staff member.")
            else:
                new_app = manager.add_appointment(
                    patient_id=patient_id,
                    staff_id=staff_id,
                    date=str(date_input_val),
                    time=str(time_input_val)[:5],
                    purpose=purpose_input_val.strip()
                )
                # Show success safely
                date_str = get_attr(new_app, "date", "Unknown")
                time_str = get_attr(new_app, "time", "Unknown")
                st.success(f"Appointment scheduled on {date_str} at {time_str}")

    st.markdown("---")


    # Manage Existing Appointments

    st.subheader("Manage Appointments")
    if not user_appointments:
        st.info("No appointments to manage.")
    else:
        # Sort safely by date and time
        def sort_key(a):
            date_val = get_attr(a, "date") or "9999-12-31"
            time_val = get_attr(a, "time") or "23:59"
            return (date_val, time_val)

        for app in sorted(user_appointments, key=sort_key):
            date_str = get_attr(app, "date") or "Unknown"
            time_str = get_attr(app, "time") or "Unknown"
            purpose_str = get_attr(app, "purpose") or "No notes"
            status_str = get_attr(app, "status") or "Unknown"

            with st.expander(f"{date_str} at {time_str} — {purpose_str} ({status_str})"):
                st.write(f"Patient ID: {get_attr(app,'patient_id')}")
                st.write(f"Staff ID: {get_attr(app,'staff_id')}")
                st.write(f"Status: {status_str}")

                col1, col2 = st.columns(2)

                # Cancel appointment
                if col1.button(f"Cancel #{get_attr(app,'id')}"):
                    manager.cancel_appointment(get_attr(app,'id'))
                    st.warning("Appointment cancelled.")
                    st.rerun()

                # Reschedule appointment
                with col2.form(f"reschedule_form_{get_attr(app,'id')}"):
                    # Safe defaults for reschedule
                    app_date_str = get_attr(app, 'date') or datetime.now().strftime("%Y-%m-%d")
                    app_time_str = get_attr(app, 'time') or "09:00"

                    # Convert to proper types for Streamlit input
                    try:
                        new_date = st.date_input("New Date", value=datetime.strptime(app_date_str, "%Y-%m-%d").date())
                    except ValueError:
                        new_date = st.date_input("New Date", value=datetime.now().date())
                    try:
                        new_time = st.time_input("New Time", value=datetime.strptime(app_time_str, "%H:%M").time())
                    except ValueError:
                        new_time = st.time_input("New Time", value=datetime.strptime("09:00", "%H:%M").time())

                    resubmit = st.form_submit_button("Reschedule")
                    if resubmit:
                        if isinstance(app, dict):
                            app['date'] = str(new_date)
                            app['time'] = str(new_time)[:5]
                        else:
                            app.date = str(new_date)
                            app.time = str(new_time)[:5]
                        manager._save_data()
                        st.success("Appointment rescheduled.")
                        st.rerun()
