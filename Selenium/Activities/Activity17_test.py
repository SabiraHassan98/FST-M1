from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
with webdriver.Firefox() as driver:
    #Open a new browser to https://training-support.net/webelements/selects
    driver.get("https://training-support.net/webelements/selects")
    #Get the title of the page and print it to the console.
    print(driver.title)
    #On the Multi Select:
    dropdown = driver.find_element(By.CSS_SELECTOR, "select.h-80")
    multi_select = Select(dropdown)
    #Select the "HTML" option using the visible text.
    multi_select.select_by_visible_text("HTML")
    #Select the 4th, 5th and 6th options using the index.
    for i in range(3,5):
        multi_select.select_by_index(i)
    #Select the "Node" option using the value.
    multi_select.select_by_value("nodejs")
    Allselected = multi_select.all_selected_options
    print("=======================ALL selected options============= ")
    for options in Allselected:
        print(options.text)

    #Deselect the 5th option using index.
    multi_select.deselect_by_index(4)
    Allselected = multi_select.all_selected_options
    print("==================post deselection of index 4: ")
    for i in Allselected:
        print(i.text)
    #Close the browser.
    driver.quit 
    