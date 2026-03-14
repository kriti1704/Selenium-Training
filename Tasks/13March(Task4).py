""" Task 4:
1. Go to https://selenium.dev/
2. Click on Download using link text
3. Click on other languages exist using partial link text
4. Fetch title"""

from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.selenium.dev/")
sleep(2)
driver.find_element(By.LINK_TEXT,"Downloads").click()
sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT,"other").click()
sleep(2)
print(driver.title)
driver.close()