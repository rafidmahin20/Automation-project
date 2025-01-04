import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# Path to ChromeDriver (use relative or absolute path)
driver_path = Service(r'chromedriver.exe')
driver = webdriver.Chrome(service=driver_path)

try:
    # Open a website
    url = "https://devprincebazar.ibos.io/"
    driver.get(url)
    
    # Wait for the mobile number field to be present
    mobile_no_ID = 'loginMobileNo'
    mobile_no_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, mobile_no_ID))
    )
    
    # Enter the mobile number
    mobile_no_field.send_keys("01553663248")  # Correct number format if needed
    time.sleep(5)  # Allow time to observe the action

    password_ID = 'loginPassword'
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, password_ID))
    )
    
    # Enter the mobile number
    password_field.send_keys("123456")  # Correct number format if needed
    time.sleep(5)  # Allow time to observe the actio

    button_ID = 'loginButton'
    button_ID_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, button_ID))
    )
    button_ID_field.click()
    time.sleep(5)
    
finally:
    # Close the browser
    driver.quit()
