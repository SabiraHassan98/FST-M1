from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/tables")
    column_no = driver.find_elements(By.XPATH, "//table[contains(@class, 'table-auto')]/thead/tr/th")
    print("column no. is: ", len(column_no))
    rows_no= driver.find_elements(By.XPATH, "//table[contains(@class, 'table-auto')]/tbody/tr")
    print("rows no. is: ", len(rows_no))

    ##Find and print all the cell values in the third row of the table.
    thirdrow = driver.find_elements(By.XPATH, "//table[contains(@class, 'table-auto')]/tbody/tr[3]/td")
    print("Third row cell values: ")
    for cell in thirdrow:
        print(cell.text)
    ##Find and print the cell value at the second row second column.
    secondrow = driver.find_element(By.XPATH, "//table[contains(@class, 'table-auto')]/tbody/tr[2]/td[2]")
    print("the second row second coloum element is : ", secondrow.text)
    ##Close the browser.
    driver.quit