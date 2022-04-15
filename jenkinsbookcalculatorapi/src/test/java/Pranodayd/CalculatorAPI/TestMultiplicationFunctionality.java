package Pranodayd.CalculatorAPI;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;

import org.testng.Assert;
import org.testng.annotations.*;
public class TestMultiplicationFunctionality 
{
	Calculator Cal;
	int Result;
	@BeforeClass
	public void Init()
	{
		
		Cal=new Calculator();	
	
	}

	@BeforeMethod
	public void ReinitialisingResult()
	{
		Result=0;
		
	}
	@Test(priority=1,dataProvider="ProvidePositiveIntegerValues",groups= {"RegressionTest"})
	public void TestMultiplicationWithPositiveValues(int Number1,int Number2,int ExpectedResult)
	{
		
		Result=Cal.Multiplication(Number1, Number2);
		Assert.assertEquals(Result, ExpectedResult,"Multiplication does not work with positive numbers");
	}

	@DataProvider
	public Object[][] ProvidePositiveIntegerValues()
	{
		/*We want to test functionality with 3 SETs
		 * 
		 * SET1						:1,2,2
		 * SET2						:10,20,200 
		 * SET3						:1000,2000,2000000  
		   SET4						:100,200,20000 	
		 */
	
		
		
		Object [][] SetOfValues=new Object[4][3];
		//This is SET 1:			1,2,2
		
		SetOfValues[0][0]=1;
		SetOfValues[0][1]=2;
		SetOfValues[0][2]=2;
		
		//This is SET 2:		 	10,20,200	
		SetOfValues[1][0]=10;
		SetOfValues[1][1]=20;
		SetOfValues[1][2]=200;
				
		//This is SET 3:		 	1000,2000,2000000
		SetOfValues[2][0]=1000;
		SetOfValues[2][1]=2000;
		SetOfValues[2][2]=2000000;
		
		
		//This is SET 4:		 	1000,2000,2000000
		SetOfValues[3][0]=100;
		SetOfValues[3][1]=200;
		SetOfValues[3][2]=20000;
	
		return SetOfValues;
	}

	
}
