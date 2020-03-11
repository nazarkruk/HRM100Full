from selenium.webdriver.support.select import Select
class ContactDetailsPage:

    def __init__(self, driver):
        self.driver = driver

    def goto_page(self):
        self.driver.find_element_by_link_text('Contact Details').click()

    def edit_button(self):
        self.driver.find_element_by_id('btnSave').click()

    def save_button(self):
        self.driver.find_element_by_id('btnSave').click()

    def set_address_1(self, address_1):
        self.driver.find_element_by_id('contact_street1').clear()
        self.driver.find_element_by_id('contact_street1').send_keys(address_1)

    def set_address_2(self, address_2):
        self.driver.find_element_by_id('contact_street2').clear()
        self.driver.find_element_by_id('contact_street2').send_keys(address_2)

    def set_city(self, city):
        self.driver.find_element_by_id('contact_city').clear()
        self.driver.find_element_by_id('contact_city').send_keys(city)

    def set_state_province(self, state_province):
        self.driver.find_element_by_id('contact_province').clear()
        self.driver.find_element_by_id('contact_province').send_keys(state_province)

    def set_zip_code(self, zip_code):
        self.driver.find_element_by_id('contact_emp_zipcode').clear()
        self.driver.find_element_by_id('contact_emp_zipcode').send_keys(zip_code)

    def select_conuntry_by_index(self, country_index):
        Select(self.driver.find_element_by_id('contact_country')).select_by_index(country_index)