import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver


# Path to ChromeDriver (use relative or absolute path)
driver_path = Service(r'chromedriver.exe')
driver = webdriver.Chrome(service=driver_path)

# Open a website
driver.get("https://www.google.com")

# Open a website
driver.get("https://www.google.com")

time.sleep(5)

