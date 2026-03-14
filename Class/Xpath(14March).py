# Xpath using relative pathh with attributes
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
sleep(1)
driver.find_element(By.XPATH,"//input[@placeholder='Full Name']").send_keys("Kriti Jain")
driver.find_element(By.XPATH,"//input[@placeholder='name@example.com']").send_keys("kritijain617@gmail.com")
driver.find_element(By.XPATH,"//textarea[@placeholder='Current Address']").send_keys("JECRC university, Jaipur")
driver.find_element(By.XPATH,"//textarea[@id='permanentAddress']").send_keys("Kishangarh, Ajmer")
driver.find_element(By.XPATH,"//button[@id='submit']").click()
sleep(2)
driver.close() """

# Xpath using relative path with text
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(1)
driver.find_element(By.XPATH,"//a[text()='Mobiles']").click()
sleep(1)
driver.find_element(By.XPATH,"//a[.='Fashion']").click()
sleep(2)
driver.close() """

# Xpath using contains attribute
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(1)
driver.find_element(By.XPATH,"//a[contains(@href,'accelerator')]").click()
sleep(2)
driver.close() """

# Xpath using contains text
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(1)
driver.find_element(By.XPATH,"//span[(contains(text(),'Refrigerators')]").click()
sleep(1)
driver.find_element(By.XPATH,"//span[contains(text(),'Whirlpool')]").click() # use contains for partial text
sleep(2)
driver.close() """

# Xpath using group by indexing
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(1)
driver.find_element(By.XPATH,"(//a[@class = 'nav_a'])[9]").click() # amazon accelerator should open
sleep(2)
driver.close()