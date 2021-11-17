# This Listener is a workaround - we need to pre-find the element using plain python so that Healenium can do their magic

from selenium.webdriver.support.events import AbstractEventListener
from robot.api import logger

class FindElementListener(AbstractEventListener):

    def before_find(self, by, value, driver):
        logger.info("Applying listener to pre-find the element %s for Healenium" % value)
        driver.find_element(by, value)