from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3618090331&geoId=103121230&keywords=it%20intern&location=Philippines&refresh=true")

title = driver.title
assert title == "Web form"

driver.implicitly_wait(0.5)

text_box = driver