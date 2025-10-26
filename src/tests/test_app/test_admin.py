import pytest
import os
from app.admin import Admin


def test_admin_creation():
    admin = Admin("A001", "Admin User")
    assert admin.id == "A001"
    assert admin.name == "Admin User"