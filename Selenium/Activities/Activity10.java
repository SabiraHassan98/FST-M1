package activities;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.interactions.Actions;

public class Activity10 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// Initialize the Firefox driver
        WebDriver driver = new FirefoxDriver();
        // Create the Actions object
        Actions builder = new Actions(driver);

        // Open the page
        driver.get("https://training-support.net/webelements/drag-drop");
        // Print the title of the page
        System.out.println("Page title: " + driver.getTitle());
        
        WebElement football = driver.findElement(By.id("ball"));
        WebElement Dropzone1 = driver.findElement(By.id("dropzone1"));
        WebElement Dropzone2 = driver.findElement(By.id("dropzone2"));
        
        builder.clickAndHold(football).moveToElement(Dropzone1).pause(3000).release().build().perform();
        if(Dropzone1.findElement(By.className("dropzone-text")).getText().equals("Dropped!")) {
        	System.out.println("The football is in Dropzone1");
        }
        
        builder.dragAndDrop(football, Dropzone2).pause(3000).build().perform();
        if(Dropzone2.findElement(By.className("dropzone-text")).getText().equals("Dropped!")) {
        	System.out.println("The football is in Dropzone2");
        }
        driver.quit();

	}

}
