package activities;


import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.interactions.Actions;

public class Activity9 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//Open a new browser to https://training-support.net/webelements/keyboard-events
		WebDriver driver = new FirefoxDriver();
		//Get the title of the page and print it to the console.
		driver.get("https://training-support.net/webelements/keyboard-events");
		System.out.println(driver.getTitle());
		
		Actions builder = new Actions(driver);
		
		//On the page, type out a string from the Selenium script to show on the page
		builder.sendKeys("this is coming from selenium ").sendKeys(Keys.RETURN).build().perform();
		
		//sendKeys(Keys.RETURN).build().perform();
			
		//Print the message to the console.
		String text = driver.findElement(By.cssSelector("h1.mt-3")).getText();
		System.out.println(text);
		//Close the browser
		driver.quit();

	}

}
