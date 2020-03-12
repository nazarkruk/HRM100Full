import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.params import CHROME_EXECUTABLE_PATH, DOMAIN, JPG_500_kb_path, Pdf_file_path, JPG_2_Mb_path
from pages.add_photograph_page import AddPhotographPage
from pages.contact_details_page import ContactDetailsPage
from pages.emergency_contacts_page import EmergencyContactsPage
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
        self.emergency_contacts_page = EmergencyContactsPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_16_add_emergency_contacts(self):
        name = 'Emer'
        relationship = 'wife'
        home_phone = '123456789'
        mobile_phone = '987654321'
        work_phone = '123366654'

        self.login_page.login()
        self.login_page.get_welcome_massage()
        self.personal_details_page.goto_page()
        self.emergency_contacts_page.goto_page()
        self.emergency_contacts_page.add_contact_button()
        self.emergency_contacts_page.set_name(name)
        self.emergency_contacts_page.set_relationship(relationship)
        self.emergency_contacts_page.set_home_phone(home_phone)
        self.emergency_contacts_page.set_mobile_phone(mobile_phone)
        self.emergency_contacts_page.set_work_phone(work_phone)
        self.emergency_contacts_page.save_button()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),'Successfully Saved'))
        table_name = self.driver.find_element_by_xpath('//*[@id="emgcontact_list"]/tbody/tr[1]/td[2]/a')
        self.assertTrue(table_name.text == name)

        # deleting created emergency contact
        self.driver.find_element_by_css_selector("td>input").click()
        self.driver.find_element_by_id("delContactsBtn").click()
        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),'Successfully Deleted'))



    def test_17_emergency_name_requered(self):
        driver = self.driver
        relationship = 'wife'
        home_phone = '123456789'
        mobile_phone = '987654321'
        work_phone = '123366654'

        self.login_page.login()
        self.login_page.get_welcome_massage()
        self.personal_details_page.goto_page()
        self.emergency_contacts_page.goto_page()
        self.emergency_contacts_page.add_contact_button()
        self.emergency_contacts_page.set_relationship(relationship)
        self.emergency_contacts_page.set_home_phone(home_phone)
        self.emergency_contacts_page.set_mobile_phone(mobile_phone)
        self.emergency_contacts_page.set_work_phone(work_phone)
        self.emergency_contacts_page.save_button()

        self.assertTrue(driver.find_element_by_xpath('//*[@id="frmEmpEmgContact"]/fieldset/ol/li[1]/span').text == 'Required')


    def test_18_emergency_relationship_requered(self):
        driver = self.driver

        name = 'Emer'
        home_phone = '123456789'
        mobile_phone = '987654321'
        work_phone = '123366654'

        self.login_page.login()
        self.login_page.get_welcome_massage()
        self.personal_details_page.goto_page()
        self.emergency_contacts_page.goto_page()
        self.emergency_contacts_page.add_contact_button()
        self.emergency_contacts_page.set_name(name)
        self.emergency_contacts_page.set_home_phone(home_phone)
        self.emergency_contacts_page.set_mobile_phone(mobile_phone)
        self.emergency_contacts_page.set_work_phone(work_phone)
        self.emergency_contacts_page.save_button()


        self.assertTrue(driver.find_element_by_xpath('//*[@id="frmEmpEmgContact"]/fieldset/ol/li[2]/span').text == 'Required')

    def test_19_emergency_one_phone_enough(self):
        name = 'Emer'
        relationship = 'wife'
        home_phone = '123456789'

        self.login_page.login()
        self.login_page.get_welcome_massage()
        self.personal_details_page.goto_page()
        self.emergency_contacts_page.goto_page()
        self.emergency_contacts_page.add_contact_button()
        self.emergency_contacts_page.set_name(name)
        self.emergency_contacts_page.set_relationship(relationship)
        self.emergency_contacts_page.set_home_phone(home_phone)
        self.emergency_contacts_page.save_button()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Saved'))

    def test_20_emergency_one_phone_requered(self):
        driver = self.driver
        name = 'Emer'
        relationship = 'wife'

        self.login_page.login()
        self.login_page.get_welcome_massage()
        self.personal_details_page.goto_page()
        self.emergency_contacts_page.goto_page()
        self.emergency_contacts_page.add_contact_button()
        self.emergency_contacts_page.set_name(name)
        self.emergency_contacts_page.set_relationship(relationship)
        self.emergency_contacts_page.save_button()

        self.assertTrue(driver.find_element_by_xpath('//*[@id="frmEmpEmgContact"]/fieldset/ol/li[3]/span').text == 'At least one phone number is required')

    def test_21_add_multiply_emg_contacts(self):
        name = 'Emer'
        relationship = 'wife'
        home_phone = '123456789'
        mobile_phone = '987654321'
        work_phone = '123366654'

        self.login_page.login()
        self.login_page.get_welcome_massage()
        self.personal_details_page.goto_page()
        self.emergency_contacts_page.goto_page()
        self.emergency_contacts_page.add_contact_button()
        self.emergency_contacts_page.set_name(name)
        self.emergency_contacts_page.set_relationship(relationship)
        self.emergency_contacts_page.set_home_phone(home_phone)
        self.emergency_contacts_page.set_mobile_phone(mobile_phone)
        self.emergency_contacts_page.set_work_phone(work_phone)
        self.emergency_contacts_page.save_button()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),'Successfully Saved'))

        self.emergency_contacts_page.add_contact_button()
        self.emergency_contacts_page.set_name(name)
        self.emergency_contacts_page.set_relationship(relationship)
        self.emergency_contacts_page.set_home_phone(home_phone)
        self.emergency_contacts_page.set_mobile_phone(mobile_phone)
        self.emergency_contacts_page.set_work_phone(work_phone)
        self.emergency_contacts_page.save_button()
        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Saved'))
        # deleting all emergency contacts
        self.driver.find_element_by_id('checkAll').click()
        self.driver.find_element_by_id("delContactsBtn").click()
        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Deleted'))

    def test_22_delete_emg_contacts(self):

        name = 'Emer'
        relationship = 'wife'
        home_phone = '123456789'

        self.login_page.login()
        self.login_page.get_welcome_massage()
        self.personal_details_page.goto_page()
        self.emergency_contacts_page.goto_page()
        self.emergency_contacts_page.add_contact_button()
        self.emergency_contacts_page.set_name(name)
        self.emergency_contacts_page.set_relationship(relationship)
        self.emergency_contacts_page.set_home_phone(home_phone)
        self.emergency_contacts_page.save_button()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Saved'))

        self.driver.find_element_by_css_selector("td>input").click()
        self.driver.find_element_by_id("delContactsBtn").click()
        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Deleted'))

    def test_23_add_attachment_emg_contacts(self):
        file_path = Pdf_file_path

        self.login_page.login()
        self.login_page.get_welcome_massage()
        self.personal_details_page.goto_page()
        self.emergency_contacts_page.goto_page()
        self.emergency_contacts_page.add_attachment_button()
        self.emergency_contacts_page.choose_file(file_path)
        self.emergency_contacts_page.upload_button()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),'Successfully Saved'))
        # cleanup_deleting attachment
        self.driver.find_element_by_css_selector("#tblAttachments > tbody > tr.odd > td.center > input").click()
        self.driver.find_element_by_id("btnDeleteAttachment").click()
        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Deleted'))

    def test_24_delete_attachment_emg_contacts(self):
        file_path = Pdf_file_path

        self.login_page.login()
        self.login_page.get_welcome_massage()
        self.personal_details_page.goto_page()
        self.emergency_contacts_page.goto_page()
        self.emergency_contacts_page.add_attachment_button()
        self.emergency_contacts_page.choose_file(file_path)
        self.emergency_contacts_page.upload_button()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),'Successfully Saved'))

        self.driver.find_element_by_css_selector("#tblAttachments > tbody > tr.odd > td.center > input").click()
        self.driver.find_element_by_id("btnDeleteAttachment").click()
        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Deleted'))

    def test_25_add_attachment_large_size(self):
        file_path = JPG_2_Mb_path

        self.login_page.login()
        self.login_page.get_welcome_massage()
        self.personal_details_page.goto_page()
        self.emergency_contacts_page.goto_page()
        self.emergency_contacts_page.add_attachment_button()
        self.emergency_contacts_page.choose_file(file_path)
        self.emergency_contacts_page.upload_button()

        self.assertEqual('413 Request Entity Too Large', self.driver.find_element_by_xpath('/html/body/center[1]/h1').text)


if __name__ == '__main__':
    unittest.main()
