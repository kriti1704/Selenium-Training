# assertion for title check
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.google.com/")
driver.maximize_window()
sleep(2)

expected = "Google Chrome"
actual = driver.title
assert  expected == actual , "Title is not matching" #error message
driver.find_element(By.XPATH,"//textarea[@title='Search']").send_keys("War updates")
driver.close() # if this works condition is true  """

# assert title check on amazon
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,"//a[text()='Bestsellers']").click()
sleep(2)
expected = 'Amazon.in Bestsellers: The most popular items on Amazon'
actual = driver.title
assert expected == actual, "Title is not matching"
driver.close() """

# screenshot for a page
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
import os
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.google.com/")
driver.maximize_window()
sleep(2)
# driver.save_screenshot("ss1.png") # stores in the same directory
folder = os.path.join(os.getcwd(),"Screenshot") # create a folder
os.makedirs(folder,exist_ok=True) # if folder is not present it will create
driver.save_screenshot(f"{folder}/ss1.png") # stores in the screenshot folder
driver.close() """

# screenshot of a particular element
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
import os
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.google.com/")
driver.maximize_window()
sleep(2)
ele = driver.find_element(By.XPATH,"//textarea[@title='Search']")
folder = os.path.join(os.getcwd(),"Screenshot")
os.makedirs(folder,exist_ok=True)
ele.screenshot(f"{folder}/ss2.png") # screenshot of element
driver.close() """

# screenshot with the help of time
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
import time
import os
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.google.com/")
driver.maximize_window()
sleep(2)
ele = driver.find_element(By.XPATH,"//textarea[@title='Search']")
folder = os.path.join(os.getcwd(),"Screenshot")
os.makedirs(folder,exist_ok=True)
timestamp = time.strftime("%d-%m-%Y--%H-%M-%S")
ele.screenshot(f"{folder}/ss3({timestamp}).png") # screenshot of element
driver.close() """

#

