package com.galenframework.java.sample.tests;

import org.testng.annotations.Test;
import java.io.IOException;
import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.testng.annotations.Test;

import com.galenframework.java.sample.components.GalenTestBase;
import com.galenframework.java.sample.components.GalenTestBase.TestDevice;

public class ISMMapPage extends GalenTestBase{
	ISMPurchasePage ismpurchagepage;
	
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
	          break; 
	          
	          
	           // adding BREAK to remove this problem stale element reference: element is not attached to the page document
	          }

	        }
	        
	        Thread.sleep(10000);
	     	getDriver().findElement(By.xpath("//*[@id=\"appContainer\"]/div/div[2]")).click();
	     	Thread.sleep(5000);
	     	//Working fine for price
	    	List <WebElement> price = getDriver().findElements(By.xpath("//div//div[contains(@class,'common-price-1RMd7')]"));
	        System.out.println("AMOUNT ON RIGHT RAIL >>>>>> : " + price.size());
	        Thread.sleep(5000);
	        for(int i=0;i<price.size();i++) {
		      	  String amount = price.get(i).getText();
		      	  System.out.println("AMOUNT ON RIGHT RAIL >>>>>> : " + amount);
	        }
	        
//	     	// working fine for all details
//	    	List <WebElement> price = getDriver().findElements(By.xpath("//div[contains(@class,'right-list-view-rightRailList-1viEC hasDataList')]"));
//	        System.out.println("AMOUNT ON RIGHT RAIL >>>>>> : " + price.size());
//	        Thread.sleep(5000);
//	        for(int i=0;i<price.size();i++) {
//		      	  String amount = price.get(i).getText();
//		      	  System.out.println("AMOUNT ON RIGHT RAIL >>>>>> : " + amount);
//	        }
	        
	    	List <WebElement> ticketcount = getDriver().findElements(By.xpath("//div//span[@class='right-list-view-popupFooterRightTicket-3GFrB']//span[@class='right-list-view-ticketText-9LLdg']"));
	        System.out.println("NUMBER OF TICKETS ON RIGHT RAIL >>>>>> : " + ticketcount.size());
	        Thread.sleep(5000);
	        for(int i=0;i<ticketcount.size();i++) {
		      	  String numberofcount = ticketcount.get(i).getText();
		      	  System.out.println("TICKET COUNT ON RIGHT RAIL >>>>>> : " + numberofcount);
	        }
	        
	        Thread.sleep(5000);
	        checkLayout("/specs/ISMMapPage.spec", device.getTags());
	        }

	        
	 }
	
	 


