# Importing necessary libraries for environment variables
from dotenv import load_dotenv
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

# Credentials via env
load_dotenv()
account_name = os.getenv["ACCOUNT_NAME"]
account_password = os.getenv["ACCOUNT_PASSWORD"]
account_phone = os.getenv["ACCOUNT_PHONE"]

# Explicit Wait
def document_initialised(driver):
    return driver.execute_script("return initialised")

driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chrome.exe")
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3618090331&geoId=103121230&keywords=it%20intern&location=Philippines&refresh=true")

title = driver.title
assert title == "Web form"

sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

WebDriverWait(driver, timeout=10).until(document_initialised)
el_button = driver.find_element(By.TAG_NAME, "button")
assert el_button.text == "Button found!"
# driver.implicitly_wait(0.5)

email_field = driver.find_element_by_id("username")
email_field.send_keys(account_name)
password_field = driver.find_element_by_id("password")
password_field.send_keys(account_password)
password_field.send_keys(Keys.ENTER)

WebDriverWait(driver, timeout=10).until(document_initialised)
el = driver.find_element(By.TAG_NAME, "p")
assert el.text == "Hello from JavaScript!, paragraph found"

# Application Button
apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
apply_button.click()

# Phone number entry
WebDriverWait(driver, timeout=10).until(document_initialised)
el_form = driver.find_element(By.TAG_NAME, "form")
phone = driver.find_element_by_class_name("fb-single-line-text__input")
if phone.text == "":
    phone.send_keys(account_phone)

#Submit the application
submit_button = driver.find_element_by_css_selector("footer button")
submit_button.click()