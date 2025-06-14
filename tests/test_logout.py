import pytest
from pages.login_page import LoginPage
from utils import config
from selenium.webdriver.common.by import By

@pytest.mark.low
def test_logout(browser):
    LoginPage(browser).open(config.BASE_URL)
    LoginPage(browser).login(username= config.USERNAME, password= config.PASSWORD)

    # Click logout
    browser.find_element(By.ID, "logout").click()

    assert browser.find_element(By.XPATH, "//button[@type='submit' and text()='Login']").is_displayed()

