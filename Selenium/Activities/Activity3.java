package activities;

import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class Activity3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
WebDriver driver = new FirefoxDriver();
driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
		
		//Open a new browser to https://training-support.net/webelements/login-form/
		driver.get("https://training-support.net/webelements/login-form/");
		//Get the title of the page and print it to the console.
		System.out.println ("Page title: " + driver.getTitle());
		//Find the user name field using any locator and enter "admin" into it.
		driver.findElement(By.xpath("//input[@placeholder='Username']")).sendKeys("admin");
		//Find the password field using any locator and enter "password" into it.
		driver.findElement(By.xpath("//input[@name='password']")).sendKeys("password");
        // Find the login button and click it
        driver.findElement(By.xpath("//button[text()='Submit']")).click();

     // Print the confirmation message
        String message = driver.findElement(By.xpath("//h1[contains(text(), 'Success')]")).getText();
        System.out.println(message);	
			
		driver.quit();	

	}

}
