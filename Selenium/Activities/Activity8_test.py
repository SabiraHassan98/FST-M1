from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/mouse-events")
    print("the title is: " + driver.title)
    actions = webdriver.ActionChains(driver)
    cargolock = driver.find_element(By.XPATH,"//h1[contains(text(),'Cargo.lock')]")
    cargotoml = driver.find_element(By.XPATH, "//h1[contains(text(), 'Cargo.toml')]")
    srcbutton = driver.find_element(By.XPATH, "//h1[contains(text(), 'src')]")
    targetbutton = driver.find_element(By.XPATH, "//h1[contains(text(), 'target')]")

    actions.click(cargolock).pause(1).move_to_element(cargotoml).pause(1).click(cargotoml).perform()
    message = driver.find_element(By.ID, "result").text
    print(message)
    actions.double_click(srcbutton).pause(2).pause(3).context_click(targetbutton).pause(4).perform()
    actions.click(driver.find_element(By.XPATH, "//div[@id = 'menu']/div/ul/li[1]")).pause(1).perform()
    messagetarget = driver.find_element(By.ID, "result").text
    print(messagetarget)

    driver.quit()
                                

    
    

    
