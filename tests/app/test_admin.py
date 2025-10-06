import pytest
from gui.admin_pages import show_admin_page
from app.manager import Manager 
data = Manager()
def test_show_admin_page():
    try:
        show_admin_page(data)
    except Exception as e:
        pytest.fail(f"show_admin_page raised an exception: {e}")
