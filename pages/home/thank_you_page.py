from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class ThankYou(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _thank_you_field = "//span[contains(text(),'תודה!')]"

    def verifyCompleteSend(self):
        thankYouLabel = self.isElementPresent(self._thank_you_field, locatorType="xpath")
        return thankYouLabel

    def verifyTitle(self):
        if "" in self.getTitle():
            return True
        else:
            return False
