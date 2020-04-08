import unittest

import HtmlTestRunner
from selenium import webdriver
from fixtures.params import CHROME_EXECUTABLE_PATH, DOMAIN
from pages.login_page import LoginPage


class LoginTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_EXECUTABLE_PATH)
        self.driver.get(DOMAIN)
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_01_valid_login(self):
        self.login_page.set_up_username('admin')
        self.login_page.set_up_password('password')
        self.login_page.press_login_button()

        welcome_text = self.login_page.get_welcome_massage()
        self.assertEqual('Welcome Admin', welcome_text)




if __name__ == '__main__':
    unittest.main(testRunner= HtmlTestRunner.HTMLTestRunner(output ='/Users/nazarkruk/PycharmProjects/HRM100Full/Reports'))
