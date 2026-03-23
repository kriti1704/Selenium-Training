"""  Task 2 : open Nike.com and perform following operations:
1. Mouse hover and click on kids
2. Give a scroll
3. Click on air max shop
4. Pick any shoe (scroll to it) and click
 5. Add to bag
6. Select size
7. Add to bag """
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.Nike.in/")
driver.maximize_window()
driver.implicitly_wait(2)
actions = ActionChains(driver)

# hover on kids and click
ele1 = driver.find_element(By.XPATH,"//span[text()='Kids']")
actions.move_to_element(ele1).perform()
sleep(2)
actions.click(ele1).perform()
sleep(2)

# scroll
driver.execute_script("window.scrollBy(0, 500)")
sleep(1)
driver.find_element(By.XPATH,"//a[contains(text(),'Shop')]").click()
sleep(2)

# have doubts as shop is not traceable so discuss it tomorrow
driver.quit()