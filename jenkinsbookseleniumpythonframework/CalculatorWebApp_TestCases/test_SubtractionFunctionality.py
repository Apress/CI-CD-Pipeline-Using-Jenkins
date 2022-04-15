import time

import pytest


from CalculatorWebApp_TestCases.BaseTestCaseClass import BaseTestCase


@pytest.mark.usefixtures("CreateCalculatorPageObj")
class TestSubtractionFunctionality(BaseTestCase):
    calculatorpage = None
    @pytest.mark.SmokeTest
    def testSubtractionFunctionalityWithPositiveValues(self):
        logger = self.getLogger()
        TestSubtractionFunctionality.calculatorpage.DoSubtraction(100,80)
        time.sleep(3)
        SubtractionResult = TestSubtractionFunctionality.calculatorpage.GetResult()
        logger.info("Actual Result: " + SubtractionResult)
        logger.info("Expected Result : " + str(20))
        assert SubtractionResult == str(20), "Subtraction functionality returned wrong result"

    @pytest.mark.RegressionTest
    def testSubtractionFunctionalityWithOnePositiveAndOneNegativeValues(self):
            logger = self.getLogger()

            logger.info("Got FirstNumber: " + str(-10))
            logger.info("Got SecondNumber: " + str(-20))

            TestSubtractionFunctionality.calculatorpage.DoSubtraction(-10,20)
            time.sleep(3)
            SubtractionResult = TestSubtractionFunctionality.calculatorpage.GetResult()
            logger.info("Actual Result: " + str(SubtractionResult))
            logger.info("Expected Result : " + str(-30))
            assert SubtractionResult == str(-30), "Subtraction functionality returned wrong result if negative numbers are sent"
