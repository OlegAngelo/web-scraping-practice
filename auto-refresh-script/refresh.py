import time
from selenium import webdriver

driver_path = './chromedriver.exe'

url = 'https://whatcanicookonline.vercel.app' 

driver = webdriver.Chrome(driver_path)

driver.get(url)

try:
    while True:
        time.sleep(5)
        driver.refresh()
except KeyboardInterrupt:
    driver.quit()

