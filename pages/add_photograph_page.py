class AddPhotographPage:

    def __init__(self, driver):
        self.driver = driver

    def emloyee_picture(self):
        self.driver.find_element_by_id('empPic').click()
