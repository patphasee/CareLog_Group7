import json
import datetime
from app.patient import Patient
from app.medstaff import MedStaff
<<<<<<< HEAD
=======
from app.admin import Admin
from app.daily_notes.models.daily_note import DailyNote
>>>>>>> 288e8346723b88158cc48b23289095d5701f4333

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
        self.patients.append(new_patient)
        self.next_patient_id += 1
        print(f"Patient '{name}' added.")
        self._save_data()
        return name
    
    def getName(self, patient_id):
        """Returns the name of a patient given their ID."""
        for patient in self.patients:
            if patient['id'] == int(patient_id):
                return patient['name']
        return None
    
    def update_patient(self, patient_id,name, dob, gender, contact, notes, assigned_staff_ids):
        """Updates an existing patient's details."""
        for patient in self.patients:
            if patient['id'] == int(patient_id):
                patient['name'] = name
                patient['dob'] = dob
                patient['gender'] = gender
                patient['contact'] = contact
                patient['notes'] = notes
                patient['assigned_staff_ids'] = assigned_staff_ids
                print(f"Patient information for patient {patient_id} updated.")
                self._save_data()
                return True
            else:
                print(f"Patient with ID {patient_id} not found.")
                return False
    
    def updateCondition(self, patient_id, allergies, preferences):
        """Updates the condition of a patient."""
        for patient in self.patients:
            if patient['id'] == int(patient_id):
                patient['allergies'] = allergies
                patient['preferences'] = preferences
                print(f"Patient condition for patient {patient_id} updated.")
                self._save_data()
                return True
            else:
                print(f"Patient with ID {patient_id} not found.")
                return False
    def add_medstaff(self, name, speciality):
        """Adds a medical staff dictionary to the data store."""
        medstaff_id = self.next_medstaff_id
        new_medstaff = {
                "id": medstaff_id, 
                "name": name, 
                "speciality": speciality
                }
        self.medstaff.append(new_medstaff)
        self.next_medstaff_id += 1
        print(f"Medical Staff '{name}' added.")
        self._save_data()
        return name
    
    def update_medstaff(self, medstaff_id, name, speciality):
        """Updates an existing medical staff's details."""
        for medstaff in self.medstaff:
            if medstaff['id'] == int(medstaff_id):
                medstaff['name'] = name
                medstaff['speciality'] = speciality
                print(f"Medical Staff information for staff {medstaff_id} updated.")
                self._save_data()
                return True
            else:
                print(f"Medical Staff with ID {medstaff_id} not found.")
                return False
    
    def is_available(self, medstaff_id, date):
        """Checks if a medical staff member is available on a given date."""
        for medstaff in self.medstaff:
            if medstaff['id'] == int(medstaff_id):
                for course in medstaff.get('courses', []):
                    if course['date'] == date:
                        return False
                return True
            else:
                print(f"Medical Staff with ID {medstaff_id} not found.")
                return False
            
    def get_specialty(self, medstaff_id):
        """Returns the speciality of a medical staff member given their ID."""
        for medstaff in self.medstaff:
            if medstaff['id'] == int(medstaff_id):
                return medstaff['speciality']
        return None
    
    def add_admin(self, name):
        """Adds an admin dictionary to the data store."""
        admin_id = self.next_admin_id
        new_admin = {
                "id": admin_id, 
                "name": name
                }
        self.admin.append(new_admin)
        self.next_admin_id += 1
        print(f"Admin '{name}' added.")
        self._save_data()
        return name

    def update_admin(self, admin_id, name):
        """Updates an existing admin's details."""
        for admin in self.admin:
            if admin['id'] == int(admin_id):
                admin['name'] = name
                print(f"Admin information for admin {admin_id} updated.")
                self._save_data()
                return True
            else:
                print(f"Admin with ID {admin_id} not found.")
                return False

    def delete_patient(self, patient_id):
        """Deletes a patient from the data store."""
        for patient in self.patients:
            if patient['id'] == int(patient_id):
                self.patients.remove(patient)
                print(f"Patient with ID {patient_id} deleted.")
                self._save_data()
                return True
        print(f"Patient with ID {patient_id} not found.")
        return False
    
    def delete_medstaff(self, medstaff_id):
        """Deletes a medical staff member from the data store."""
        for medstaff in self.medstaff:
            if medstaff['id'] == int(medstaff_id):
                self.medstaff.remove(medstaff)
                print(f"Medical Staff with ID {medstaff_id} deleted.")
                self._save_data()
                return True
            else:
                print(f"Medical Staff with ID {medstaff_id} not found.")
                return False
    
    def delete_admin(self, admin_id):
        """Deletes an admin from the data store."""
        for admin in self.admin:
            if admin['id'] == int(admin_id):
                self.admin.remove(admin)
                print(f"Admin with ID {admin_id} deleted.")
                self._save_data()
                return True
            else:
                print(f"Admin with ID {admin_id} not found.")
                return False
            
    