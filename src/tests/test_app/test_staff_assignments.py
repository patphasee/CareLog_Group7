import pytest 
import os
from app.staff_assignments.models.staff_assignment import StaffAssignment
from app.staff_assignments.services.staff_assignments_service import StaffAssignmentsService
from app.staff_assignments.controllers.staff_assignments_controller import StaffAssignmentsController


def test_staff_assignment_basic():
    a = StaffAssignment(
        id=1,
        staff_id=10,
        resident_id=20,
        date="2025-10-20",
        shift="Morning"
    )
    assert a.id == 1
    assert a.staff_id == 10
    assert a.resident_id == 20
    assert a.date == "2025-10-20"
    assert a.shift == "Morning"

# create a fake manager to avoid saving data to files during tests
class FakeManager1:
    def __init__(self):
        self.assignments = []
        self.next_id = 1

    def add_assignment(self, staff_id, resident_id, date, shift):
        a = StaffAssignment(self.next_id, staff_id, resident_id, date, shift)
        self.assignments.append(a)
        self.next_id += 1
        return a

    def get_all_assignments(self):
        return self.assignments

def test_service_create_and_retrieve():
    manager = FakeManager1()
    service = StaffAssignmentsService(manager)

    a = service.create_assignment(10, 20, "2025-10-20", "Night")
    assert a.id == 1
    assert a.shift == "Night"

    results = service.get_assignments_by_staff(10)
    assert len(results) == 1
    assert results[0].resident_id == 20