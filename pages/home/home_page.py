from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class HomePage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _name_field = "name"
    _error_name_field = "//span[contains(text(),'שדה שם הוא שדה חובה')]"
    _email_field = "email"
    _error_email_field = "//span[contains(text(),'שדה אימייל הוא שדה חובה')]"
    _phone_field = "phone"
    _error_phone_field = "//span[contains(text(),'שדה טלפון הוא שדה חובה')]"
    _send_button_field = '//span[contains(text(),"שליחה")]'

    def enterName(self, name):
        self.sendKeys(name, self._name_field, locatorType="name")

    def clearName(self):
        self.clearKeys(self._name_field, locatorType="name")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType="name")

    def clearEmail(self):
        self.clearKeys(self._email_field, locatorType="name")

    def enterPhone(self, phone):
        self.sendKeys(phone, self._phone_field, locatorType="name")

    def clearPhone(self):
        self.clearKeys(self._phone_field, locatorType="name")

    def clickSend(self):
        self.elementClick(self._send_button_field, locatorType="xpath")

    def verifyNameError(self):
        nameLabel = self.isElementPresent(self._error_name_field, locatorType="xpath")
        return nameLabel

    def verifyPhoneError(self):
        phoneLabel = self.isElementPresent(self._error_phone_field, locatorType="xpath")
        return phoneLabel

    def verifyEmailError(self):
        emailLabel = self.isElementPresent(self._error_email_field, locatorType="xpath")
        return emailLabel
