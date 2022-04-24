from selenium import webdriver # import selenium & download chromedriver (https://chromedriver.chromium.org/downloads)
from time import sleep # install time for watch time
# If you have pip errors try : pip --version and if it doesn't work, uninstall and install python latest version 


driver = webdriver.Chrome(executable_path="chromedriver.exe") # you can create as much as you want for more views
driver1 = webdriver.Chrome(executable_path="chromedriver.exe") # it only depends of your machine
driver2 = webdriver.Chrome(executable_path="chromedriver.exe") # chromedriver path need to work 
driver3 = webdriver.Chrome(executable_path="chromedriver.exe")
driver4 = webdriver.Chrome(executable_path="chromedriver.exe")

driver.get("https://youtu.be/WLmAcdPvX8g") # replace with your video url !
driver1.get("https://youtu.be/WLmAcdPvX8g") # replace with your video url !
driver2.get("https://youtu.be/WLmAcdPvX8g") # replace with your video url !
driver3.get("https://youtu.be/WLmAcdPvX8g") # replace with your video url !
driver4.get("https://youtu.be/WLmAcdPvX8g") # replace with your video url !

while True:
    sleep(20) # you can change the watchtime here (sleep(20) = 20s)
    driver.refresh() # if you created other vars dont forget to update them in here
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()
    driver4.refresh()
