package Pranodayd.CalculatorAPI;

import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.BeforeGroups;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;
import org.testng.Assert;
public class TestAdditionFunctionality 
{
	
	
	Calculator Obj;
	int Result;
	
	@BeforeGroups("RegressionTest")
	public void InitGroup()
	{
		System.out.println("Im in Before Group");
		Obj=new Calculator();
	}
	
	@BeforeClass
	public void Init()
	{
		System.out.println("Im in Before class");
		Obj=new Calculator();
	}
	@BeforeMethod
	public void ReinitialiseResultVar()
	{
		System.out.println("I am in Before Method");
		Result=0;
	}
	@Test(priority=1)
	public void TestAdditionWithPositiveNumbers()
	{
		System.out.println("I am in 1 st TestCase");
		Result=Obj.Addition(10,20);
		Assert.assertEquals(Result, 30,"Addition does not work with positive numbers");
	}
	@Test(priority=3)
	public void TestAdditionWithZeroNumbers()
	{	
		System.out.println("I am in 3rd TestCase");
		Result=Obj.Addition(0, 0);
		Assert.assertEquals(Result, 0,"Addition does not work with zero numbers");
	}

	@Test(priority=2,groups= {"RegressionTest"})
	public void TestAdditionWithOnePositiveOneNegative()
	{
		System.out.println("I am in 2nd TestCase");
		Result=Obj.Addition(10, -8);
		Assert.assertEquals(Result, 2,"Addition does not work with 1 Positive and 1 Negative numbers");
	}
	
	@AfterClass
	public void Teardown()
	{
		System.out.println("I am in After Class");
		Obj=null;
	}
}
