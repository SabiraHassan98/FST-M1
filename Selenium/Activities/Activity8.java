package activities;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.interactions.Actions;

public class Activity8 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		WebDriver driver = new FirefoxDriver();
		//create action object
		Actions builder = new Actions(driver);
		// Open the page
        driver.get("https://training-support.net/webelements/mouse-events");
        // Print the title of the page
        System.out.println("Page title: " + driver.getTitle());
        
        // Find the elements that can be clicked
        WebElement cargoLock = driver.findElement(By.xpath("//h1[text()='Cargo.lock']"));
        WebElement cargoToml = driver.findElement(By.xpath("//h1[text()='Cargo.toml']"));
        WebElement srcButton = driver.findElement(By.xpath("//h1[text()='src']"));
        WebElement targetButton = driver.findElement(By.xpath("//h1[text()='target']"));
        //Left click on the Cargo.lock button, move the cursor to the Cargo.toml button and then click it. 
        //Print the confirmation text at the end of the sequence.
        
        builder.click(cargoLock).pause(3000).moveToElement(cargoToml).pause(2000).click(cargoToml).pause(1000).build().perform();
        
        String confirmText = driver.findElement(By.id("result")).getText();
        System.out.println(confirmText);
        
        //Double click on the src button. Then right click on the target button and select open.
        //Print the confirmation text at the end of the sequence.
        builder.doubleClick(srcButton).pause(2000).contextClick(targetButton).pause(1000).build().perform();
        builder.click(driver.findElement(By.xpath("//div[@id='menu']/div/ul/li[1]"))).pause(1000).build().perform();
        
        String textMsg = driver.findElement(By.id("result")).getText();
        System.out.println(textMsg);
        driver.close();
         
        
       

       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
		
       
		
		
		

	}

}
