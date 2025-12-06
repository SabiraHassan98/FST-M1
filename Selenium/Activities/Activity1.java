package activities;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class Activity1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
				//install the driver object
				WebDriver driver = new FirefoxDriver();
				
				// open the page 
				driver.get("https://training-support.net");
			
				//interact with page
				
				System.out.println ("Page title: " + driver.getTitle());
			
			
			    //Click the about us button
				driver.findElement(By.linkText("About Us")).click();	
			
			    //Print the title of the new page
				System.out.println ("Page title: " + driver.getTitle());
				driver.quit();
				//driver.findElement(By.className(my-8))// can give multiple class names undr card class
				//driver.findElement(By.cssSelector("a.card.svelte-4bhb3l")).click();


	}

}
