package activities;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

public class Activity7 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//Open a new browser to https://training-support.net/webelements/dynamic-controls
		WebDriver driver= new FirefoxDriver();
		driver.get("https://training-support.net/webelements/dynamic-controls");
		
		//Get the title of the page and print it to the console.
		System.out.println("page title is : "+ driver.getTitle());
		//On the page, perform:Find the text field.
		WebElement textField = driver.findElement(By.id("textInput"));
		//Check if the text field is enabled and print it.
		System.out.println("The text field is enabled : "+ textField.isEnabled());
		//Click the "Enable Input" button to enable the input field.
		driver.findElement(By.id("textInputButton")).click();
		//Check if the text field is enabled again and print it.
		System.out.println("The text field is enabled : "+ textField.isEnabled());
		//Close the browser.
		driver.quit();

	}

}
