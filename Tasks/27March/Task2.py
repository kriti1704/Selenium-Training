#Task2 : open demo webshop and click on Apparel & Shoes and handle three dropdwons
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT,"Apparel & Shoes").click()

# dropdown1 using select_by_index
dropdown1 = driver.find_element(By.XPATH,"//select[@id='products-orderby']")
s1 = Select(dropdown1)
s1.select_by_index(2)
sleep(2)

# dropdown2 using select_by_value
dropdown2 = driver.find_element(By.XPATH,"//select[@id='products-pagesize']")
s2 = Select(dropdown2)
s2.select_by_value("https://demowebshop.tricentis.com/apparel-shoes?orderby=6&pagesize=4")
sleep(2)

# dropdown3 using select_by_visible_text
dropdown3 = driver.find_element(By.XPATH,"//select[@id='products-viewmode']")
s3 = Select(dropdown3)
s3.select_by_visible_text("List")
sleep(2)

driver.close()