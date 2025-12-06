from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Firefox() as driver:
    #Open a new browser to https://training-support.net/webelements/login-form/
    driver.get("https://training-support.net/webelements/login-form/")
    #Get the title of the page and print it to the console.
    print("The page title is: " + driver.title)
    #Find the username field using any locator and enter "admin" into it.
    # Find the username field
    username = driver.find_element(By.XPATH, "//input[@id='username']")
    # Find the password field
    password = driver.find_element(By.XPATH, "//input[@id='password']")

    # Enter the given credentials
    # Enter username
    username.send_keys("admin")
    # Enter password
    password.send_keys("password")
    
    #Find the "Log in" button using any locator and click it.
    login=driver.find_element(By.XPATH, "//button[text()='Submit']")
    login.click()
    
    
    text=driver.find_element(By.XPATH, "//h1[contains(text(), 'Success!')]")
    print(text.text)
   
    #Close the browser.
    driver.close()