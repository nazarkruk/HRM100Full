#######################################################################################################################
#                           HERE IS SOME TIPS AND METHODS
#######################################################################################################################

# # # IMPORT ALL METHODS HERE # # #

import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.wait import WebDriverWait


# # # HERE IS THE NAME OF CLASS # # #
class MyTestCase(unittest.TestCase):

    # # # HERE IS WE SETUP ALL METHODS NEED TO BE DONE BEFORE EACH TEST # # #
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/PycharmProjects/HRM100Full/browsers_drivers/chromedriver")
        self.driver.get("http://hrm-online.portnov.com/")      # # # WILL OPEN PAGE URL

    # # # HERE IS WE SETUP ALL METHODS NEED TO BE DONE AFTER EACH TEST # # #

    def tearDown(self) -> None:
        self.driver.quit()          # # #W ILL QUIT CURRENT BROWSER SESSION

    # # # THE PLACE WHERE OUR TEST STARTING # # #
    def test_something(self):
        driver = self.driver

    # # # TO LOCATE ELEMENTS AND PERFORM SOME ACTIONS ON IT # # #

        driver.find_element_by_id('element_ID')     # # #  WILL LOCATE THE ELEMENT

        driver.find_element_by_id('element_ID').clear()    # # # WILL ERASE DATA FROM TEXT FIELD

        driver.find_element_by_id('element_ID').click()     # # # WILL PERFORM CLICK

        driver.find_element_by_id('element_ID').send_keys()     # # # WILL INPUT STRING TO TEXT FIELDS

        Select(driver.find_element_by_id('element_ID')).select_by_visible_text("Text")  # # # WILL SELECT ITEM FROM DROP DOWN LIST

        sleep(5)  # # # WILL WAIT 5 SECONDS BEFORE EXECUTE NEXT LINE OF YOUR CODE

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".css.selector"),
                                                                          'Displayed test'))    # # WILL WAIT EXPLICITLY UNTIL ELEMENT WITH TEXT WILL BE DESPLAYED

    # # # HERE IS ACTUAL TEST HAVE PLACE # # #

        self.assertEqual(True, False)       # # # WILL COMPARE FIRST AND SECOND ITEM AND TEST WILL PASS IF THEY EQUAL
        self.assertTrue(5 in 456)           # # # WILL CHECK IS EXPRESSION  - TRUE


# # # THAT'S THE JUNIT FRAMWORK PART # # #
if __name__ == '__main__':
    unittest.main()
