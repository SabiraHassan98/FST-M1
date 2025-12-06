package activities;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class activity2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		WebDriver driver = new FirefoxDriver();
		
		//Open a new browser to https://training-support.net/webelements/login-form/
		driver.get("https://training-support.net/webelements/login-form/");
		//Get the title of the page and print it to the console.
		System.out.println ("Page title: " + driver.getTitle());
		//Find the user name field using any locator and enter "admin" into it.
		driver.findElement(By.xpath("//input[@id='username']")).sendKeys("admin");
		//Find the password field using any locator and enter "password" into it.
		driver.findElement(By.xpath("//input[@id='password']")).sendKeys("password");
		//Find the "Log in" button using any locator and click it.
		driver.findElement(By.xpath("//button[contains(text(), 'Submit')]")).click();
		System.out.println ("Page title: " + driver.getTitle());
			
		String message = driver.findElement(By.xpath("//h1[contains(text(),'Success!)]")).getText();
		System.out.println(message);
			
		//driver.quit();	
			//Close the browser
	



	}

}
