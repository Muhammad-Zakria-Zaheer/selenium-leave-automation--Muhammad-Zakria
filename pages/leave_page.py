

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class LeavePage:
    def __init__(self, driver):
        self.driver = driver

    def open_leave_form(self):
        self.driver.find_element(By.ID, "applyLeaveBtn").click()

    def select_leave_type(self, leave_type):
        dropdown = Select(self.driver.find_element(By.ID, "leaveType"))
        dropdown.select_by_visible_text(leave_type)

    def select_leave_date(self, date):
        date_input = self.driver.find_element(By.ID, "leaveDate")
        date_input.clear()
        date_input.send_keys(date)

    def submit_request(self):
        self.driver.find_element(By.ID, "submitBtn").click()
