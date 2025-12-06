from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/drag-drop")
    print(driver.title)
    football = driver.find_element(By.ID, "ball")
    dropzone1 = driver.find_element(By.ID, "dropzone1")
    dropzone2 = driver.find_element(By.ID, "dropzone2")

    actions = webdriver.ActionChains(driver)
    actions.click_and_hold(football).move_to_element(dropzone1).pause(1).release().perform()
    if(dropzone1.find_element(By.CLASS_NAME, "dropzone-text").text=="Dropped!"):
        print("ball is in dropzone 1")
    

    actions.drag_and_drop(football,dropzone2).pause(2).perform()
    if (dropzone2.find_element(By.CLASS_NAME, "dropzone-text").text=="Dropped!"):
        print("Ball is in dropzone2") 
    
    driver.quit()