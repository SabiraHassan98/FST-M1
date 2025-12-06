from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/")
    print ("the title of the page is : " + driver.title)
    driver.find_element(By.LINK_TEXT, "About Us")
    # Find the "About Us" button on the page using ID and click it
    #print thenew titke of the page
    print("The new title is: " + driver.title)
