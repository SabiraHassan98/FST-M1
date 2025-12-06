from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as driver:


    #Open a new browser to https://training-support.net/webelements/tables
    driver.get("https://training-support.net/webelements/tables")
    #Get the title of the page and print it to the console.
    print("the page title is: " + driver.title)
    #Using xpaths on the table:
    #Find the number of rows and columns in the table and print them.
    column_no = driver.find_elements(By.XPATH, "//table[contains(@class, 'table-auto')]/thead/tr/th")
    print("column no. is: ", len(column_no))
    rows_no= driver.find_elements(By.XPATH, "//table[contains(@class, 'table-auto')]/tbody/tr")
    print("rows no. is: ", len(rows_no))
    #Find and print the Book Name in the 5th row.
    FifthBook = driver.find_element(By.XPATH, "//table[contains(@class, 'table-auto')]/tbody/tr[5]/td[2]")
    print("the 5th book name is : " + FifthBook.text)
    #Click the header of the Price column to sort it in ascending order.
    driver.find_element(By.XPATH, "//table[contains(@class, 'table-auto')]/thead/tr/th[5]").click()
    #Find and print the Book Name in the 5th row again.
    aftersort=driver.find_element(By.XPATH, "//table[contains(@class, 'table-auto')]/tbody/tr[5]/td[2]")
    print("after sorting the 5th book name is : " + aftersort.text)
    #Close the browser.