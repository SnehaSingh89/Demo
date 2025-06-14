from selenium.webdriver.common.by import By

class AddPatientPage:
    def __init__(self, driver):
        self.driver = driver
        self.fields = {
            "mrn": (By.ID, "mrn"),
            "first_name": (By.ID, "firstName"),
            "last_name": (By.ID, "lastName"),
            "dob": (By.ID, "dob"),
            "discharge": (By.ID, "discharge"),
            "phone": (By.ID, "phone"),
            "language": (By.ID, "language"),
            "timezone": (By.ID, "timezone")
        }
        self.submit_btn = (By.XPATH, "//select[@id='timezone']/following-sibling::button[@type='submit']")

    def fill_form(self, patient_data):
        # Fill MRN
        self.driver.find_element(*self.fields["mrn"]).send_keys(patient_data.get("mrn", ""))

        # Fill First Name
        self.driver.find_element(*self.fields["first_name"]).send_keys(patient_data.get("first_name", ""))

        # Fill Last Name
        self.driver.find_element(*self.fields["last_name"]).send_keys(patient_data.get("last_name", ""))

        # Fill Date of Birth
        self.driver.find_element(*self.fields["dob"]).send_keys(patient_data.get("dob", ""))

        # Fill Discharge Date & Time
        self.driver.find_element(*self.fields["discharge"]).send_keys(patient_data.get("discharge", ""))

        # Fill Phone Number
        self.driver.find_element(*self.fields["phone"]).send_keys(patient_data.get("phone", ""))

        # Select Language (Dropdown)
        self.driver.find_element(*self.fields["language"]).send_keys(patient_data.get("language", ""))

        # Select Timezone (Dropdown)
        self.driver.find_element(*self.fields["timezone"]).send_keys(patient_data.get("timezone", ""))

        # Click Save button
        self.driver.find_element(*self.submit_btn).click()


    def is_patient_present(self, mrn):
        self.patient_table_rows = (By.CSS_SELECTOR, "#patients-table tbody tr")
        rows = self.driver.find_elements(*self.patient_table_rows)

        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            row_data = [col.text.strip() for col in cols]
            if mrn in row_data:
                return True

        return False