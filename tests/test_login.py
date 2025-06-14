import pytest
from selenium.common import NoSuchElementException, NoAlertPresentException

from pages.login_page import LoginPage
from utils import config
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

@pytest.mark.high
def test_valid_login(browser):
    login = LoginPage(browser)
    login.open(config.BASE_URL)
    login.login(username= config.USERNAME, password= config.PASSWORD)
    button = browser.find_element(By.XPATH, "//button[@id='logout']/following-sibling::h2")
    button_text = button.text
    assert button_text == 'Patients', f"Expected 'Patients' but got '{button_text}'"


@pytest.mark.medium
def test_invalid_login_with_only_username(browser):
    login = LoginPage(browser)
    login.open(config.BASE_URL)
    login.login(username = "invalid")
    try:
        alert = Alert(browser)
        alert_text = alert.text
        assert "Invalid login" in alert_text, f"Unexpected alert text: {alert_text}"
        alert.accept()  # Click OK
    except NoAlertPresentException:
        assert False, "Expected alert not found after invalid login"


@pytest.mark.medium
def test_invalid_login_with_wrong_username_password(browser):
    login = LoginPage(browser)
    login.open(config.BASE_URL)
    login.login(username="invalid", password="invalid")
    try:
        alert = Alert(browser)
        alert_text = alert.text
        assert "Invalid login" in alert_text, f"Unexpected alert text: {alert_text}"
        alert.accept()  # Click OK
    except NoAlertPresentException:
        assert False, "Expected alert not found after invalid login"
