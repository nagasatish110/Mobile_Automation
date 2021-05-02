import unittest

from appium import webdriver
from seleniumpagefactory.Pagefactory import PageFactory
import time
class TheAppPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "ListDemo_button": ('xpath', '//android.widget.TextView[@text="List Demo"]'),
        "Stratocumulus_button": ('xpath', '//android.widget.TextView[@text="Stratocumulus"]'),
        "PopUp_Title": ('id', 'android:id/alertTitle'),
        "popup_ok_button": ('xpath', '//android.widget.Button[@text="OK"]'),
        "element_top":('xpath', '//android.widget.TextView[@text="Check out these clouds"]')
    }

    def navigateToListDemoPage(self):
        self.ListDemo_button.click_button()
    def validate_Stratocumulus(self):
        time.sleep(1)

        self.driver.swipe(75, 500, 75, 0, 800)
        time.sleep(2)
        # self.execute_script(self.Stratocumulus_button.click_button())
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
            "app": "bs://8e4f578ef564c3ba64ea5b410501ced8d2b842ee",

            # Specify device and os_version for testing
            "device": "Google Pixel 3",
            "os_version": "9.0",

            # Set other BrowserStack capabilities
            "project": "First Python project",
            "build": "Python Android",
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