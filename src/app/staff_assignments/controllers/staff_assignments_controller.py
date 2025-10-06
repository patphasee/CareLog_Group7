"""
Author: Pitipat Phasee
Last Modified: 2025-10-05
Version: 1.0

Staff assignment controller object
"""

from app.staff_assignments.services.staff_assignments_service import StaffAssignmentsService

class StaffAssignmentsController:
    """Controller for Staff Assignments."""

    def __init__(self):
        self.service = StaffAssignmentsService()

    def assign_staff(self, staff_id, resident_id, date, shift):
        return self.service.create_assignment(staff_id, resident_id, date, shift)

    def view_staff_assignments(self, staff_id):
        return self.service.get_assignments_by_staff(staff_id)

    def view_resident_assignments(self, resident_id):
        return self.service.get_assignments_by_resident(resident_id)

    def edit_assignment(self, assignment_id, new_shift):
        return self.service.update_assignment(assignment_id, new_shift)

    def remove_assignment(self, assignment_id):
        return self.service.delete_assignment(assignment_id)
