from AutomationFramework.Utilities.Utils import Utils
from CalculatorWebApp_Pages.BasePage import BasePage


class CalculatorPage(BasePage):
    def __init__(self,BrowserName):
        #Here we are calling BasePage constructor
        super().__init__()
        Utils.InitialiseEnvVars()
        self.T.StartTest(BrowserName)
        self.T.CreateObjectRepositoy("CalculatorPage")

    def DoAddition(self,Number1,Number2):
        if(isinstance(Number1,int)):
            Number1=str(Number1)
        for Digit in Number1:
            Locator="input[value=\"{}\"]".format(Digit)
            NumberButton=self.T.FindAndReturnElement("BY_CSS",Locator)
            self.T.ClickElement(NumberButton)

        self.T.ClickElement(self.T.ObjectRepo["AddButton"])

        if (isinstance(Number2, int)):
            Number2 = str(Number2)

        for Digit in Number2:
            #NumberButton=self.T.FindAndReturnElement("BY_CSS","//input[value='"+Digit+"']")
            Locator = "input[value='{}']".format(Digit)
            NumberButton = self.T.FindAndReturnElement("BY_CSS", Locator)
            self.T.ClickElement(NumberButton)

        self.T.ClickElement(self.T.ObjectRepo["EqualToButton"])



    def DoSubtraction(self,Number1,Number2):
        if (isinstance(Number1, int)):
            Number1 = str(Number1)
        for Digit in Number1:
            Locator = "input[value=\"{}\"]".format(Digit)
            NumberButton = self.T.FindAndReturnElement("BY_CSS", Locator)
            self.T.ClickElement(NumberButton)

        self.T.ClickElement(self.T.ObjectRepo["MinusButton"])

        if (isinstance(Number2, int)):
            Number2 = str(Number2)

        for Digit in Number2:
            # NumberButton=self.T.FindAndReturnElement("BY_CSS","//input[value='"+Digit+"']")
            Locator = "input[value='{}']".format(Digit)
            NumberButton = self.T.FindAndReturnElement("BY_CSS", Locator)
            self.T.ClickElement(NumberButton)

        self.T.ClickElement(self.T.ObjectRepo["EqualToButton"])


    def GetResult(self):
        ResultElement=self.T.ObjectRepo["ResultField"]
        ResultValue=self.T.GetElementAttribute(ResultElement,"value")
        return ResultValue

    def ClearResult(self):
        self.T.ClickElement(self.T.ObjectRepo["ClearButton"])