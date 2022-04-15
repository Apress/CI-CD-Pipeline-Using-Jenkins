import time

from selenium import webdriver

from AutomationFramework.Utilities.Utils import Utils
from selenium.webdriver.common.keys import Keys


def StartChromeDriver():
    # WebTest.Driver=webdriver.Chrome(executable_path="D:\\XoriantPythonSeleniumPostmanTraining\\Drivers\\chromedriver.exe")
    from AutomationFramework.WebTest import WebTest
    WebTest.Driver = webdriver.Chrome(
        executable_path=Utils.EnvVars.get("ChromeDriverPath"))
    WebTest.Driver.get("chrome://settings/clearBrowserData")
    time.sleep(5)
    WebTest.Driver.find_element_by_xpath('//settings-ui').send_keys(Keys.ENTER)
    time.sleep(5)
def StartFirefoxDriver():
    pass