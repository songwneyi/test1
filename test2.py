import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement

url = "https://10.155.0.135:31757/#/login"
class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(url)
    def test_case01(self):
        self.driver.maximize_window()
        self.driver.find_element_by_xpath('//*[@id="operatorCode"]').send_keys("135roc")
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="pwd"]').send_keys("111111")
        sleep(2)
        self.driver.find_element_by_xpath("//button[@class='login-form-button ant-btn ant-btn-default ant-btn-lg']").click()
        sleep(2)







    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
