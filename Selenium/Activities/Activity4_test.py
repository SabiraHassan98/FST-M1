from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color

with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/target-practice")
    print("The page title is: " + driver.title)
    #Get the title of the page and print it to the console.
    #Using xpath: Find the 3rd header on the page and print it's text to the console.
    thirdelement= driver.find_element(By.XPATH, "//h3[contains(text(), '#3')]")
    print("The header text is: " + thirdelement.text)
    #Find the 5th header on the page and print it's color.
    fifth_heading_color = Color.from_string(driver.find_element(By.XPATH, "//h5[contains(text(), '#5')]").value_of_css_property("color"))
    print("Fifth heading colour as Hexcode: ", fifth_heading_color.hex)
    print("Fifth heading colour as RGB: ", fifth_heading_color.rgb)
    #Using any other locator:
    #Find the purple button and print all it's classes.
    purple_button = driver.find_element(By.XPATH, "//button[contains(@class, 'text-purple-900')]").get_attribute("class")
    print("the class values are:" + purple_button)
    #Find the slate button and print it's text.
    slate_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Slate')]").text
    print("the slate text is: " + slate_button)

    #Close the browser.
    driver.quit