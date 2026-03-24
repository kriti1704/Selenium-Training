from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("file:///C:/Desktop/Selenium/Page1.html")
driver.maximize_window()
sleep(2)

driver.find_element(By.ID,"inp1").send_keys("input 1")
driver.switch_to.default_content()
sleep(2)

driver.switch_to.frame("frame1") #using name or id
driver.find_element(By.ID,"inp2").send_keys("input 2")
sleep(2)

driver.switch_to.frame(0) #using indexing
driver.find_element(By.ID,"inp3").send_keys("input 3")
sleep(2)

driver.switch_to.parent_frame() #switching back to parent frame
driver.find_element(By.ID,"inp2").clear()
driver.find_element(By.ID,"inp2").send_keys("I am back from page 3")
sleep(2)

driver.switch_to.default_content() #switching back to main page
driver.find_element(By.ID,"inp1").clear()
driver.find_element(By.ID,"inp1").send_keys("I am back from page 2")
sleep(2)

iframe = driver.find_element(By.ID,"frame1") #using webelement
driver.switch_to.frame(iframe)
driver.find_element(By.ID,"inp2").clear()
driver.find_element(By.ID,"inp2").send_keys("using webelement")
sleep(2)

# moving to page1 from page3
driver.switch_to.frame(0)
driver.switch_to.default_content()
driver.find_element(By.ID,"inp1").clear()
driver.find_element(By.ID,"inp1").send_keys("I am back from page 3")
sleep(2)
driver.close()
