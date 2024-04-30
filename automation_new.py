from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

# Start the Chrome WebDriver with the specified path
driver = webdriver.Chrome()
# Open the website

driver.get("https://stagingui.geotabreports.com/login/")

field1 = driver.find_element(By.ID, "validationCustomUsername")
field1.send_keys("sqltestbruffolo@gmail.com")

field2 = driver.find_element(By.ID, "dz-password")
field2.send_keys("gpssolsql2022")

# Click the submit button
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()

time.sleep(5)

driver.get("https://stagingui.geotabreports.com/dashboard/lng_menus_text/")

time.sleep(5)

# field3 = driver.find_element(By.ID, "name")
# field3.send_keys("Client ID")


# field4 = driver.find_element(By.ID, "title")
# field4.send_keys("Client ID")

# field5 = driver.find_element(By.ID, "type")
# field5.send_keys("Label")

# submit_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.ID, "save_btn"))
# )
# submit_button.click()



values = [
    
    # {"name": "Client ID", "title": "Client ID", "type": "Label"},
    # {"name": "Unit ID", "title": "Unit ID", "type": "Label"},
    # {"name": "Purchase Date", "title": "Purchase Date", "type": "Label"},
    # {"name": "Date From", "title": "Date From", "type": "Label"},
    # {"name": "Date To", "title": "Date To", "type": "Label"},
    # {"name": "Model", "title": "Model", "type": "Label"},

]


for value_set in values:
    
    parent_container = driver.find_element(By.ID, "cable_form")

    field1 = parent_container.find_element(By.ID, "name")
    # field1.clear()  
    field1.send_keys(value_set["name"])

    field2 = parent_container.find_element(By.ID, "title")
    # field2.clear()
    field2.send_keys(value_set["title"])

    field3 = parent_container.find_element(By.ID, "type")
    # field3.clear()  
    field3.send_keys(value_set["type"])

    # Click the submit button
    submit_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "save_btn"))
    )
    try:
        driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()
    except ElementClickInterceptedException:
        # Retry scrolling and clicking the button
        driver.execute_script("window.scrollBy(0, 100);")  # Scroll a bit more
        driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()

    time.sleep(2)  

driver.quit()

    # submit_button.click()

# time.sleep(10)


# # Close the browser
# driver.quit()
