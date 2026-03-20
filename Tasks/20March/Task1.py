# search zomato and order your favourite food using dropdown
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.zomato.com/jaipur/restaurants")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[@placeholder = 'Search for restaurant, cuisine or a dish']").send_keys("Pizza")
driver.find_element(By.XPATH,"//input[@placeholder = 'Search for restaurant, cuisine or a dish']").click()
sleep(5)
dropdown = driver.find_elements(By.XPATH,"//p[@class ='sc-1hez2tp-0 sc-gFXMyG jkvifB']")
dropdown[7].click()
sleep(2)
driver.quit()