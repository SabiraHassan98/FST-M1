from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as driver:
    #Open a new browser to https://training-support.net/webelements/dynamic-controls
	driver.get("https://training-support.net/webelements/dynamic-controls")
	#Get the title of the page and print it to the console.
	print("page title is : "+ driver.title)
	#On the page, perform:Find the text field.
	textField = driver.find_element(By.ID, "textInput")
	#Check if the text field is enabled and print it.
	print("The text field is enabled : ", textField.is_enabled())
	#Click the "Enable Input" button to enable the input field.
	driver.find_element(By.ID, "textInputButton").click()
	#Check if the text field is enabled again and print it.
	print("The text field is enabled : ", textField.is_enabled())
	#Close the browser.
	driver.quit()