from AutomationFramework.WebTest import WebTest


class BasePage:

    def __init__(self):
        #We are creating object of WebTest framework class,in which all
        #low-level framework APIs are implemented
        self.T=WebTest()

    def GetPageURL(self):
        return self.T.GetCurrentURL()