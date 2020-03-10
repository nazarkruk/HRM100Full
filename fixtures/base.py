import unittest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.params import CHROME_EXECUTABLE_PATH, EXPLICIT_TIMEOUT, DOMAIN, BROWSER_TYPE, FIREFOX_EXECUTABLE_PATH
from pages.login_page import LoginPage


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_EXECUTABLE_PATH)
        self.wait = WebDriverWait(self.driver, EXPLICIT_TIMEOUT)


    def tearDown(self):
        self.driver.quit()


class AdminLoginTestCase(BaseTestCase):

    def get_browser(self):
        if BROWSER_TYPE.lower().find("chrome") >= 0:
            self.driver = webdriver.Chrome(executable_path=CHROME_EXECUTABLE_PATH)
        elif BROWSER_TYPE.lower().find("firefox") >=0:
            self.driver = webdriver.Firefox(executable_path=FIREFOX_EXECUTABLE_PATH)
        else:
            raise Error('')

    def setUp(self):
        super(AdminLoginTestCase, self).setUp()
        self.login = LoginPage(self.driver)
        self.driver.get(DOMAIN)
        ####login(self.driver)

    def tearDown(self):
        super(AdminLoginTestCase, self).tearDown()



class POMAdminLoginTestCase(BaseTestCase):
    def setUp(self):
        super(POMAdminLoginTestCase, self).setUp()
        self.login = LoginPage(self.driver)
        self.driver.get('http://hrm-online.portnov.com/')
        self.login.goto_page()
        self.login.login()


    def tearDown(self):
        super(POMAdminLoginTestCase, self).tearDown()


class POMAdminLoginTestCase(BaseTestCase):
    def setUp(self):
        super(POMAdminLoginTestCase, self).setUp()
        self.login = LoginPage(self.driver)
        self.driver.get('http://hrm-online.portnov.com/')
        self.login.goto_page()
        self.login.login()

    def tearDown(self):
        super(POMAdminLoginTestCase, self).tearDown()

if __name__ == '__main__':
    unittest.main()