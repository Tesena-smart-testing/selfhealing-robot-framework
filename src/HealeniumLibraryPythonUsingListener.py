# this is an extension of SeleniumLibrary to enhance it by adding Healenium features
# more info about extending SeleniumLibrary can be found at https://github.com/robotframework/SeleniumLibrary/blob/master/docs/extending/extending.rst
from SeleniumLibrary import SeleniumLibrary

ROBOT_LIBRARY_SCOPE = 'SUITE'
from selenium import webdriver
from SeleniumLibrary.keywords import BrowserManagementKeywords
from robot.api.deco import keyword
from src.FindElementListener import FindElementListener

from selenium.webdriver.support.events import EventFiringWebDriver

class HealeniumLibraryPythonUsingListener(SeleniumLibrary):

    @keyword
    def open_selfhealing_browser(self, url):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        self.healeniumdriver = webdriver.Remote(
            command_executor="http://localhost:8085",
            desired_capabilities=webdriver.DesiredCapabilities.CHROME,
            options=options)

        self.healeniumdriver = EventFiringWebDriver(self.healeniumdriver, FindElementListener())

        # register webdriver in seleniumlibrary of robot framework
        browser_management = BrowserManagementKeywords(self)
        browser_management.ctx.register_driver(self.healeniumdriver, "healeniumdriver")

        # go to the given url
        browser_management.go_to(url)

        # python test
        # self.healeniumdriver.find_element(By.XPATH, "//button[contains(@class,'default-btn')]").click()
        # self.healeniumdriver.switch_to.alert.accept()
        # self.healeniumdriver.find_element(By.ID, "markup-generation-button").click()
        # self.healeniumdriver.find_element(By.XPATH, "//button[contains(@class,'default-btn')]").click()  # should be healed
        # self.healeniumdriver.switch_to.alert.accept()

    pass  # very important - it inherits the rest of the methods and attributes from the parent class