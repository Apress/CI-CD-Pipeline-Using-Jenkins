import pytest
import time

from CalculatorWebApp_TestCases.BaseTestCaseClass import BaseTestCase

#To use CLASS-LEVEL fixture mark class with the fixture name using @pytest.mark.usefixtures("CreateLoginPageObj")
@pytest.mark.usefixtures("CreateCalculatorPageObj")
class TestAdditionFunctionality(BaseTestCase):
    calculatorpage=None

    @pytest.mark.RegressionTest
    def testAdditionFunctionalityWithPositiveValues(self,NumberDataProvider):
        logger=self.getLogger()

        logger.info("Got FirstNumber: "+NumberDataProvider["Number1"])
        logger.info("Got SecondNumber: " + NumberDataProvider["Number2"])

        TestAdditionFunctionality.calculatorpage.DoAddition(NumberDataProvider["Number1"],NumberDataProvider["Number2"])
        time.sleep(3)
        AdditionResult=TestAdditionFunctionality.calculatorpage.GetResult()
        logger.info("Actual Result: " + AdditionResult)
        logger.info("Expected Result : " + NumberDataProvider["Result"])
        assert AdditionResult==NumberDataProvider["Result"],"Addition functionality returned wrong result"

    @pytest.mark.SmokeTest
    def testAdditionFunctionalityWithNegativeValues(self):

        logger = self.getLogger()

        logger.info("Got FirstNumber: " + str(-10))
        logger.info("Got SecondNumber: " + str(-20))

        TestAdditionFunctionality.calculatorpage.DoAddition(-10,-20)
        time.sleep(3)
        AdditionResult = TestAdditionFunctionality.calculatorpage.GetResult()
        logger.info("Actual Result: " + AdditionResult)
        logger.info("Expected Result : " + str(-30))
        assert AdditionResult == str(-30), "Addition functionality returned wrong result if negative numbers are sent"
