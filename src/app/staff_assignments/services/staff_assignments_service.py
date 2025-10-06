"""
Author: Pitipat Phasee
Last Modified: 2025-10-05
Version: 1.0

Service object for staff_assignments
"""

from app.staff_assignments.models.staff_assignment import StaffAssignment

class StaffAssignmentsService:
    """Service for managing staff assignments."""

    def __init__(self):
        self.assignments = []
        self.next_id = 1

    def create_assignment(self, staff_id, resident_id, date, shift):
        assignment = StaffAssignment(self.next_id, staff_id, resident_id, date, shift)
        self.assignments.append(assignment)
        self.next_id += 1
        return assignment

    def get_assignments_by_staff(self, staff_id):
        return [a for a in self.assignments if a.staff_id == staff_id]

    def get_assignments_by_resident(self, resident_id):
        return [a for a in self.assignments if a.resident_id == resident_id]

    def update_assignment(self, assignment_id, new_shift):
        for assignment in self.assignments:
            if assignment.id == assignment_id:
                assignment.shift = new_shift
                return assignment
        return None

    def delete_assignment(self, assignment_id):
        for assignment in self.assignments:
            if assignment.id == assignment_id:
                self.assignments.remove(assignment)
                return True
        return False
