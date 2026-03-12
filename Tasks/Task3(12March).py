""" Task 3:
Open wikipedia.org
Refresh
Fetch title
Open Amazon.com
Fetch title
Go back
Close """

from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)

driver.get("https://www.wikipedia.org/")
sleep(3)
driver.refresh()
sleep(3)
print(driver.title)

driver.get("https://www.amazon.com/")
sleep(3)
print(driver.title)
driver.back()
sleep(3)
driver.close()
