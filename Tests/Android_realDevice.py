import unittest
from seleniumpagefactory.Pagefactory import PageFactory
from appium import webdriver


class TheAppPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "ListDemo_button": ('xpath', '//android.widget.TextView[@text="List Demo"]'),
        "Stratocumulus_button": ('xpath', '//android.widget.TextView[@text="Stratocumulus"]'),
        "PopUp_Title": ('id', 'android:id/alertTitle'),
        "popup_ok_button": ('xpath', '//android.widget.Button[@text="OK"]')
    }
    # This function created to navigate to listdemo page
    def navigateToListDemoPage(self):
        self.ListDemo_button.click_button()
    def validate_Stratocumulus(self):
        self.driver.swipe(75, 500, 75, 0, 800)
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


            "platformName":"Android",
            "platformVersion":"10",
            "deviceName":"52846113",
            "app":"C:\\Users\\TMPL-FA1957\\Desktop\\Kapalan_Assignment\\App\\TheApp-v1.10.0.apk",
            "appActivity":"io.cloudgrey.the_app.MainActivity",

        }
        # Initialize the remote Webdriver using remote URL
        # and desired capabilities defined above
        driver = webdriver.Remote(
            command_executor="http://localhost:4723/wd/hub",
            desired_capabilities=desired_cap
        )
        test_app = TheAppPage(driver)
        test_app.navigateToListDemoPage()
        test_app.validate_Stratocumulus()
        driver.quit()

if __name__ == "__main__":
     unittest.main()