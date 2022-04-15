import csv

from selenium.webdriver.common.by import By
from selenium import webdriver

from AutomationFramework.Switcher import BrowserDriverSwitcher
from AutomationFramework.Utilities.Utils import Utils

class WebTest:
    Driver=None
    def __init__(self):
        #ObjectRepo is a dictionary saving WebElements against the Keys
        self.ObjectRepo={}

    def StartTest(self,BrowserName):
        #StartTest method will start the required browser and will open the URL
        self.__OpenBrowser(BrowserName)
        self.OpenURL()
    #OpenBrowser is a private function defined using __ i.e. double underscore
    def __OpenBrowser(self,BrowserName):
        #This method is responsible for invoking driver/browser according to the
        #browsername recieved as parameter
        #Here we are retrieving function names stored as values
        Func=BrowserDriverSwitcher.get(BrowserName)
        #Calling function,name of which retrieved from dictionary
        Func()
    def OpenURL(self):
        WebTest.Driver.get(Utils.EnvVars.get("ApplicationURL"))

    def CreateObjectRepositoy(self,FileName):
        FilePath=Utils.EnvVars.get("ObjectRepositoryPath")+"\\"+FileName+".csv"
        with open(FilePath) as ObjectRepo:
            csv_reader = csv.reader(ObjectRepo, delimiter=',')
            #In row we will get the content of a row as a tuple
            #Each member of tuple will represent column from that row
            for row in csv_reader:
                #This loop will read each row containing identification data with
                #every iteration
                #e.g. in 1st iteration row=(UserNameField,BY_ID,txtUsername)
                #e.g. in 2nd iteration row=(PasswordField,BY_CSS,input[type='password'])
                #Calling function FindAndReturnElement with Identification stratergy token
                #and locator as arguments.
                #Identification stratergy token is in row[1]
                #Locator is in row[2]
                El=self.FindAndReturnElement(row[1],row[2])
                self.ObjectRepo[row[0]]=El

    def FindAndReturnElement(self,Stratergy,Locator):
        #e.g. Stratergy will have BY_ID and Locator will have userName
        IdentificationData=self.CreateStratergyLocatorTuple(Stratergy,Locator)
        #driver.findElement(By.Id("abcs"))
        #In python driver.find_element() requires a tuple of Identification stratergy and locator
        #i.e. If we want to use id attribute to find element having id set to "userName"
        # then find_element(BY.ID,"userName")
        RequiredElement=WebTest.Driver.find_element(*IdentificationData)
        return RequiredElement

    def CreateStratergyLocatorTuple(self,StratergyToken,Locator):
        StratergyLocatorTuple={
            "BY_ID":(By.ID,Locator),
            "BY_CLASS":(By.CLASS_NAME,Locator),
            "BY_NAME":(By.NAME,Locator),
            "BY_CSS":(By.CSS_SELECTOR,Locator),
            "BY_XPATH":(By.XPATH,Locator),
            "BY_LINKTEXT":(By.LINK_TEXT,Locator)


        }
        return StratergyLocatorTuple.get(StratergyToken)

    def EnterText(self,El,TextTobeEntered):
        El.clear()
        El.send_keys(TextTobeEntered)

    def ClickElement(self,El):
        El.click()
    def GetCurrentURL(self):
        return self.Driver.current_url
    def GetElementText(self,E):
        return E.text
    def GetElementAttribute(self,E,AttributeName):
        return E.get_attribute(AttributeName)