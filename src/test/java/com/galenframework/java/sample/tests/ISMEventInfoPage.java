package com.galenframework.java.sample.tests;

import org.testng.ITestResult;
import org.testng.annotations.AfterTest;
import org.testng.annotations.Test;

import java.io.File;
import java.io.IOException;
import java.util.List;

import org.apache.commons.io.FileUtils;
import org.openqa.selenium.By;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.testng.annotations.Test;

import com.galenframework.java.sample.components.GalenTestBase;
import com.galenframework.java.sample.components.GalenTestBase.TestDevice;

public class ISMEventInfoPage extends GalenTestBase{
	
	 @Test(dataProvider = "devices",priority =1,enabled=true)
	    public void ISM_MAP_Page_onDevice(TestDevice device) throws IOException, Exception {
		 load("/buy");
		 Thread.sleep(5000);
     	getDriver().findElement(By.xpath("//*[name()='path' and contains(@stroke,'currentcol')]")).click();

	    	List <WebElement> list1 = getDriver().findElements(By.xpath("//div[contains(@class,'target-plans__StyledWrapper-sc-1bjozck-0 ktocsc')]//div[contains(@class,'Basestyles__Base-sc-1tnb9cm-0 iKNzhH text text--dark text--primary')]"));
	        System.out.println("NUMBER OF NAM EVENT COUNT >>>>>> : " + list1.size());
	        Thread.sleep(5000);
	        for(int i=0;i<list1.size();i++) {
	      	  String listitem1 = list1.get(i).getText();
	      	  System.out.println("NAM EVENTS ON PLAN SCREEN >>>>>> : " + listitem1);
	        
	      	  
	      	if(listitem1.contentEquals("Event to test ISM GA RES")) {
		          getDriver().findElement(By.xpath("//input[contains(@placeholder,'Search Event Name')]")).sendKeys("ga");
		          System.out.println("click on search");
		          Thread.sleep(10000);
		          System.out.println("try to click on ism ga event");
		          getDriver().findElement(By.xpath("//div[contains(@class,'target-plans__StyledWrapper-sc-1bjozck-0 ktocsc')]//div[1]//div[3]//button[1]")).click();
		          System.out.println("CLICKED on ism ga event");
		          Thread.sleep(10000);
	          
	          break; // adding BREAK to remove this problem stale element reference: element is not attached to the page document
	          }
	        }
	        
	        String url = getDriver().getCurrentUrl();
	        if(url.contains("ism")) {
		        Thread.sleep(10000);
		        System.out.println("User navigate to ISM screen:>>>" + url);
		        getDriver().findElement(By.xpath("//div[@class='styles__StyledCheckInfoButton-sc-1y188te-3 jQWREI']")).click();
		        Thread.sleep(5000);
		        getDriver().findElement(By.xpath("//button[contains(text(),'Got it')]")).click();
		        System.out.println("CLICKED on GOT it button");
		        Thread.sleep(5000);
		        getDriver().findElement(By.xpath("//div[@class='styles__StyledCheckInfoButton-sc-1y188te-3 jQWREI']")).click();
		        Thread.sleep(10000);
		        checkLayout("/specs/ISMEventInfoPage.spec", device.getTags());
	        }
	        else {
	        	System.out.println("unable to find ism in url");
	        	 try{
	        		 // To create reference of TakesScreenshot
	        		 TakesScreenshot screenshot=(TakesScreenshot)driver;
	        		 // Call method to capture screenshot
	        		 File src=screenshot.getScreenshotAs(OutputType.FILE);
	        		 // Copy files to specific location 
	        		 // result.getName() will return name of test case so that screenshot name will be same as test case name
	        		 FileUtils.copyFile(src, new File("/Users/sharadgupta/Documents/automation/ISMFRONTEND/screens" + ".png"));
	        		 System.out.println("Successfully captured a screenshot");
	        		 }catch (Exception e){
	        		 System.out.println("Exception while taking screenshot "+e.getMessage());
	        		 } 
	        }        
	        
	 }
	 
}