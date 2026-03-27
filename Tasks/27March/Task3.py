"""Task 3:Open demowebshop application 
Scroll to Facebook link (bottom of page)
Click and enter username and password 
Click on login"""
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ActionChains
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("http://demowebshop.tricentis.com/")
driver.maximize_window()
sleep(2)

# scrolling to the facebook link
actions = ActionChains(driver)
ele = driver.find_element(By.LINK_TEXT,"Facebook")
actions.scroll_to_element(ele).perform()

# clicking on facebook link
ele.click()
sleep(2)

# entering username and password
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.NAME,"email").send_keys("kritijain617@gmail.com")
driver.find_element(By.NAME,"pass").send_keys("Kriti@1234")

# clicking on login button
driver.find_element(By.XPATH,"//div[@aria-label='Log in to Facebook']").click()
sleep(2)

driver.close()