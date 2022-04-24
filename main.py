from selenium import webdriver
from time import sleep 

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver1 = webdriver.Chrome(executable_path="chromedriver.exe")
driver2 = webdriver.Chrome(executable_path="chromedriver.exe")
driver3 = webdriver.Chrome(executable_path="chromedriver.exe")
driver4 = webdriver.Chrome(executable_path="chromedriver.exe")

driver.get("https://youtu.be/WLmAcdPvX8g")
driver1.get("https://youtu.be/WLmAcdPvX8g")
driver2.get("https://youtu.be/WLmAcdPvX8g")
driver3.get("https://youtu.be/WLmAcdPvX8g")
driver4.get("https://youtu.be/WLmAcdPvX8g")

while True:
    sleep(20)
    driver.refresh()
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()
    driver4.refresh()