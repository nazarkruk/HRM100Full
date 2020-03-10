from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.page_url = "http://hrm-online.portnov.com/symfony/web/index.php/auth/login"

    def set_up_username(self, username):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys(username)

    def set_up_password(self, password):
        driver = self.driver
        driver.find_element_by_id('txtPassword').send_keys(password)

    def press_login_button(self):
        self.driver.find_element_by_id("btnLogin").click()

    def get_welcome_massage(self):
        return WebDriverWait(self.driver, 2).until(
                expected_conditions.presence_of_element_located((By.ID, 'welcome'))).text

    def login(self, username='admin', password='password'):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys(username)
        driver.find_element_by_id('txtPassword').send_keys(password)
        driver.find_element_by_id("btnLogin").click()


    def logout(self):
        self.driver.find_element_by_id('welcome').click()
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, 'Logout'))).click()

    def is_element_present(self, by, locator):
        try:
            self.driver.find_element(by, locator)
        except NoSuchElementException:
            return False
        return True


