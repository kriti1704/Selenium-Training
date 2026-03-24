"""  Task 2 : open Nike.com and perform following operations:
1. Mouse hover and click on kids
2. Give a scroll
3. Click on air max shop
4. Pick any shoe (scroll to it) and click
5. Add to bag
6. Select size
7. Add to bag """
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.nike.in/")
driver.maximize_window()
sleep(5)
actions = ActionChains(driver)

# mouse hover and clicking on 'Kids'
ele1=driver.find_element(By.XPATH, "//span[text()='Kids']")
actions.move_to_element(ele1).perform()
actions.click(ele1).perform()
driver.switch_to.window(driver.window_handles[1])

# scrolling down and clicking on 'shop'
ele2=driver.find_element(By.XPATH, "//a[text()='Shop']")
actions.scroll_to_element(ele2).perform()
actions.click(ele2).perform()
sleep(5)

# clicking on 'shoes'
ele3=driver.find_element(By.XPATH, "//div[text()='Nike Air Max 90 SE']")
actions.scroll_to_element(ele3).perform()
actions.click(ele3).perform()
sleep(5)
driver.switch_to.window(driver.window_handles[2])

# add to bag 
ele4=driver.find_element(By.XPATH, "//button[text()='Add to Bag']")
actions.scroll_to_element(ele4).perform()
actions.click(ele4).perform()

# selecting size and clicking on 'add to bag'
ele5=driver.find_element(By.XPATH, "//label[text()='UK 6 (EU 40)']")
actions.click(ele5).perform()
actions.click(ele4).perform()
sleep(5)

driver.quit()