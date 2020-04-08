import unittest
from time import sleep

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.params import DOMAIN, CHROME_EXECUTABLE_PATH, JPG_500_kb_path, JPG_1_Mb_path, JPG_2_Mb_path, Py_file_path
from pages.add_photograph_page import AddPhotographPage
from pages.login_page import LoginPage
from pages.personal_details_page import PersonalDetailsPage


class AddPhotoTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_EXECUTABLE_PATH)
        self.driver.get(DOMAIN)
        self.wait = WebDriverWait(self.driver, 2)
        self.login_page = LoginPage(self.driver)
        self.personal_details_page = PersonalDetailsPage(self.driver)
        self.add_photograph_page = AddPhotographPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_04_add_valid_photo(self):
        file_path = JPG_500_kb_path
        self.login_page.login()
        self.login_page.get_welcome_massage()
        self.personal_details_page.goto_page()
        self.add_photograph_page.emloyee_picture()
        self.add_photograph_page.chose_file(file_path)
        self.add_photograph_page.upload_button()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Uploaded'))

    def test_05_add_1_1mb_photo(self):
        file_path = JPG_1_Mb_path
        self.login_page.login()
        self.login_page.get_welcome_massage()
        self.personal_details_page.goto_page()
        self.add_photograph_page.emloyee_picture()
        self.add_photograph_page.chose_file(file_path)
        self.add_photograph_page.upload_button()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.warning"),
                                                                          'Failed to Save: File Size Exceeded'))

    def test_06_add_more_1mb_photo(self):
        file_path = JPG_2_Mb_path
        self.login_page.login()
        self.login_page.get_welcome_massage()
        self.personal_details_page.goto_page()
        self.add_photograph_page.emloyee_picture()
        self.add_photograph_page.chose_file(file_path)
        self.add_photograph_page.upload_button()

        crash_message = self.driver.find_element_by_xpath('/html/body/center[1]/h1').text
        self.assertEqual('413 Request Entity Too Large', crash_message)

    def test_07_add_invalid_format_photo(self):
        file_path = Py_file_path
        self.login_page.login()
        self.login_page.get_welcome_massage()
        self.personal_details_page.goto_page()
        self.add_photograph_page.emloyee_picture()
        self.add_photograph_page.chose_file(file_path)
        self.add_photograph_page.upload_button()

        #self.wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".message.warning")))
        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.warning"),'Failed to Save: File Type Not Allowed'))


    """

        ======USE THIS TEST CASE AS EXAMPLE OF WHILE LOOP=======

        def test_04_add_photograph(self):
            driver = self.driver
            driver.find_element_by_id('txtUsername').send_keys('admin')
            driver.find_element_by_id('txtPassword').send_keys('password')
            driver.find_element_by_id("btnLogin").click()

            sleep(1)

            driver.find_element_by_id('menu_pim_viewMyDetails').click()
            driver.find_element_by_id('empPic').click()

            while True:
                try:
                    button = driver.find_element_by_id('btnDelete')
                    button.click()
                    driver.switch_to.active_element
                    driver.find_element_by_id('btnYes').click()
                    self.wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".message.warning")))
                    self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                                      'Successfully Deleted'))
                except:
                    driver.find_element_by_id('empPic').click()
                    driver.find_element_by_name('photofile').send_keys('/Users/nazarkruk/Desktop/jpg_500kbmb.jpg')
                    driver.find_element_by_id('btnSave').click()
                    self.wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".message.success")))
                    self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                                      'Successfully Uploaded'))

                    break



            else:
                driver.find_element_by_id('empPic').click()
                driver.find_element_by_name('photofile').send_keys('/Users/nazarkruk/Desktop/jpg_500kbmb.jpg')
                driver.find_element_by_id('btnSave').click()
                self.wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".message.success")))
                self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                                  'Successfully Uploaded'))

            button_delete = driver.find_element_by_id('btnDelete').text

            self.assertTrue('Delete', button_delete)

            self.assertTrue(True)
    """


if __name__ == '__main__':
    unittest.main(testRunner= HtmlTestRunner.HTMLTestRunner(output ='/Users/nazarkruk/PycharmProjects/HRM100Full/Reports'))
