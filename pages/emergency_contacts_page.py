from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class EmergencyContactsPage:


    def __init__(self, driver):
        self.driver = driver

    def goto_page(self):
        self.driver.find_element_by_link_text('Emergency Contacts').click()

    def add_contact_button(self):
        self.driver.find_element_by_id('btnAddContact').click()

    def set_name(self, name):
        self.driver.find_element_by_id('emgcontacts_name').clear()
        self.driver.find_element_by_id('emgcontacts_name').send_keys(name)

    def set_relationship(self, relationship):
        self.driver.find_element_by_id('emgcontacts_relationship').clear()
        self.driver.find_element_by_id('emgcontacts_relationship').send_keys(relationship)

    def set_home_phone(self, home_phone):
        self.driver.find_element_by_id('emgcontacts_homePhone').clear()
        self.driver.find_element_by_id('emgcontacts_homePhone').send_keys(home_phone)

    def set_mobile_phone(self, mobile_phone):
        self.driver.find_element_by_id('emgcontacts_mobilePhone').clear()
        self.driver.find_element_by_id('emgcontacts_mobilePhone').send_keys(mobile_phone)

    def set_work_phone(self, work_phone):
        self.driver.find_element_by_id('emgcontacts_workPhone').clear()
        self.driver.find_element_by_id('emgcontacts_workPhone').send_keys(work_phone)

    def save_button(self):
        self.driver.find_element_by_id('btnSaveEContact').click()

    def add_attachment_button(self):
        self.driver.find_element_by_id('btnAddAttachment').click()

    def choose_file(self, file_path):
        self.driver.find_element_by_id('ufile').send_keys(file_path)

    def upload_button(self):
        self.driver.find_element_by_id('btnSaveAttachment').click()