from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
with webdriver.Firefox() as driver:
    #Open a new browser to https://training-support.net/webelements/selects
    driver.get("https://training-support.net/webelements/selects")
    #Get the title of the page and print it to the console.
    print("the page title is: " + driver.title)
    #On the Single Select:
    dropdown = driver.find_element(By.CSS_SELECTOR, "select.h-10" )
    select_singleObject = Select(dropdown)
    #Select the second option using the visible text.
    select_singleObject.select_by_visible_text("Two")
    print("2nd option: " + select_singleObject.first_selected_option.text)
    #Select the third option using the index.
    select_singleObject.select_by_index(3)
    print("3rd index option: " + select_singleObject.first_selected_option.text)
    #Select the fourth option using the value.
    select_singleObject.select_by_value("four")
    print("4th option: " + select_singleObject.first_selected_option.text)
    ##Get all the options and print them to the console.
    all_the_options = select_singleObject.options
    for options in all_the_options:
        print(options.text)
    #Close the browser
    driver.quit