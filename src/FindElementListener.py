from selenium.webdriver.support.events import AbstractEventListener
from robot.api import logger

class FindElementListener(AbstractEventListener):

    def before_find(self, by, value, driver):
        logger.info("Healenium searching for element %s" % value)
        driver.find_element(by, value)  # workaround: need to pre-find the element using plain python so that Healenium can do their magic