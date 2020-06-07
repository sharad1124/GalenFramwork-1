package com.galenframework.java.sample.tests;

import org.testng.annotations.Test;
import java.awt.Window;
import java.io.IOException;
import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.testng.annotations.Test;

import com.galenframework.java.sample.components.GalenTestBase;
import com.galenframework.java.sample.components.GalenTestBase.TestDevice;


public class ISMPurchasePage extends GalenTestBase {  

    @Test(dataProvider = "devices",priority =1,enabled=true)
    public void ISM_Landing_Page_onDevice(TestDevice device) throws IOException, Exception {
    	load("/");
    	//checkLayout("/specs/ISMPurchasePage.spec", device.getTags());
    	List <WebElement> list = getDriver().findElements(By.xpath("//nav[@id='block-iom-main-navigation-block']/ul/li"));
        System.out.println("NAM HEADER LINKS COUNT >>>>>> : " + list.size());
        Thread.sleep(5000);
    
        //if heading equal to 0 direct click on the BUY button  if(list.size() == 0)
        if(list.isEmpty()) {	
        	load("/buy");
        	System.out.println("<<<<<<<<<<list is Empty>>>>>>>" + list.isEmpty());
        	System.out.println("buy url load");
        	Thread.sleep(5000);
        	getDriver().findElement(By.xpath("//*[name()='path' and contains(@stroke,'currentcol')]")).click();
        	System.out.println("click on layout button");
        	//if heading is exist and user click on the buy link
        } else {
            
            for(int i=0;i<list.size();i++) {
          	  
          	  String listitem = list.get(i).getText();
          	  System.out.println("NAM HEADER LINKS ARE >>>>>> : " + listitem);
          	if(listitem.contains("buy")) {
          		Thread.sleep(5000);
      		  list.get(i).click();
          	getDriver().findElement(By.xpath("//*[name()='path' and contains(@stroke,'currentcol')]")).click();
      		System.out.println("NAM HEADER LINKS FOUND BUY TEXT >>>>>>");
      		break;
          	}
            }
        }
        Thread.sleep(10000);
        checkLayout("/specs/ISMPurchasePage.spec", device.getTags());  
   
    }

}