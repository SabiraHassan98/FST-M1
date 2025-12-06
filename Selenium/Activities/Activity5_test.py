from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/dynamic-controls")
    print("the tite of the page is: "+ driver.title)
    checkbox= driver.find_element(By.ID, "checkbox")

    toggle_checkbox = driver.find_element(By.XPATH, "//button[text()='Toggle Checkbox']")
    toggle_checkbox.click()
    print("Checkbox is displayed: " , checkbox.is_displayed())
    toggle_checkbox.click()
    print("Checkbox is displayed: " , checkbox.is_displayed())
    #3rd time
    toggle_checkbox.click()

    print("Checkbox is displayed: " , checkbox.is_displayed())
    driver.quit()
    