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
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--headless")
driver=Chrome(options=o)
driver.get("https://the-internet.herokuapp.com/tables")
due = driver.find_element(By.XPATH,"(//td[text()='Tim'])[1]//following-sibling::td[2]")
print("Due amount of Tim is:",due.text)
driver.close() """

#Xpath using parent - can access only parent
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://the-internet.herokuapp.com/tables")
parent = driver.find_element(By.XPATH,"((//td[text()='Tim'])[1]/parent::tr")
print(parent.text)
driver.close() """

# Xpath using ancestor - can access parent, grandparent etc
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://the-internet.herokuapp.com/tables")
table = driver.find_element(By.XPATH,"(//td[text()='Tim'])[1]/ancestor::table")
print(due.text)
driver.close() """

# Xpath using child - can access only child
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://the-internet.herokuapp.com/tables")
child = driver.find_element(By.XPATH,"(//td[text()='Tim'])[1]/../child::td[4]")
print(child.text)
driver.close() """

#Xpath using descendant - can access child,grandchild etc
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://the-internet.herokuapp.com/tables")
due = driver.find_element(By.XPATH,"(//td[text()='Tim'])[1]/../../descendant::td[22]")
print(due.text)
driver.close() """