


class AddPhotographPage:

    def __init__(self, driver):
        self.driver = driver

    def emloyee_picture(self):
        self.driver.find_element_by_id('empPic').click()

    def chose_file(self, file_path):
        self.driver.find_element_by_name('photofile').send_keys(file_path)

    def upload_button(self):
        self.driver.find_element_by_id('btnSave').click()

