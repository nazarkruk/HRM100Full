import unittest

import HtmlTestRunner
from selenium import webdriver
from fixtures.params import DOMAIN, CHROME_EXECUTABLE_PATH
from pages.login_page import LoginPage
from pages.personal_details_page import PersonalDetailsPage


class PersonalDetailsTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_EXECUTABLE_PATH)
        self.driver.get(DOMAIN)
        self.login_page = LoginPage(self.driver)
        self.personal_details_page = PersonalDetailsPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_01_see_personal_details(self):
        driver = self.driver
        self.login_page.login()
        self.login_page.get_welcome_massage()
        self.personal_details_page.goto_page()

        self.assertEqual("Personal Details", driver.find_element_by_xpath("//*[@id='pdMainContainer']/div[1]/h1").text)

    def test_02_edit_personal_details(self):
        driver = self.driver
        input_middle_name = 'Richard'
        employee_id = '101010'
        other_id = '033303'
        nick_name = 'Rick'
        military_status = 'N/A'

        self.login_page.login()
        self.login_page.get_welcome_massage()
        self.personal_details_page.goto_page()
        self.personal_details_page.edit_button()
        self.personal_details_page.setup_middle_name(input_middle_name)
        self.personal_details_page.setup_emloyee_id(employee_id)
        self.personal_details_page.setup_other_id(other_id)
        self.personal_details_page.setup_emp_mick_name(nick_name)
        self.personal_details_page.setup_military_status(military_status)
        self.personal_details_page.save_button()
        self.personal_details_page.get_success_message()

        employee_full = driver.find_element_by_xpath('//*[@id="profile-pic"]/h1').text
        self.assertTrue(input_middle_name in employee_full)

    def test_03_edit_restricted_personal_details(self):
        driver = self.driver
        input_ssn = '50001000'
        driver_license_num = '002002002'
        sin_number = '9998765'
        date_of_birth = '03-09-1985'
        marital_text = 'Married'

        self.login_page.login()
        self.login_page.get_welcome_massage()
        self.personal_details_page.goto_page()
        self.personal_details_page.edit_button()
        self.personal_details_page.set_driver_license_num(driver_license_num)
        self.personal_details_page.set_sin_number(sin_number)
        self.personal_details_page.set_ssn_number(input_ssn)
        self.personal_details_page.set_smoker_radio_button()
        self.personal_details_page.set_date_of_birth(date_of_birth)
        self.personal_details_page.select_marital_status(marital_text)
        self.personal_details_page.save_button()
        self.personal_details_page.get_success_message()

        value_snn = driver.find_element_by_id('personal_txtNICNo').get_attribute('value')
        self.assertEqual(input_ssn, value_snn)


if __name__ == '__main__':
    unittest.main(testRunner= HtmlTestRunner.HTMLTestRunner(output ='/Users/nazarkruk/PycharmProjects/HRM100Full/Reports'))
