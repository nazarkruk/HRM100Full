from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class PersonalDetailsPage:
    middle_name_text_field = 'personal_txtEmpMiddleName'

    def __init__(self, driver):
        self.driver = driver

    def goto_page(self):
        self.driver.find_element_by_id('menu_pim_viewMyDetails').click()

    def edit_button(self):
        self.driver.find_element_by_id('btnSave').click()

    def setup_middle_name(self,  input_middle_name):
        self.driver.find_element_by_id(self.middle_name_text_field).clear()
        self.driver.find_element_by_id(self.middle_name_text_field).send_keys(input_middle_name)

    def setup_emloyee_id(self, employee_id):
        self.driver.find_element_by_id('personal_txtOtherID').clear()
        self.driver.find_element_by_id('personal_txtOtherID').send_keys(employee_id)

    def setup_other_id(self, other_id):
        self.driver.find_element_by_id('personal_txtOtherID').clear()
        self.driver.find_element_by_id('personal_txtOtherID').send_keys(other_id)

    def setup_emp_mick_name(self, nick_name):
        self.driver.find_element_by_id('personal_txtEmpNickName').clear()
        self.driver.find_element_by_id('personal_txtEmpNickName').send_keys(nick_name)

    def setup_military_status(self, military_status):
        self.driver.find_element_by_id('personal_txtMilitarySer').clear()
        self.driver.find_element_by_id('personal_txtMilitarySer').send_keys(military_status)

    def save_button(self):
        self.driver.find_element_by_id('btnSave').click()

    def get_success_message(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Saved'))

    def set_driver_license_num(self, driver_license_num):
        self.driver.find_element_by_id('personal_txtLicenNo').clear()
        self.driver.find_element_by_id('personal_txtLicenNo').send_keys(driver_license_num)

    def set_sin_number(self, sin_number):
        self.driver.find_element_by_id('personal_txtSINNo').clear()
        self.driver.find_element_by_id('personal_txtSINNo').send_keys(sin_number)

    def set_ssn_number(self, input_ssn):
        self.driver.find_element_by_id('personal_txtNICNo').clear()
        self.driver.find_element_by_id('personal_txtNICNo').send_keys(input_ssn)

    def set_smoker_radio_button(self):
        self.driver.find_element_by_id("personal_chkSmokeFlag").click()

    def set_date_of_birth(self, date_of_birth):
        self.driver.find_element_by_name('personal[DOB]').clear()
        self.driver.find_element_by_name('personal[DOB]').send_keys(date_of_birth)

    def select_marital_status(self, marital_text):
        Select(self.driver.find_element_by_id('personal_cmbMarital')).select_by_visible_text(marital_text)
