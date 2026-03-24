"""Task 2: open zomato and click on login and clink on google login"""
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.zomato.com/jaipur/delivery")
driver.maximize_window()
sleep(2)
# click on login
driver.find_element(By.XPATH,"//a[text()='Log in']").click()
sleep(4)
# switch to login iframe
iframe = driver.find_element(By.XPATH,"//iframe[contains(@id,'auth')]")
driver.switch_to.frame(iframe)
#switch to google iframe
iframe2 = driver.find_element(By.XPATH,"//iframe[@title='Sign in with Google Button'][1]")
driver.switch_to.frame(iframe2)
# click on sign in with google
driver.find_element(By.XPATH,"//span[text()='Sign in with Google']").click()
sleep(4)
driver.quit()