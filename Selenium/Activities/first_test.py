from selenium import webdriver
    
with webdriver.Firefox() as driver:
    #open the page
    driver.get("https://training-support.net")
    #verify page title
    print("The title is: {driver.title}")
    #page interaction

    #close the browser
    driver.quit()




    