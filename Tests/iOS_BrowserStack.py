import unittest

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from seleniumpagefactory import PageFactory


class TheAppPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "ListDemo_button": ('xpath', ''),
        "Stratocumulus_button": ('xpath', ''),
        "PopUp_Title": ('id', ''),
        "popup_ok_button": ('xpath', '')
    }

    def navigateToListDemoPage(self):
        self.ListDemo_button.click_button()

    def validate_Stratocumulus(self):
        self.execute_script(self.Stratocumulus_button.click_button())
        self.Stratocumulus_button.click_button()
        title = self.PopUp_Title.get_text()
        print(title)
        if title == "Your Cloud Selection":
            print("Popup is displayed")
            self.popup_ok_button.click_button()
        else:
            ("Popup is not displayed")


class TheAppTest(unittest.TestCase):
    def test_navigation(self):
        desired_cap = {
            # Set your access credentials
            "browserstack.user": "testone_kISrL3",
            "browserstack.key": "icAkeCqqCjzzaVqJvDLa",

            # Set URL of the application under test
            "app": "",

            # Specify device and os_version for testing
            "device": "iPhone XS",
            "os_version": "12",

            # Set other BrowserStack capabilities
            "project": "First Python project",
            "build": "Python iOS",
            "name": "first_test"
        }

        # Initialize the remote Webdriver using BrowserStack remote URL
        # and desired capabilities defined above
        driver = webdriver.Remote(
            command_executor="http://hub-cloud.browserstack.com/wd/hub",
            desired_capabilities=desired_cap
        )
        test_app = TheAppPage(driver)
        test_app.navigateToListDemoPage()
        test_app.validate_Stratocumulus()

        # Invoke driver.quit() after the test is done to indicate that the test is completed.
        driver.quit()

if __name__ == "__main__":
     unittest.main()