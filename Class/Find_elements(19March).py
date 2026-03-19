#fetch all the links on google home page using find_elements
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--headless")
driver = Chrome(options=o)
driver.get("https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(5)
links = driver.find_elements(By.TAG_NAME,"a")
#print(links) # gives the address of all the links
print(len(links)) # gives the count of links
#print the visible text or name of links
for l in links: 
    print(l.text) """

#get_attribute to fetch attribute value
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--headless")
driver = Chrome(options=o)
driver.get("https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(10)
ele = driver.find_element(By.XPATH,"//a[@class='gb_A']")
print(ele.get_attribute('aria-label')) # returns the value of aria-label attribute """

# get attributes of all links in amazon
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--headless")
driver = Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(10)
links = driver.find_elements(By.XPATH,"//a[@class = 'nav-a  ']")
for l in links:
    print(l.get_attribute('text'))



