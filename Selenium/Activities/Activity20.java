package activities;

import java.time.Duration;

import org.openqa.selenium.Alert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class Activity20 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		WebDriver driver = new FirefoxDriver();
		WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        //Open a new browser to https://training-support.net/webelements/alerts
        driver.get("https://training-support.net/webelements/alerts");
        // Print the title of the page
        System.out.println("Page title: " + driver.getTitle());


        // Find and click the prompt button to open the alert
        driver.findElement(By.id("prompt")).click();

        // Switch focus to the alert
        wait.until(ExpectedConditions.alertIsPresent());
        Alert confirmAlert = driver.switchTo().alert();

        // Print the text in the alert
        String alertText = confirmAlert.getText();
        System.out.println("Text in alert: " + alertText);
        //Type "Awesome!" into the prompt.
        confirmAlert.sendKeys("Awesome!");
        // Close the alert by clicking OK
        confirmAlert.accept();
        System.out.println(driver.findElement(By.id("result")).getText());

        // Can also close the alert by clicking Cancel
        driver.findElement(By.id("prompt")).click();
        wait.until(ExpectedConditions.alertIsPresent());
        confirmAlert.dismiss();

        // Print the message
        System.out.println(driver.findElement(By.id("result")).getText());

        // Close the browser
        driver.quit();
        
	}

}
