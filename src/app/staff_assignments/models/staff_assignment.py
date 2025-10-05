"""
Author: Pitipat Phasee
Last Modified: 2025-10-05
Version: 1.0

Staff assignment data object
"""

class StaffAssignment:
    """Data model for a staff assignment."""

    def __init__(self, id, staff_id, resident_id, date, shift):
        """
        Initialize a StaffAssignment object.

        Args:
            id (int): Unique assignment ID
            staff_id (int): ID of the staff member
            resident_id (int): ID of the resident assigned
            date (str): Date of the assignment (YYYY-MM-DD)
            shift (str): Shift type (e.g., 'Morning', 'Afternoon', 'Night')
        """
        self.id = id
        self.staff_id = staff_id
        self.resident_id = resident_id
        self.date = date
        self.shift = shift
