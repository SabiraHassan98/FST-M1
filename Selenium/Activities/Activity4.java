package activities;

import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.Color;

public class Activity4 {

	public static void main(String[] args) {
		// Open a new browser to https://training-support.net/webelements/target-practice
		WebDriver driver = new FirefoxDriver();
		driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
				
				//Open a new browser to https://training-support.net/webelements/login-form/
				driver.get("https://training-support.net/webelements/target-practice");
				//Get the title of the page and print it to the console.
				System.out.println ("Page title: " + driver.getTitle());
				
				//Find the 3rd header on the page and print it's text to the console.
				String thirdelement = driver.findElement(By.xpath("//h3[contains(text(), '#3')]")).getText();
				System.out.println(thirdelement);
				//Find the 5th header on the page and print it's color.
				
				Color fifthHeaderColor = Color.fromString(driver.findElement(By.xpath("//h5[contains(text(), '#5')]")).getCssValue("color"));
				System.out.println("the RGB color : " + fifthHeaderColor.asRgb());
				System.out.println("the HEX color : " + fifthHeaderColor.asHex());
				//using any other locator:
				//Find the purple button and print all it's classes.
				String purple = driver.findElement(By.xpath("//button[contains(text(), 'Purple')]")).getDomAttribute("Class");
				System.out.println(purple);
				//Find the slate button and print it's text.
				String Slatebutton = driver.findElement(By.xpath("//button[contains(@class, 'slate')]")).getText();
				System.out.println(Slatebutton);
				
				//Close the browser.
				driver.quit();
	}

}
