import unittest
from selenium import webdriver
from fixtures.params import DOMAIN, CHROME_EXECUTABLE_PATH


from pages.login_page import LoginPage
from menus.main_menu import MainMenu


class UserTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_EXECUTABLE_PATH)
        self.driver.get(DOMAIN)
        self.login_page = LoginPage(self.driver)
        self.main_menus = MainMenu(self.driver)

    def tearDown(self):
        self.driver.quit()



    def test_user_menu(self):
        self.login_page.set_up_username('admin')
        self.login_page.set_up_password('password')
        self.login_page.press_login_button()

        welcome_text = self.login_page.get_welcome_massage()
        self.assertEqual('Welcome Admin', welcome_text)

        self.main_menus.goto_users_sub_menu()

        self.assertTrue('System Users', self.driver.find_element_by_xpath('//*[@id="systemUser-information"]/div[1]/h1').text)







if __name__ == '__main__':
    unittest.main()
