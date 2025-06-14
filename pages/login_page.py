from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def open(self, url):
        self.driver.get(url)

    def login(self, **kwargs):
        self.driver.find_element(*self.username_input).send_keys(kwargs.get("username",""))
        self.driver.find_element(*self.password_input).send_keys(kwargs.get("password",""))
        self.driver.find_element(*self.login_button).click()
