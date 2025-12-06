package activities;

import java.time.Duration;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class Activity15 {
	
	public static void main(String[] args) {
		WebDriver driver = new FirefoxDriver();
		 WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
		
		//Open a new browser to https://training-support.net/webelements/dynamic-attributes
		driver.get("https://training-support.net/webelements/dynamic-attributes");
		//Get the title of the page and print it to the console.
		System.out.println(driver.getTitle());
		//Find the input fields and type in the required data in the fields.
		WebElement user = driver.findElement(By.xpath("//input[starts-with(@id, 'full-name-')]"));
		WebElement email = driver.findElement(By.xpath("//input[contains(@id, '-email')]"));
		WebElement date = driver.findElement(By.xpath("//input[contains(@name, '-event-date-')]"));
		WebElement details = driver.findElement(By.xpath("//textarea[contains(@id, '-additional-details-')]"));
		user.sendKeys("Sabira Hassan");
		email.sendKeys("Sabira.H@gmail.com");
		date.sendKeys("2025-11-30");
		details.sendKeys("event details");
		//Wait for success message to appear and print it to the console.
		driver.findElement(By.xpath("//button[contains(text(), 'Submit')]")).click();
		String msg= wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("action-confirmation"))).getText();
		System.out.println(msg);
		//Close the browser.
		driver.quit();
		
		
	}

}
