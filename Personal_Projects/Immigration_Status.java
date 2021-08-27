/*
 * First Project 
 * 	-Immigration Current Processing Time-
 * 	1. Goes to the USCIS web site
 * 	2. Selects specified Form #
 * 	3. Selects specified field office
 * 	4. Locates the the current processing case date and prints it out
 * 	5. Windows Closes
 */

package com.learning;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class Immigration_Status {

	public static void main(String[] args) {
		
		System.setProperty("webdriver.chrome.driver", "C:\\Users\\mario\\Downloads\\chromedriver.exe");
		WebDriver driver = new ChromeDriver(); 
		WebDriverWait wait = new WebDriverWait(driver, 5);
		
		System.out.println("Opening windows to Immigration site!");
		driver.manage().window().maximize();
		//English// "https://egov.uscis.gov/processing-times
		//Spanish// https://egov.uscis.gov/processing-times/es
	
		
		driver.get("https://egov.uscis.gov/processing-times/");
		driver.findElement(By.xpath("//*[@id=\'selectForm\']/option[7]")).click();
		wait.until(ExpectedConditions.elementToBeClickable(By.cssSelector("#officeOrCenter > option:nth-child(2)"))).click();
		// Thought about doing it as stated below but couldn't get it to work that way. Had to take a more direct route.
		//driver.findElement(By.cssSelector("#officeOrCenter")).click();
		//driver.findElement(By.xpath("//*[@id=\'officeOrCenter\']/option[2]")).click();
		driver.findElement(By.cssSelector("#getProcTimes")).click();
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[@id=\'inquiryDateHeader\']/p")));
		
		//String currentDate = driver.findElement(By.cssSelector("#resultList > li:nth-child(2)")).getText();
		//Currently going with cssSelector #date which is not reliable but will check back and fix it when I learn more.
		String currentDate = driver.findElement(By.cssSelector("#date")).getText();
		System.out.println(currentDate);
		driver.close();
		
		
		
		

		
		
	}

}
