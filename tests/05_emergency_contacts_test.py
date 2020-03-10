import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ContactDetailsTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='/Users/nazarkruk/PycharmProjects/HRM100Full/browsers_drivers/chromedriver')
        self.driver.get("http://hrm-online.portnov.com/")
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_16_add_emergency_contacts(self):
        driver = self.driver
        emergency_contact_name = 'Emer'

        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Emergency Contacts').click()

        sleep(1)

        driver.find_element_by_id('btnAddContact').click()

        driver.find_element_by_id('emgcontacts_name').clear()
        driver.find_element_by_id('emgcontacts_name').send_keys(emergency_contact_name)
        driver.find_element_by_id('emgcontacts_relationship').clear()
        driver.find_element_by_id('emgcontacts_relationship').send_keys('wife')
        driver.find_element_by_id('emgcontacts_homePhone').clear()
        driver.find_element_by_id('emgcontacts_homePhone').send_keys(123456789)
        driver.find_element_by_id('emgcontacts_mobilePhone').clear()
        driver.find_element_by_id('emgcontacts_mobilePhone').send_keys(987654321)
        driver.find_element_by_id('emgcontacts_workPhone').clear()
        driver.find_element_by_id('emgcontacts_workPhone').send_keys(123321456)

        driver.find_element_by_id('btnSaveEContact').click()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),'Successfully Saved'))

        table_name = self.driver.find_element_by_xpath('//*[@id="emgcontact_list"]/tbody/tr[1]/td[2]/a')

        self.assertTrue(table_name.text == emergency_contact_name)

        self.driver.find_element_by_css_selector("td>input").click()

        self.driver.find_element_by_id("delContactsBtn").click()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),'Successfully Deleted'))



    def test_17_emergency_name_requered(self):
        driver = self.driver

        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Emergency Contacts').click()

        sleep(1)

        driver.find_element_by_id('btnAddContact').click()

        driver.find_element_by_id('emgcontacts_name').clear()
        driver.find_element_by_id('emgcontacts_relationship').clear()
        driver.find_element_by_id('emgcontacts_relationship').send_keys('wife')
        driver.find_element_by_id('emgcontacts_homePhone').clear()
        driver.find_element_by_id('emgcontacts_homePhone').send_keys(123456789)
        driver.find_element_by_id('emgcontacts_mobilePhone').clear()
        driver.find_element_by_id('emgcontacts_mobilePhone').send_keys(987654321)
        driver.find_element_by_id('emgcontacts_workPhone').clear()
        driver.find_element_by_id('emgcontacts_workPhone').send_keys(123321456)

        driver.find_element_by_id('btnSaveEContact').click()

        self.assertTrue(driver.find_element_by_xpath('//*[@id="frmEmpEmgContact"]/fieldset/ol/li[1]/span').text == 'Required')


    def test_18_emergency_relationship_requered(self):
        driver = self.driver

        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Emergency Contacts').click()

        sleep(1)

        driver.find_element_by_id('btnAddContact').click()

        driver.find_element_by_id('emgcontacts_name').clear()
        driver.find_element_by_id('emgcontacts_name').send_keys('Emmy')
        driver.find_element_by_id('emgcontacts_relationship').clear()
        driver.find_element_by_id('emgcontacts_homePhone').clear()
        driver.find_element_by_id('emgcontacts_homePhone').send_keys(123456789)
        driver.find_element_by_id('emgcontacts_mobilePhone').clear()
        driver.find_element_by_id('emgcontacts_mobilePhone').send_keys(987654321)
        driver.find_element_by_id('emgcontacts_workPhone').clear()
        driver.find_element_by_id('emgcontacts_workPhone').send_keys(123321456)

        driver.find_element_by_id('btnSaveEContact').click()

        self.assertTrue(driver.find_element_by_xpath('//*[@id="frmEmpEmgContact"]/fieldset/ol/li[2]/span').text == 'Required')

    def test_19_emergency_one_phone_enough(self):
        driver = self.driver

        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Emergency Contacts').click()

        sleep(1)

        driver.find_element_by_id('btnAddContact').click()

        driver.find_element_by_id('emgcontacts_name').clear()
        driver.find_element_by_id('emgcontacts_name').send_keys('Emmy')
        driver.find_element_by_id('emgcontacts_relationship').clear()
        driver.find_element_by_id('emgcontacts_relationship').send_keys('wife')
        driver.find_element_by_id('emgcontacts_homePhone').clear()
        driver.find_element_by_id('emgcontacts_homePhone').send_keys(123456789)

        driver.find_element_by_id('btnSaveEContact').click()
        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Saved'))

    def test_20_emergency_one_phone_requered(self):
        driver = self.driver

        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Emergency Contacts').click()

        sleep(1)

        driver.find_element_by_id('btnAddContact').click()

        driver.find_element_by_id('emgcontacts_name').clear()
        driver.find_element_by_id('emgcontacts_name').send_keys('Emmy')
        driver.find_element_by_id('emgcontacts_relationship').clear()
        driver.find_element_by_id('emgcontacts_relationship').send_keys('wife')

        driver.find_element_by_id('btnSaveEContact').click()

        self.assertTrue(driver.find_element_by_xpath('//*[@id="frmEmpEmgContact"]/fieldset/ol/li[3]/span').text == 'At least one phone number is required')

    def test_21_add_multiply_emg_contacts(self):
        driver = self.driver

        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Emergency Contacts').click()

        sleep(1)

        driver.find_element_by_id('btnAddContact').click()

        driver.find_element_by_id('emgcontacts_name').clear()
        driver.find_element_by_id('emgcontacts_name').send_keys('Emmy')
        driver.find_element_by_id('emgcontacts_relationship').clear()
        driver.find_element_by_id('emgcontacts_relationship').send_keys('wife')
        driver.find_element_by_id('emgcontacts_homePhone').clear()
        driver.find_element_by_id('emgcontacts_homePhone').send_keys(123456789)

        driver.find_element_by_id('btnSaveEContact').click()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Saved'))
        driver.find_element_by_id('btnAddContact').click()

        driver.find_element_by_id('emgcontacts_name').clear()
        driver.find_element_by_id('emgcontacts_name').send_keys('Emmy')
        driver.find_element_by_id('emgcontacts_relationship').clear()
        driver.find_element_by_id('emgcontacts_relationship').send_keys('wife')
        driver.find_element_by_id('emgcontacts_homePhone').clear()
        driver.find_element_by_id('emgcontacts_homePhone').send_keys(123456789)

        driver.find_element_by_id('btnSaveEContact').click()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Saved'))

        self.driver.find_element_by_id('checkAll').click()
        self.driver.find_element_by_id("delContactsBtn").click()
        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Deleted'))

    def test_22_delete_emg_contacts(self):
        driver = self.driver

        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Emergency Contacts').click()

        sleep(1)

        driver.find_element_by_id('btnAddContact').click()

        driver.find_element_by_id('emgcontacts_name').clear()
        driver.find_element_by_id('emgcontacts_name').send_keys('Emmy')
        driver.find_element_by_id('emgcontacts_relationship').clear()
        driver.find_element_by_id('emgcontacts_relationship').send_keys('wife')
        driver.find_element_by_id('emgcontacts_homePhone').clear()
        driver.find_element_by_id('emgcontacts_homePhone').send_keys(123456789)

        driver.find_element_by_id('btnSaveEContact').click()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Saved'))

        self.driver.find_element_by_css_selector("td>input").click()
        self.driver.find_element_by_id("delContactsBtn").click()
        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Deleted'))

    def test_23_add_attachment_emg_contacts(self):
        driver = self.driver

        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Emergency Contacts').click()

        sleep(1)

        driver.find_element_by_id('btnAddAttachment').click()

        driver.find_element_by_id('ufile').send_keys('/Users/nazarkruk/Desktop/Orange_HRM/Orange-HRM-Test_Plan.pdf')

        driver.find_element_by_id('btnSaveAttachment').click()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),'Successfully Saved'))

        self.driver.find_element_by_css_selector("#tblAttachments > tbody > tr.odd > td.center > input").click()

        self.driver.find_element_by_id("btnDeleteAttachment").click()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Deleted'))

    def test_24_delete_attachment_emg_contacts(self):
        driver = self.driver

        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Emergency Contacts').click()

        sleep(1)

        driver.find_element_by_id('btnAddAttachment').click()

        driver.find_element_by_id('ufile').send_keys('/Users/nazarkruk/Desktop/Orange_HRM/Orange-HRM-Test_Plan.pdf')

        driver.find_element_by_id('btnSaveAttachment').click()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),'Successfully Saved'))

        self.driver.find_element_by_css_selector("#tblAttachments > tbody > tr.odd > td.center > input").click()

        self.driver.find_element_by_id("btnDeleteAttachment").click()
        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Deleted'))

    def test_25_add_attachment_large_size(self):
        driver = self.driver

        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Emergency Contacts').click()

        sleep(1)

        driver.find_element_by_id('btnAddAttachment').click()

        driver.find_element_by_id('ufile').send_keys('/Users/nazarkruk/Desktop/Orange_HRM/jpg_2mb.jpg')

        driver.find_element_by_id('btnSaveAttachment').click()

        sleep(1)

        crash_message = driver.find_element_by_xpath('/html/body/center[1]/h1').text

        self.assertEqual('413 Request Entity Too Large', crash_message)


if __name__ == '__main__':
    unittest.main()
