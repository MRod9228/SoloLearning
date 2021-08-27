/*
 * First Project -- [Created for a family member that is not very good with computers and asks me to check constantly.]
 * 	-Immigration I-130 FORM Current Processing Time-
 * 	1. Goes to the USCIS web site
 * 	2. Selects specified Form #
 * 	3. Selects specified field office
 * 	4. Locates the the current processing case date and prints it out
 * 	
 */

package com.learning;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.util.Scanner;


public class Immigration_Status {

	static String language;
	public static void main(String[] args) throws InterruptedException {
		
		System.setProperty("webdriver.chrome.driver", "C:\\Users\\**YOUR-USER-HERE**\\Downloads\\chromedriver.exe");
		Scanner scan = new Scanner(System.in);
		
	
		System.out.println("Spanish or English? ");
		String language = scan.nextLine();
		System.out.println("You selected: "+ language +"!");
		WebDriver driver = new ChromeDriver(); 
		WebDriverWait wait = new WebDriverWait(driver, 5);
		if (language.equals("Spanish")) {
			System.out.println("Pulling the information...");
			driver.get("https://egov.uscis.gov/processing-times/es");	
		} else if (language.equals("English")) {
			System.out.println("Pulling the information...");
			driver.get("https://egov.uscis.gov/processing-times");
		} else{System.out.println("Something went wrong");};
		
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[@id=\'selectForm\']/option[7]")));
		driver.findElement(By.xpath("//*[@id=\'selectForm\']/option[7]")).click();
		wait.until(ExpectedConditions.elementToBeClickable(By.cssSelector("#officeOrCenter > option:nth-child(2)"))).click();
		driver.findElement(By.cssSelector("#getProcTimes")).click();
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[@id=\'inquiryDateHeader\']/p")));
		
		String currentDate = driver.findElement(By.cssSelector("#date")).getText();
		if (language.equals("English")) {
			System.out.println("Currently processing receipts from: " +currentDate);	
		} else if (language.equals("Spanish")) {
			System.out.println("Actualmente estan processando el dia: " +currentDate);
		}
		driver.close();
		for (int i = 5; i>=1;i--) {
			System.out.println("Closing in: "+ i);
			Thread.sleep(1000);
		}
		System.exit(0);
		
		
		
		
		
		
		
		

		
		
	}

}
