# Task 2: get attributes of all links in amazon
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