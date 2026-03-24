"Task 1: open twitter and click on sign up with google"
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://twitter.com/")
driver.maximize_window()
sleep(2)
iframe = driver.find_element(By.TAG_NAME,"iframe")
driver.switch_to.frame(iframe)
driver.find_element(By.XPATH,"//span[text()='Sign up with Google']").click()
sleep(2)
driver.quit()