"""
Author: Pitipat Phasee
Last Modified: 2025-10-05
Version: 1.0

Test for staff_assignents
"""

from app.staff_assignments.controllers.staff_assignments_controller import StaffAssignmentsController

def main():
    controller = StaffAssignmentsController()

    staff_id = 200
    resident_id = 101
    date = "2025-10-05"

    # Create assignments
    a1 = controller.assign_staff(staff_id, resident_id, date, "Morning")
    a2 = controller.assign_staff(staff_id, 102, date, "Night")

    print("Created Assignments:")
    for a in controller.view_staff_assignments(staff_id):
        print(f"{a.id}: Resident {a.resident_id}, Shift: {a.shift}")

    # Update an assignment
    controller.edit_assignment(a1.id, "Afternoon")
    print("\nAssignments after update:")
    for a in controller.view_staff_assignments(staff_id):
        print(f"{a.id}: Resident {a.resident_id}, Shift: {a.shift}")

    # Delete an assignment
    controller.remove_assignment(a2.id)
    print("\nAssignments after deletion:")
    for a in controller.view_staff_assignments(staff_id):
        print(f"{a.id}: Resident {a.resident_id}, Shift: {a.shift}")

if __name__ == "__main__":
    main()
