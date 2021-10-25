import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test():

    @pytest.fixture()
    def setup_method(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        self.driver = webdriver.Remote(
            command_executor="http://localhost:8085",
            desired_capabilities=webdriver.DesiredCapabilities.CHROME,
            options=options)

    def teardown_method(self, method):
        self.driver.quit()

    def test(self, setup_method):
        self.driver.get('https://sha-test-app.herokuapp.com/')
        self.driver.find_element(By.XPATH, "//button[contains(@class,'default-btn')]").click()
        self.driver.switch_to_alert().accept()
        self.driver.find_element(By.ID, "markup-generation-button").click()
        self.driver.find_element(By.XPATH, "//button[contains(@class,'default-btn')]").click()  # should be healed
        self.driver.switch_to_alert().accept()