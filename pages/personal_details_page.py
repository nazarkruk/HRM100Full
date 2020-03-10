
class PersonalDetailsPage:

    def __init__(self, driver):
        self.driver = driver

    def goto_page(self):
        self.driver.find_element_by_id('menu_pim_viewMyDetails').click()

    def edit_button(self):
        self.driver.find_element_by_id('btnSave').click()