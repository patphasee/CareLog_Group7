import pytest
import os
import datetime
from src.app.patient import Patient

def test_patient_defaults():
    p = Patient("P001", "Alia")
    assert p.id == "P001"
    assert p.name == "Alia"
    assert p.dob is None
    assert p.allergies == []
    assert p.preferences == ""
    assert p.current_patient is True
    assert p.password == "password"


def test_patient_custom_values():
    p = Patient("P002", "Casey", dob=datetime.date(2000, 1, 1), gender="Male", password="1234")
    assert p.dob == datetime.date(2000, 1, 1)
    assert p.gender == "Male"
    assert p.password == "1234"


def test_patient_allergy_add():
    p = Patient("P003", "Alex")
    p.allergies.append("peanuts")
    assert "peanuts" in p.allergies