import json
import datetime
from app.patient import Patient
from app.medstaff import MedStaff

class Manager:
    """The main controller for all business logic and data handling."""
    def __init__(self, data_path="src\data\carelog.json"): 
        self.data_path = data_path
        self.admin = []
        self.patients = []
        self.medstaff = []
        self.next_patient_id = 1
        self.next_medstaff_id = 1
        self.next_admin_id = 1
        self._load_data()

    def _load_data(self):
        """Loads data from the JSON file and populates the object lists."""
        try:
            with open(self.data_path, 'r') as f:
                data = json.load(f)
                self.admin = data.get("admin", [])
                self.patients = data.get("patients", [])
                self.medstaff = data.get("medstaff", []) 
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
            "next_admin_id": self.next_admin_id,
            "next_patient_id": self.next_patient_id,
            "next_medstaff_id": self.next_medstaff_id
        }
        with open(self.data_path, 'w') as f:
            json.dump(data_to_save, f, indent=4)

    def find_patient_by_id(self, patient_id): 
        """A new helper to find one student by their exact ID."""
        for patient in self.patients:
            if patient['id'] == int(patient_id):
                return patient['name']
    
    def add_patient(self, name, assigned_staff):
        """Adds a patient dictionary to the data store."""
        patient_id = self.next_patient_id
        assigned_staff = [assigned_staff]
        new_patient = {
            "id": patient_id, 
            "name": name, 
            "assigned_staff_ids": assigned_staff
            }
        self.students.append(new_patient)
        self.next_patient_id += 1
        print(f"Patient '{name}' added.")
        self._save_data()
        return name
    
