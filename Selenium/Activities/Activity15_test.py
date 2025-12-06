from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Firefox() as driver:

	wait = WebDriverWait(driver, timeout=10)
	#Open a new browser to https://training-support.net/webelements/dynamic-attributes
	driver.get("https://training-support.net/webelements/dynamic-attributes")
	#//Get the title of the page and print it to the console.
	print(driver.title)
	#Find the input fields and type in the required data in the fields.
	user = driver.find_element(By.XPATH, "//input[starts-with(@id, 'full-name-')]")
	email = driver.find_element(By.XPATH, "//input[contains(@id, '-email')]")
	date = driver.find_element(By.XPATH, "//input[contains(@name, '-event-date-')]")
	details = driver.find_element(By.XPATH, "//textarea[contains(@id, '-additional-details-')]")
	user.send_keys("Sabira Hassan")
	email.send_keys("Sabira.H@gmail.com")
	date.send_keys("2025-11-30")
	details.send_keys("event details")
	#//Wait for success message to appear and print it to the console.
	driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]").click()
	msg= wait.until(EC.visibility_of_element_located((By.ID, "action-confirmation"))).text
	print(msg)
	#//Close the browser.
	driver.quit()
		