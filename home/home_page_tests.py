from pages.home.home_page import HomePage
from pages.home.thank_you_page import ThankYou
from utilities.teststatus import TestStatus
import unittest
import pytest
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class HomePageTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.ty = ThankYou(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_Empty(self):
        self.hp.clickSend()

        nameResult = self.hp.verifyNameError()
        self.ts.mark(nameResult, "Name error appears")
        phoneResult = self.hp.verifyPhoneError()
        self.ts.mark(phoneResult, "Phone error appears")
        emailResult = self.hp.verifyEmailError()
        self.ts.markFinal("Test empty fields", emailResult, "All error message appears")

    @pytest.mark.run(order=2)
    def test_NameOnly(self):
        self.hp.enterName('Daniel')
        self.hp.clickSend()

        phoneResult = self.hp.verifyPhoneError()
        self.ts.mark(phoneResult, "Phone error appears")
        emailResult = self.hp.verifyEmailError()
        self.ts.markFinal("Test only name", emailResult, "Phone and Email error message appears")

    @pytest.mark.run(order=3)
    def test_PhoneOnly(self):
        self.hp.enterPhone('0548040629')
        self.hp.clearName()
        self.hp.clickSend()

        nameResult = self.hp.verifyNameError()
        self.ts.mark(nameResult, "Name error appears")
        emailResult = self.hp.verifyEmailError()
        self.ts.markFinal("Test only Phone", emailResult, "Name and Email error message appears")

    @pytest.mark.run(order=4)
    def test_EmailOnly(self):
        self.hp.enterEmail('danielhan737@gmail.com')
        self.hp.clearPhone()
        self.hp.clickSend()

        phoneResult = self.hp.verifyPhoneError()
        self.ts.mark(phoneResult, "Name error appears")
        nameResult = self.hp.verifyNameError()
        self.ts.markFinal("Test only Email ", nameResult, "Name and Phone error message appears")

    @pytest.mark.run(order=5)
    def test_All(self):
        self.hp.clearName()
        self.hp.enterName('Daniel')
        self.hp.clearPhone()
        self.hp.enterPhone('0548040629')
        self.hp.clearEmail()
        self.hp.enterEmail('danielhan737@gmail.com')
        self.hp.clickSend()
        time.sleep(3)

        thankYouResult = self.ty.verifyCompleteSend()

        self.ts.markFinal("Test all", thankYouResult, "Thank page loaded")
