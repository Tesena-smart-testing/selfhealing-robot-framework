# this is an extension of SeleniumLibrary to enhance it by adding Healenium features
# more info about extending SeleniumLibrary can be found at:
# https://github.com/robotframework/SeleniumLibrary/blob/master/docs/extending/extending.rst

ROBOT_LIBRARY_SCOPE = 'SUITE'
from robot.api.deco import keyword
from SeleniumLibrary import SeleniumLibrary
from selenium import webdriver
from SeleniumLibrary.keywords import BrowserManagementKeywords
from src.FindElementListener import FindElementListener
from selenium.webdriver.support.events import EventFiringWebDriver

class HealeniumLibrary(SeleniumLibrary):

    @keyword
    def open_selfhealing_browser(self, url):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        self.healeniumdriver = webdriver.Remote(
            command_executor="http://localhost:8085",
            desired_capabilities=webdriver.DesiredCapabilities.CHROME,
            options=options)

        # register FindElementListener
        self.healeniumdriver = EventFiringWebDriver(self.healeniumdriver, FindElementListener())

        # register WebDriver in SeleniumLibrary of Robot Framework
        browser_management = BrowserManagementKeywords(self)
        browser_management.ctx.register_driver(self.healeniumdriver, "healeniumdriver")

        # navigate to the given url
        browser_management.go_to(url)

    pass  # very important - it inherits the rest of the methods and attributes from the parent class