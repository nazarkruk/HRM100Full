from selenium.webdriver import ActionChains


class MainMenu():

    def __init__(self, driver):
        self.driver = driver

    def goto_users_sub_menu(self):


        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]/b')).move_to_element(self.driver.find_element_by_id('menu_admin_UserManagement')).move_to_element(self.driver.find_element_by_id('menu_admin_viewSystemUsers')).click().perform()
