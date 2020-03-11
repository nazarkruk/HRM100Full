import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.params import DOMAIN, CHROME_EXECUTABLE_PATH
from pages.add_photograph_page import AddPhotographPage
from pages.contact_details_page import ContactDetailsPage
from pages.login_page import LoginPage
from pages.personal_details_page import PersonalDetailsPage


class ContactDetailsTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_EXECUTABLE_PATH)
        self.driver.get(DOMAIN)
        self.wait = WebDriverWait(self.driver, 2)
        self.login_page = LoginPage(self.driver)
        self.personal_details_page = PersonalDetailsPage(self.driver)
        self.add_photograph_page = AddPhotographPage(self.driver)
        self.contact_details_page = ContactDetailsPage(self.driver)

    def tearDown(self):
        self.driver.quit()


    def test_08_contact_details(self):

        self.login_page.login()
        self.login_page.get_welcome_massage()
        self.personal_details_page.goto_page()
        sleep(1)
        self.contact_details_page.goto_page()
        sleep(1)

        page_title = self.driver.find_element_by_xpath('//*[@id="contact-details"]/div[2]/div[1]/h1').text
        self.assertEqual('Contact Details', page_title)

    def test_09_is_contact_details_editable(self):
        driver = self.driver
        self.login_page.login()
        self.login_page.get_welcome_massage()
        self.personal_details_page.goto_page()
        self.contact_details_page.goto_page()
        self.contact_details_page.edit_button()

        self.assertTrue(driver.find_element_by_id('contact_street1').is_enabled())

    def test_10_contact_details_edit(self):
        driver = self.driver
        address_1 = 'adress1_1234!@#$'
        address_2 = 'adress2_f1234!@#$'
        city = 'city_asdf1234!@#$'
        state_province = 'state_asdf1234!@#$'
        zip_code = 'zip1234!@#$'
        country_index = '5'

        self.login_page.login()
        self.login_page.get_welcome_massage()
        self.personal_details_page.goto_page()
        self.contact_details_page.goto_page()
        self.contact_details_page.edit_button()
        self.contact_details_page.set_address_1(address_1)
        self.contact_details_page.set_address_2(address_2)
        self.contact_details_page.set_city(city)
        self.contact_details_page.set_state_province(state_province)
        self.contact_details_page.set_zip_code(zip_code)
        self.contact_details_page.select_conuntry_by_index(country_index)
        self.contact_details_page.save_button()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),'Successfully Saved'))

        self.assertEqual(city, driver.find_element_by_id('contact_city').get_attribute('value'))

    def test_11_contact_valid_zip_10(self):
        driver = self.driver
        zip_code = '1234567890'

        self.login_page.login()
        self.login_page.get_welcome_massage()
        self.personal_details_page.goto_page()
        self.contact_details_page.goto_page()
        self.contact_details_page.edit_button()
        self.contact_details_page.set_zip_code(zip_code)
        self.contact_details_page.save_button()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),'Successfully Saved'))

        self.assertEqual(zip_code, driver.find_element_by_id('contact_emp_zipcode').get_attribute('value'))


    def test_11_1_contact_zip_more_10(self):
        driver = self.driver
        zip_code = '123456789123456789'

        self.login_page.login()
        self.login_page.get_welcome_massage()
        self.personal_details_page.goto_page()
        self.contact_details_page.goto_page()
        self.contact_details_page.edit_button()
        self.contact_details_page.set_zip_code(zip_code)
        self.contact_details_page.save_button()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),'Successfully Saved'))

        number_characters = len(driver.find_element_by_id('contact_emp_zipcode').get_attribute('value'))
        self.assertTrue(number_characters <= 10)

    def test_12_contact_valid_phone(self):
        driver = self.driver
        phone_number = '1234567890+ - / ( )'
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Contact Details').click()

        sleep(1)

        driver.find_element_by_id('btnSave').click()

        driver.find_element_by_id('contact_emp_hm_telephone').clear()
        driver.find_element_by_id('contact_emp_hm_telephone').send_keys(phone_number)
        driver.find_element_by_id('contact_emp_mobile').clear()
        driver.find_element_by_id('contact_emp_mobile').send_keys(phone_number)
        driver.find_element_by_id('contact_emp_work_telephone').clear()
        driver.find_element_by_id('contact_emp_work_telephone').send_keys(phone_number)

        driver.find_element_by_id('btnSave').click()

        # self.wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".message.success")))
        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),'Successfully Saved'))

        input_num = driver.find_element_by_id('contact_emp_mobile')
        value_mobile = input_num.get_attribute('value')

        self.assertEqual(phone_number, value_mobile)

    def test_13_contact_invalid_phone(self):
        driver = self.driver
        phone_number = 'abc!4567890+ - / ( )'
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Contact Details').click()

        sleep(1)

        driver.find_element_by_id('btnSave').click()

        driver.find_element_by_id('contact_emp_hm_telephone').clear()
        driver.find_element_by_id('contact_emp_hm_telephone').send_keys(phone_number)
        driver.find_element_by_id('contact_emp_mobile').clear()
        driver.find_element_by_id('contact_emp_mobile').send_keys(phone_number)
        driver.find_element_by_id('contact_emp_work_telephone').clear()
        driver.find_element_by_id('contact_emp_work_telephone').send_keys(phone_number)

        driver.find_element_by_id('btnSave').click()

        self.assertTrue(driver.find_element_by_xpath('//*[@id="frmEmpContactDetails"]/fieldset/ol[2]/li[1]/span').text == 'Allows numbers and only + - / ( )')

    def test_14_contact_valid_email(self):
        driver = self.driver
        work_email = 'work@test.test'
        other_email = 'other@test.test'
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Contact Details').click()

        sleep(1)

        driver.find_element_by_id('btnSave').click()

        driver.find_element_by_id('contact_emp_work_email').clear()
        driver.find_element_by_id('contact_emp_work_email').send_keys(work_email)
        driver.find_element_by_id('contact_emp_oth_email').clear()
        driver.find_element_by_id('contact_emp_oth_email').send_keys(other_email)


        driver.find_element_by_id('btnSave').click()


        value_work_email = driver.find_element_by_id('contact_emp_work_email').get_attribute('value')
        value_other_email = driver.find_element_by_id('contact_emp_oth_email').get_attribute('value')

        self.assertEqual(work_email, value_work_email)
        self.assertEqual(other_email, value_other_email)


    def test_15_contact_invalid_email(self):
        driver = self.driver
        work_email = 'work@test'
        other_email = '@test.test'
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Contact Details').click()

        sleep(1)

        driver.find_element_by_id('btnSave').click()

        driver.find_element_by_id('contact_emp_work_email').clear()
        driver.find_element_by_id('contact_emp_work_email').send_keys(work_email)
        driver.find_element_by_id('contact_emp_oth_email').clear()
        driver.find_element_by_id('contact_emp_oth_email').send_keys(other_email)


        driver.find_element_by_id('btnSave').click()

        self.assertTrue(driver.find_element_by_xpath('//*[@id="frmEmpContactDetails"]/fieldset/ol[3]/li[1]/span').text == 'Expected format: admin@example.com')



    def test_15_contact_same_email(self):
        driver = self.driver
        work_email = 'work@test.test'

        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Contact Details').click()

        sleep(1)

        driver.find_element_by_id('btnSave').click()

        driver.find_element_by_id('contact_emp_work_email').clear()
        driver.find_element_by_id('contact_emp_work_email').send_keys(work_email)
        driver.find_element_by_id('contact_emp_oth_email').clear()
        driver.find_element_by_id('contact_emp_oth_email').send_keys(work_email)

        driver.find_element_by_id('btnSave').click()

        self.assertTrue(driver.find_element_by_xpath('//*[@id="frmEmpContactDetails"]/fieldset/ol[3]/li[2]/span').text == 'Already exists')


if __name__ == '__main__':
    unittest.main()
