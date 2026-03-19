""" Task 2: open demoqa
add your details in webtables
fetch your name and salary
and print name = salary"""
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
o=ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--disable-notifications")
#o.add_argument("--headless")
driver=Chrome(options=o)
driver.get("https://demoqa.com/webtables")
driver.maximize_window()
wait = WebDriverWait(driver,50)
#add your details in the table
name = wait.until(EC.visibility_of_element_located((By.XPATH,"//td[text()='Kriti']")))
salary = wait.until(EC.visibility_of_element_located((By.XPATH,"//td[text()='Kriti']//following-sibling::td[4]")))
print(name.text,"=",salary.text)
driver.close()