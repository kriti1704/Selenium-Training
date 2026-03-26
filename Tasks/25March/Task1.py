"""Task1: open saucedemo.com
if credentials are valid login 
else take screenshot"""
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
import time
import os
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
sleep(2)
uname = "standard_user"
password = "secret_sauce"
driver.find_element(By.ID,"user-name").send_keys(uname)
driver.find_element(By.ID,"password").send_keys(password)
driver.find_element(By.ID,"login-button").click()
sleep(2)
try:
    assert "inventory" in driver.current_url
    print("Login successful")
except:
    print("Login failed")
    driver.save_screenshot("screenshot.png")

driver.close()