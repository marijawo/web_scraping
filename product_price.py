# https://www.province-electric.com/m18-jobsite-radio-milwaukee-1.html
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Start Webdiver and navigate to website
PATH = "C:\Program Files (x86)\chromedriver.exe"
serv_obj = Service(PATH)
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.province-electric.com/m18-jobsite-radio-milwaukee-1.html")

# Wait for the product details to load and get the data
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'pdp'))
)

product_name = driver.find_element(By.TAG_NAME, 'h1').text
product_price = driver.find_element(By.CLASS_NAME, 'price').text
cad_price = product_price.replace("CAD", "")


# Write the data to a csv file

with open("product_details.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(['Product Name', 'Price'])
    writer.writerow([product_name, cad_price])

# close the webdriver
driver.quit()

