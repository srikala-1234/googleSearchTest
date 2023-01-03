from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    def test_search_automationstepbystep(self):
        self.driver.get("https://google.com")
        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys("Automation step by step")
        self.driver.find_element(By.XPATH, "//input[@name='btnK']").click()
    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()
        print("Test completed successfully")

if __name__ == '__main__':
    unittest.main()

