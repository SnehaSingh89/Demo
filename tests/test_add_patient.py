import pytest
from pages.login_page import LoginPage
from pages.add_patient_page import AddPatientPage
from utils import config
from selenium.webdriver.common.by import By
import time

@pytest.mark.critical
def test_add_patient(browser):
    LoginPage(browser).open(config.BASE_URL)
    LoginPage(browser).login(username= config.USERNAME, password= config.PASSWORD)

    # Navigate to Add Patient
    browser.find_element(By.XPATH, "//button[text()='Add Patient']").click()
    add_patient_page = AddPatientPage(browser)

    patient_data = {
        "mrn": "MRN12345",
        "first_name": "John",
        "last_name": "Doe",
        "dob": "01/01/1990",
        "discharge": "2025-07-02T20:01",
        "phone": "1234567890",
        "language": "English",
        "timezone": "UTC"
    }

    AddPatientPage(browser).fill_form(patient_data)

    # Wait and assert patient appears
    time.sleep(2)
    assert add_patient_page.is_patient_present("MRN12345"), " Patient with MRN12345 not found in the patient table"


