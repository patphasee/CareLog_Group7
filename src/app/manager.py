import json
import os
from app.patient import Patient
from app.medstaff import MedStaff
from app.staff_assignments.models.staff_assignment import StaffAssignment

class Manager:
    """The main controller for all business logic and data handling."""
    def __init__(self, data_path=os.path.abspath("src/data/carelog.json")):
        self.data_path = data_path
        print(data_path)
        self.admin = []
        self.patients = []
        self.medstaff = []
        self.appointment = []
        self.record = []
        self.careplan = []
        self.next_patient_id = 1
        self.next_medstaff_id = 1
        self.next_admin_id = 1
        self.next_assignment_id = 1 
        self._load_data()


    def _load_data(self):
        """Loads data from the JSON file and populates the object lists."""
        try:
            with open(self.data_path, 'r') as f:
                data = json.load(f)
                self.admin = data.get("admin", [])
                self.patients = data.get("patients", [])
                self.medstaff = data.get("medstaff", []) 
                self.appointment = data.get("appointment", [])
                self.record = data.get("record", [])
                self.careplan = data.get("careplan", [])
                self.next_admin_id = data.get("next_admin_id")
                self.next_patient_id = data.get("next_patient_id")
                self.next_medstaff_id = data.get("next_medstaff_id")
        except FileNotFoundError:
            print("Data file not found. Starting with a clean state.")

    def _save_data(self):
        """Converts object lists back to dictionaries and saves to JSON."""
        data_to_save = {
            "admin": [dict(a) for a in self.admin],
            "patients": [dict(p) for p in self.patients],
            "medstaff": [dict(m) for m in self.medstaff],
            "appointment": [dict(app) for app in self.appointment],
            "record": [dict(r) for r in self.record],
            "careplan": [dict(c) for c in self.careplan],
            "next_admin_id": self.next_admin_id,
            "next_patient_id": self.next_patient_id,
            "next_medstaff_id": self.next_medstaff_id,
            "next_assignment_id": self.next_assignment_id,
        }
        with open(self.data_path, 'w') as f:
            json.dump(data_to_save, f, indent=4)

    # --- Existing methods ---

    def add_patient(self, name, assigned_staff):
        patient_id = self.next_patient_id
        assigned_staff = [assigned_staff]
        new_patient = {
            "id": patient_id,
            "name": name,
            "assigned_staff_ids": assigned_staff,
        }
        self.patients.append(new_patient)
        self.next_patient_id += 1
        self._save_data()
        return name

    # Assignment persistence helpers

    def add_assignment(self, staff_id, resident_id, date, shift):
        assignment = StaffAssignment(
            self.next_assignment_id, staff_id, resident_id, date, shift
        )
        self.assignments.append(assignment)
        self.next_assignment_id += 1
        self._save_data()
        return assignment

    def get_all_assignments(self):
        return self.assignments

    def update_assignment_shift(self, assignment_id, new_shift):
        for assignment in self.assignments:
            if assignment.id == assignment_id:
                assignment.shift = new_shift
                self._save_data()
                return assignment
        return None

    def delete_assignment(self, assignment_id):
        for assignment in self.assignments:
            if assignment.id == assignment_id:
                self.assignments.remove(assignment)
                self._save_data()
                return True
        return False
