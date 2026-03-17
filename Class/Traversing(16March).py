# Xpath using traversing
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--headless") # won't open browser
o.add_argument("--disable-notifications") # won't show notification or popups
driver=Chrome(options=o)
driver.get("https://demoqa.com/webtables")
salary = driver.find_element(By.XPATH,"//td[text()='Kierra']/..//td[5]")
print("Salary of Kierra is:",salary.text)
driver.close() """

# 2
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--headless")
driver=Chrome(options=o)
driver.get("https://the-internet.herokuapp.com/tables")
due = driver.find_element(By.XPATH,"//td[text()='Frank']/..//td[4]")
print("Due amount of Frank is:",due.text)
driver.close() """

# Xpath using sibling
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--headless")
driver=Chrome(options=o)
driver.get("https://the-internet.herokuapp.com/tables")
due = driver.find_element(By.XPATH,"(//td[text()='Tim'])[1]//following-sibling::td[2]")
print("Due amount of Tim is:",due.text)
driver.close()
