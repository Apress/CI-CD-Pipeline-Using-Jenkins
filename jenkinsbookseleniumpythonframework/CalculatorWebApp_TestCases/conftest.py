#In tnis file we can write COMMON/reusable fixtures which we would like to use
#across multiple testcase files

import pytest

from AutomationFramework.Utilities.Utils import Utils
from CalculatorWebApp_Pages.CalcualatorPage import CalculatorPage
calculatorpage=None

#@pytest.fixture(params=[{"UserName":"Admin","Password":"","Error":"User name can not be empty"}])
@pytest.fixture(params=Utils.ReadNumberTestData())
def NumberDataProvider(request):
    #request.param returns item of list with each iteration
    return request.param

#Mentioning scope of fixture makes it work like BeforeClass from TestNG
@pytest.fixture(scope="class")
def CreateCalculatorPageObj(request):
    global calculatorpage
    calculatorpage=CalculatorPage("Chrome")
    request.cls.calculatorpage=calculatorpage
    #We can get the reference of class requesting this fixture using request.cls
    #loginpage object we want to be passed to loginpage class variable of testcase class
    #request.cls.loginpage=loginpage will set loginpage variable from Testcase class
    #to object of loginpage PAGECLASS
    #return loginpage

@pytest.fixture(autouse=True)
def ClearResultField():
    calculatorpage.ClearResult()