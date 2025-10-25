import pytest
import os
from src.app.admin import Admin

def test_admin_creation():
    admin = Admin("A001", "Admin User", password="adminpass")
    assert admin.id == "A001"
    assert admin.name == "Admin User"
    assert admin.password == "adminpass"