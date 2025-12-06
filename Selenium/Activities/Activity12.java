package activities;

import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class Activity12 {

public static void main(String[] args) {
		// TODO Auto-generated method stub
		WebDriver driver = new FirefoxDriver();
		WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
		
	
		driver.get("https://training-support.net/webelements/dynamic-content");
		System.out.println ("Page title: " + driver.getTitle());
		driver.findElement(By.id("genButton")).click();
		//Finds and clicks button above line
		WebElement wordElement = driver.findElement(By.id("word"));
		wait.until(ExpectedConditions.textToBePresentInElement(wordElement, "release"));
		System.out.println(wordElement.getText());
		driver.quit();
		//can also use if condition
	}

}
