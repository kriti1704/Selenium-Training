""" Task 1: open Flipkart
search for any product
fetch the name of 6th product using waits"""
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
o=ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--disable-notifications")
o.add_argument("--headless")
driver=Chrome(options=o)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//span[@role='button']").click()
driver.find_element(By.NAME,"q").send_keys("Lipstick")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
wait = WebDriverWait(driver,10)
name = wait.until(EC.visibility_of_element_located((By.XPATH,"(//a[@title='MARS Ultra Pigmented Creamy Matte Lipstick'])[1]")))
print(name.text)
driver.close()