

from pages.login_page import LoginPage
from pages.leave_page import LeavePage
from utils import config
import time

def test_apply_leave(setup):
    driver = setup
    login = LoginPage(driver)
    leave = LeavePage(driver)

    
    login.login(config.CREDENTIALS["username"], config.CREDENTIALS["password"])

    leave.open_leave_form()
    leave.select_leave_type("Casual Leave")
    leave.select_leave_date("2025-08-10")
    leave.submit_request()

 
    assert "Leave request submitted" in driver.page_source
    time.sleep(2) 
