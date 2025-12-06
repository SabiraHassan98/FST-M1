from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/keyboard-events")
    actions = webdriver.ActionChains(driver)

    actions.send_keys("this is coming from selenium using python ").send_keys(Keys.RETURN).perform()
    message = driver.find_element(By.CSS_SELECTOR, "h1.mt-3").text
    print(message)