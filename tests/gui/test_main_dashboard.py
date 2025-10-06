from gui.main_dashboard import show_main_dashboard
def test_show_main_dashboard():
    try:
        show_main_dashboard()
    except Exception as e:
        pytest.fail(f"show_main_dashboard raised an exception: {e}")
