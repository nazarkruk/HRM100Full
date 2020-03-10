import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class AddPhotoTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='/Users/nazarkruk/PycharmProjects/HRM100Full/browsers_drivers/chromedriver')
        self.driver.get("http://hrm-online.portnov.com/")
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_04_add_valid_photo(self):

        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_id('empPic').click()

        driver.find_element_by_id('empPic').click()
        driver.find_element_by_name('photofile').send_keys('/Users/nazarkruk/Desktop/Orange_HRM/simple_image/jpg_500kbmb.jpg')
        driver.find_element_by_id('btnSave').click()

        self.wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".message.success")))
        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Uploaded'))

    def test_05_add_1_1mb_photo(self):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_id('empPic').click()

        driver.find_element_by_id('empPic').click()
        driver.find_element_by_name('photofile').send_keys('/Users/nazarkruk/Desktop/Orange_HRM/simple_image/jpg_1mb.jpg')
        driver.find_element_by_id('btnSave').click()
        self.wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".message.warning")))
        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.warning"),
                                                                          'Failed to Save: File Size Exceeded'))

    def test_06_add_more_1mb_photo(self):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_id('empPic').click()

        driver.find_element_by_id('empPic').click()
        driver.find_element_by_name('photofile').send_keys('/Users/nazarkruk/Desktop/Orange_HRM/simple_image/jpg_2mb.jpg')
        driver.find_element_by_id('btnSave').click()

        sleep(1)

        crash_message = driver.find_element_by_xpath('/html/body/center[1]/h1').text
        self.assertEqual('413 Request Entity Too Large', crash_message)

    def test_07_add_invalid_format_photo(self):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_id('empPic').click()

        driver.find_element_by_id('empPic').click()
        driver.find_element_by_name('photofile').send_keys('/Users/nazarkruk/Desktop/Orange_HRM/simple_image/login_page.py')
        driver.find_element_by_id('btnSave').click()

        self.wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".message.warning")))
        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.warning"),'Failed to Save: File Type Not Allowed'))


    """

        ======USE THIS TEST CASE AS EXAMPLE OF WILE LOOP=======

        def test_04_add_photograph(self):
            driver = self.driver
            driver.find_element_by_id('txtUsername').send_keys('admin')
            driver.find_element_by_id('txtPassword').send_keys('password')
            driver.find_element_by_id("btnLogin").click()

            sleep(1)

            driver.find_element_by_id('menu_pim_viewMyDetails').click()
            driver.find_element_by_id('empPic').click()

            while True:
                try:
                    button = driver.find_element_by_id('btnDelete')
                    button.click()
                    driver.switch_to.active_element
                    driver.find_element_by_id('btnYes').click()
                    self.wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".message.warning")))
                    self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                                      'Successfully Deleted'))
                except:
                    driver.find_element_by_id('empPic').click()
                    driver.find_element_by_name('photofile').send_keys('/Users/nazarkruk/Desktop/jpg_500kbmb.jpg')
                    driver.find_element_by_id('btnSave').click()
                    self.wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".message.success")))
                    self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                                      'Successfully Uploaded'))

                    break



            else:
                driver.find_element_by_id('empPic').click()
                driver.find_element_by_name('photofile').send_keys('/Users/nazarkruk/Desktop/jpg_500kbmb.jpg')
                driver.find_element_by_id('btnSave').click()
                self.wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".message.success")))
                self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                                  'Successfully Uploaded'))

            button_delete = driver.find_element_by_id('btnDelete').text

            self.assertTrue('Delete', button_delete)

            self.assertTrue(True)
    """


if __name__ == '__main__':
    unittest.main()
