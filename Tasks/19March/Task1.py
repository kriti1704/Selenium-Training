""" Task 1: open amazon
search for anything
fetch how many product are getting displayed
click on the ith product"""
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach",True)
#o.add_argument("--headless")
driver = Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Dress")
driver.find_element(By.ID,"nav-search-submit-button").click()
products = driver.find_elements(By.XPATH,"//img[@class='s-image']")
print("no. of products being dispalyed=",len(products))
products[5].click()
driver.quit()