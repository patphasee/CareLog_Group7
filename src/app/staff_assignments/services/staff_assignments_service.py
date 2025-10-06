"""
Author: Pitipat Phasee
Last Modified: 2025-10-05
Version: 1.0

Staff assignment data object
"""

from app.staff_assignments.models.staff_assignment import StaffAssignment

class StaffAssignmentsService:
    """Service for managing staff assignments (persistent version)."""

    def __init__(self, manager):
        self.manager = manager  # now relies on Manager’s storage

    def create_assignment(self, staff_id, resident_id, date, shift):
        return self.manager.add_assignment(staff_id, resident_id, date, shift)

    def get_assignments_by_staff(self, staff_id):
        return [a for a in self.manager.get_all_assignments() if a.staff_id == staff_id]

    def get_assignments_by_resident(self, resident_id):
        return [a for a in self.manager.get_all_assignments() if a.resident_id == resident_id]

    def update_assignment(self, assignment_id, new_shift):
        return self.manager.update_assignment_shift(assignment_id, new_shift)

    def delete_assignment(self, assignment_id):
        return self.manager.delete_assignment(assignment_id)
