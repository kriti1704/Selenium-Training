# select from and to station and get details
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.bmrc.co.in/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//span[text()='English']").click()
sleep(5)
dropdown = driver.find_element(By.XPATH,"(//select[@class='form-control select fare-selects'])[1]")
s = Select(dropdown)
s.select_by_visible_text("Trinity")
sleep(2)
dropdown2 = driver.find_element(By.XPATH,"(//select[@class='form-control select fare-selects'])[2]")
s1 = Select(dropdown2)
s1.select_by_visible_text("Cubbon Park")
sleep(2)
driver.find_element(By.XPATH,"(//button)[2]").click()
sleep(2)
driver.quit()

