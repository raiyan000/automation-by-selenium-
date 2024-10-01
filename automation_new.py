from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time

# Start the Chrome WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://stagingui.geotabreports.com/login/")

# Input login credentials
field1 = driver.find_element(By.ID, "validationCustomUsername")
field1.send_keys("sqltestbruffolo@gmail.com")

field2 = driver.find_element(By.ID, "dz-password")
field2.send_keys("gpssolsql2022")

# Click the login button
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()

# Wait for the page to load
time.sleep(10)

# Navigate to the dashboard
driver.get("https://stagingui.geotabreports.com/dashboard/lng_menus_text/")
time.sleep(10)

values = [
    # {"name": "Previous Driver", "title": "Previous Driver", "type": "TH"},
    # {"name": "Current Driver Full Name", "title": "Current Driver Full Name", "type": "TH"},
    # {"name": "Current Driver Address Line 1", "title": "Current Driver Address Line 1", "type": "TH"},
    # {"name": "Current Driver Address Line 2", "title": "Current Driver Address Line 2", "type": "TH"},
    # {"name": "Current Driver City", "title": "Current Driver City", "type": "TH"},
    # {"name": "Current Driver State or Province", "title": "Current Driver State or Province", "type": "TH"},
    # {"name": "Current Driver ZIP or Postal Code", "title": "Current Driver ZIP or Postal Code", "type": "TH"},
    # {"name": "Current Driver County", "title": "Current Driver County", "type": "TH"},
    # {"name": "Current Driver Home Phone ID", "title": "Current Driver Home Phone ID", "type": "TH"},
    # {"name": "Current Driver Work Phone ID", "title": "Current Driver Work Phone ID", "type": "TH"},
    # {"name": "Current Driver Email Address", "title": "Current Driver Email Address", "type": "TH"},
    # {"name": "Vehicle License Plate ID", "title": "Vehicle License Plate ID", "type": "TH"},
    # {"name": "Vehicle License Plate State or Province", "title": "Vehicle License Plate State or Province", "type": "TH"},
    # {"name": "License Plate Expiration Date", "title": "License Plate Expiration Date", "type": "TH"},
    # {"name": "Client Purchase Order ID", "title": "Client Purchase Order ID", "type": "TH"},
    # {"name": "Initial Bill Date", "title": "Initial Bill Date", "type": "TH"},
    # {"name": "Manager Name", "title": "Manager Name", "type": "TH"},
    # {"name": "Manager Employee ID", "title": "Manager Employee ID", "type": "TH"},
    # {"name": "Manager Email ID", "title": "Manager Email ID", "type": "TH"},
    # {"name": "Interior Color", "title": "Interior Color", "type": "TH"},
    # {"name": "Exterior Color", "title": "Exterior Color", "type": "TH"},
    # {"name": "Seating", "title": "Seating", "type": "TH"},
    # {"name": "Drive System", "title": "Drive System", "type": "TH"},
    # {"name": "Payload", "title": "Payload", "type": "TH"},
    # {"name": "License Plate Type", "title": "License Plate Type", "type": "TH"},
    # {"name": "Tire Size", "title": "Tire Size", "type": "TH"},
    # {"name": "Taxable Weight Amount", "title": "Taxable Weight Amount", "type": "TH"},
    # {"name": "Title Owner Name", "title": "Title Owner Name", "type": "TH"},
    # {"name": "Title In-House Indicator", "title": "Title In-House Indicator", "type": "TH"},
    # {"name": "Personal Use Premium Fee Exemption", "title": "Personal Use Premium Fee Exemption", "type": "TH"},
    # {"name": "Current Driver Status", "title": "Current Driver Status", "type": "TH"},
    # {"name": "Title Issue State or Province", "title": "Title Issue State or Province", "type": "TH"},
    # {"name": "Title Issue Date", "title": "Title Issue Date", "type": "TH"},
    # {"name": "Title Retention Indicator", "title": "Title Retention Indicator", "type": "TH"},
    # {"name": "Breakdown Override", "title": "Breakdown Override", "type": "TH"},
    # {"name": "Address Override", "title": "Address Override", "type": "TH"},
    # {"name": "Current Driver Breakdown", "title": "Current Driver Breakdown", "type": "TH"},
    # {"name": "Current Driver Name", "title": "Current Driver Name", "type": "TH"},
    # {"name": "Current Driver Role", "title": "Current Driver Role", "type": "TH"},
    # {"name": "Current Driver First Name", "title": "Current Driver First Name", "type": "TH"},
    # {"name": "Current Driver Last Name", "title": "Current Driver Last Name", "type": "TH"},
    # {"name": "Current Driver Hire Date", "title": "Current Driver Hire Date", "type": "TH"},
    # {"name": "Dealer Assigned ID", "title": "Dealer Assigned ID", "type": "TH"}
    # {"name": "Dealer Related Amount", "title": "Dealer Related Amount", "type": "TH"},
    # {"name": "Factory Invoice Amount", "title": "Factory Invoice Amount", "type": "TH"},
    # {"name": "Purchase Order Type", "title": "Purchase Order Type", "type": "TH"},
    # {"name": "PUTB Payment Amount", "title": "PUTB Payment Amount", "type": "TH"},
    # {"name": "Sale Amount", "title": "Sale Amount", "type": "TH"},
    # {"name": "Termination Date", "title": "Termination Date", "type": "TH"},
    # {"name": "Unit Address Line 1", "title": "Unit Address Line 1", "type": "TH"},
    # {"name": "Unit Address Line 2", "title": "Unit Address Line 2", "type": "TH"},
    # {"name": "Unit City", "title": "Unit City", "type": "TH"},
    # {"name": "Unit County", "title": "Unit County", "type": "TH"},
    # {"name": "Unit State or Province", "title": "Unit State or Province", "type": "TH"},
    # {"name": "Unit ZIP or Postal Code", "title": "Unit ZIP or Postal Code", "type": "TH"},
    # {"name": "Vendor Related Amount", "title": "Vendor Related Amount", "type": "TH"},
    # {"name": "Current Month Depreciation Amount", "title": "Current Month Depreciation Amount", "type": "TH"},
    # {"name": "Current Month Interest Amount", "title": "Current Month Interest Amount", "type": "TH"},
    # {"name": "Current Month Lease Payment Amount", "title": "Current Month Lease Payment Amount", "type": "TH"},
    # {"name": "Current Month Management Fee Amount", "title": "Current Month Management Fee Amount", "type": "TH"},
    # {"name": "Current Month Rental Tax Amount", "title": "Current Month Rental Tax Amount", "type": "TH"},
    # {"name": "Current Month Thereafter Fee", "title": "Current Month Thereafter Fee", "type": "TH"},
    # {"name": "Storage Address", "title": "Storage Address", "type": "TH"},
    # {"name": "Storage Days", "title": "Storage Days", "type": "TH"},
    # {"name": "Storage Start Date", "title": "Storage Start Date", "type": "TH"},
    # {"name": "Spin Asset ID", "title": "Spin Asset ID", "type": "TH"},
    # {"name": "Purged Unit Indicator", "title": "Purged Unit Indicator", "type": "TH"}

]

for value_set in values:
    parent_container = driver.find_element(By.ID, "cable_form")

    field1 = parent_container.find_element(By.ID, "name")
    field1.clear()
    field1.send_keys(value_set["name"])

    field2 = parent_container.find_element(By.ID, "title")
    field2.clear()
    field2.send_keys(value_set["title"])

    field3 = parent_container.find_element(By.ID, "type")
    field3.clear()
    field3.send_keys(value_set["type"])

    # Re-locate the submit button inside the loop to avoid stale references
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "save_btn"))
    )

    try:
        # Scroll to and click the submit button using JavaScript
        driver.execute_script("arguments[0].click();", submit_button)
    except ElementClickInterceptedException:
        # If the button is not clickable, scroll down further and retry
        driver.execute_script("window.scrollBy(0, window.innerHeight);")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_button)
        submit_button.click()

    time.sleep(10)

driver.quit()
