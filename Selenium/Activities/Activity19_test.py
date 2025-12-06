from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
with webdriver.Firefox() as driver:
    #Open a new browser to https://training-support.net/webelements/alerts
    driver.get("https://training-support.net/webelements/alerts")
    wait = WebDriverWait(driver, timeout=10)
    #Get the title of the page and print it to the console.
    print("The title of the age is: " + driver.title)
    #Find the button to open a SIMPLE alert and click it.
    driver.find_element(By.ID, "confirmation").click()
    #Switch the focus from the main window to the Alert box and get the text in it and print it.
    confirmalert = wait.until(EC.alert_is_present())
    print(confirmalert.text)
    #Close the alert once with OK.
    confirmalert.accept()
    driver.find_element(By.ID, "confirmation").click()
    #Switch the focus from the main window to the Alert box and get the text in it and print it.
    confirmalert = wait.until(EC.alert_is_present())
    confirmalert.dismiss()
    # Print the message
    print(driver.find_element(By.ID, "result").text)
    #Close the browser.
    driver.quit