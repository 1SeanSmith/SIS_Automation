import unittest
import time
from config import driver,reportAddress,projectName,url, username, password, password_wrong


class SearchClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def class_search(self):

        # Navigate to the URL and insert username, password
        self.driver.get(url)
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("cu-privacy-notice-button").click()

        # Click on Submit button
        element = self.driver.find_element_by_name("submit")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        time.sleep(5)

        # Verify user is able to Student Information System page
        message = self.driver.find_element_by_xpath("//*[@id='app-content']/mat-toolbar[3]/div/div[1]/span/a").text
        self.assertEqual(message, "Student Information System", "Login Failed")

        # Click on Student Groups card
        self.driver.find_element_by_xpath("//mat-card-title[normalize-space()='Student Groups']").click()
        self.driver.implicitly_wait(10)

        # Verify that user is navigated to Group Listing page.
        title = self.driver.find_element_by_xpath("//h1[normalize-space()='Group Listings']").text
        self.driver.implicitly_wait(10)
        self.assertEqual(title, "Group Listings")

        # Verify that user is able to search data under Search under Keyword field
        self.driver.find_element_by_xpath("//input[@arr.aria-label='Filter by keyword']").send_keys("april")
        group_name = self.driver.find_element_by_xpath("//div[@class='results-container']//mat-card//span[@class='groupDiscription']").text
        name = str(group_name)
        flag = name.__contains__("april")
        self.assertTrue(flag)

        self.driver.find_element_by_css_selector("svg[data-icon='list-ul']").click()





    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Login Test Completed")
