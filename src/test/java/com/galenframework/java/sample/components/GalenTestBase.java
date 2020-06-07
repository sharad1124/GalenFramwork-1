package com.galenframework.java.sample.components;

import com.galenframework.testng.GalenTestNgTestBase;

import org.apache.commons.io.FileUtils;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.testng.ITestResult;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.AfterTest;
import org.testng.annotations.DataProvider;

import java.util.List;

import static java.util.Arrays.asList;

import java.io.File;

public abstract class GalenTestBase extends GalenTestNgTestBase {

    public static final String ENV_URL = "https://am.ticketmaster.com/ell";

    @Override
    public WebDriver createDriver(Object[] args) {
    	DesiredCapabilities capa = DesiredCapabilities.chrome();
	    ChromeOptions options = new ChromeOptions();
	    options.addArguments("--user-agent= 5Lo1RZau");
	    capa.setCapability(ChromeOptions.CAPABILITY, options);
	    System.setProperty("webdriver.chrome.driver", "/Users/sharadgupta/Downloads/chromedriver 6");
        WebDriver driver = new ChromeDriver(options);

        if (args.length > 0) {
            if (args[0] != null && args[0] instanceof TestDevice) {
                TestDevice device = (TestDevice)args[0];
                if (device.getScreenSize() != null) {
                    driver.manage().window().setSize(device.getScreenSize());
                }
            }
        }
        return driver;
    }

    public void load(String uri) {
    	//DesiredCapabilities capa = DesiredCapabilities.chrome();
        getDriver().get(ENV_URL + uri);
    }

    @DataProvider(name = "devices")
    public Object [][] devices () {
        return new Object[][] {
        	//closing mobile and tab
                //{new TestDevice("mobile", new Dimension(450, 800), asList("mobile"))},
                //{new TestDevice("tablet", new Dimension(750, 800), asList("tablet"))},
                {new TestDevice("desktop", new Dimension(1680, 900), asList("desktop"))}
        };
    }

    public static class TestDevice {
        private final String name;
        private final Dimension screenSize;
        private final List<String> tags;

        public TestDevice(String name, Dimension screenSize, List<String> tags) {
            this.name = name;
            this.screenSize = screenSize;
            this.tags = tags;
        }

        public String getName() {
            return name;
        }

        public Dimension getScreenSize() {
            return screenSize;
        }

        public List<String> getTags() {
            return tags;
        }

        @Override
        public String toString() {
            return String.format("%s %dx%d", name, screenSize.width, screenSize.height);
        }
    }
  
    
    } 
    


