""" Task 1: Open amazon
Search for Mobiles
Click search
Get the price of Mobile using Name (traversing) 
"""
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
#o.add_argument("--headless")
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Mobiles")
driver.find_element(By.ID,"nav-search-submit-button").click()
sleep(2)
price=driver.find_element(By.XPATH,"//span[text()='Samsung Galaxy M07 Mobile (Black, 4GB RAM, 64GB Storage) | MediaTek Helio G99 | AnTuTu 624K | IP54| 50MP Camera | 7.6mm Slim | 5000mAh Battery | 25W Fast Charging | 6 Gen OS Upgrades | Without Charger']/../../../..//div[3]//div[1]//div[1]//div[1]//div[1]//div[1]//span[2]//span[2]")
print("Price of Samsung is:",price.text)   
driver.close()
