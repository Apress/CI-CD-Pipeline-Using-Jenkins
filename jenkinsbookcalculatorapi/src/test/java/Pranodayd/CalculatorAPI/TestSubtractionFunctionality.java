package Pranodayd.CalculatorAPI;

import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import org.testng.annotations.BeforeMethod;
public class TestSubtractionFunctionality 
{
	Calculator Cal;
	int Result;
	@BeforeClass
	public void Init()
	{
		Cal=new Calculator();
		
	}
	
	@BeforeMethod
	public void ReInitialise()
	{
		Result=0;
	}
	
	@Test(priority=1,groups= {"RegressionTest"})
	public void TestSubtractionWithPositiveNumbers()
	{
		
		Result=Cal.Subtraction(50, 10);
		Assert.assertEquals(Result, 40,"Subtraction does not work with Positive Numbers");
	}
	
	@Test(priority=2)
	public void TestSubtractionWith1Positive1NegativeNumbers()
	{
		
		Result=Cal.Subtraction(50, -10);
		Assert.assertEquals(Result, 60,"Subtraction does not work with 1 Positive and 1 Negative Numbers");
	}
	
	
	@AfterClass
	public void Teardown()
	{
		Cal=null;
	}
}
