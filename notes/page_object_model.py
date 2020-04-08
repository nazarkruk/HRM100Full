#######################################################################################################################
#                           HERE IS HOW TO IMPLEMENT POM
#######################################################################################################################
'''

1. Create instances of the pages in setUp:

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_EXECUTABLE_PATH)
        self.driver.get(DOMAIN)
        self.wait = WebDriverWait(self.driver, 2)
        self.login_page = LoginPage(self.driver)
        self.personal_details_page = PersonalDetailsPage(self.driver)
        self.add_photograph_page = AddPhotographPage(self.driver)
        self.contact_details_page = ContactDetailsPage(self.driver)
        self.emergency_contacts_page = EmergencyContactsPage(self.driver)

2. Import Classes from pages:

from pages.add_photograph_page import AddPhotographPage
from pages.contact_details_page import ContactDetailsPage
from pages.emergency_contacts_page import EmergencyContactsPage
from pages.login_page import LoginPage
from pages.personal_details_page import PersonalDetailsPage


3. Create all functions in page.py starting with constructor bellow

class ContactDetailsPage:

    def __init__(self, driver):
        self.driver = driver

    def goto_page(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'Contact Details'))).click()

    def edit_button(self):
        self.driver.find_element_by_id('btnSave').click()






'''