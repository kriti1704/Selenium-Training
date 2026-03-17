""" Task 1: Open flipkart
Search for any item
Click search
Get the price of item using Name (traversing) 
"""
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--disable-notifications")
o.add_argument("--headless")
driver=Chrome(options=o)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
sleep(1)
driver.find_element(By.XPATH,"//span[@role='button']").click()
sleep(2)
driver.find_element(By.NAME,"q").send_keys("Lipstick")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
sleep(2)
price=driver.find_element(By.XPATH,"(//a[text() = 'SWISS BEAUTY Pure Matte Creamy Lipstick | Non-drying, H...'])[1]/..//a[3]//div//div[1]")
print("Price of the lipstick is:",price.text)
driver.close()