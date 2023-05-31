# Importing necessary libraries for environment variables
from dotenv import load_dotenv
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# Credentials via env
load_dotenv()
account_name = os.getenv["ACCOUNT_NAME"]
account_password = os.getenv["ACCOUNT_PASSWORD"]

# Explicit Wait
def document_initialised(driver):
    return driver.execute_script("return initialised")

driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chrome.exe")

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3618090331&geoId=103121230&keywords=it%20intern&location=Philippines&refresh=true")

title = driver.title
assert title == "Web form"

WebDriverWait(driver, timeout=10).until(document_initialised)
el = driver.find_element(By.TAG_NAME, "p")
driver.implicitly_wait(0.5)

text_box = driver