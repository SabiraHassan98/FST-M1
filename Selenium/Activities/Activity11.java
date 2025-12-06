package activities;

import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class Activity11 {
	public static void main(String[] args) {
		WebDriver driver = new FirefoxDriver();
		WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
		//Open a new browser to https://training-support.net/webelements/dynamic-controls
		driver.get("https://training-support.net/webelements/dynamic-controls");
		//Get the title of the page and print it to the console.
		System.out.println("The page title is : "+ driver.getTitle());
		//On the page, perform:
		//Find the checkbox on the page.
		WebElement Checkbox = driver.findElement(By.id("checkbox"));
		System.out.println("The checkbox is visible: " + Checkbox.isDisplayed());
		
		//Click the "Toggle Checkbox" button to remove the checkbox.
		WebElement Togglebox= driver.findElement(By.xpath("//button[text()='Toggle Checkbox']"));
		Togglebox.click();
		//Wait for the checkbox to disappear.
		wait.until(ExpectedConditions.invisibilityOf(Checkbox));
		System.out.println("The checkbox is visible: " + Checkbox.isDisplayed());
		//Toggle the checkbox again.
		Togglebox.click();
		//Wait for it appear and then select it.
		wait.until(ExpectedConditions.elementToBeClickable(Checkbox)).click();
		System.out.println("The checkbox is selected: " + Checkbox.isSelected());
		//Close the browser.
		driver.quit();
		
		
	}

}
