from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/dynamic-controls")
    checkbox = driver.find_element(By.ID, "checkbox")
    #checkbox.click()
    print("the checkbox is selected: " , checkbox.is_selected())
    checkbox.click()
    print("the checkbox is selected: " , checkbox.is_selected())
    driver.quit()
    
    