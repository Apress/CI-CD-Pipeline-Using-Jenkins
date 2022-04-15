from selenium import webdriver

from AutomationFramework.InvokeDrivers import StartChromeDriver, StartFirefoxDriver

BrowserDriverSwitcher = {
    "Chrome": StartChromeDriver,
    "Firefox":StartFirefoxDriver

}
