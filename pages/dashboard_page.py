from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.table = (By.TAG_NAME, "table")

    def is_loaded(self):
        return self.driver.find_element(*self.table).is_displayed()
