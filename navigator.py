# https://www.province-electric.com/brands
import csv
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Start Webdiver and navigate to website
PATH = "C:\Program Files (x86)\chromedriver.exe"
serv_obj = Service(PATH)
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://www.province-electric.com/brands")

# link = driver.find_element(By.XPATH, "//div/span[@class='alphabetsButton'][14]")
# link_text = driver.find_element(By.XPATH, "//div/span[@class='alphabetsButton'][14]").text


# Wait for the product details to load and get the data
try:
    wait = WebDriverWait(driver, 10)
    link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div/span[@class='alphabetsButton'][14]"))
    )
    link.click()
    # time.sleep(5)

    link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Milwaukee"))
    )
    link.click()
    # time.sleep(5)

    # NOT reaching this page, will have to look at it later
    link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div/span[@class='part-no'][1]"))
    )
    link.click()
    time.sleep(20)
    driver.back()
    driver.back()

finally:
    driver.quit()
