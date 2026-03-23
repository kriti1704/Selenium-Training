""" Task-1: Search testautomationpractice.blogspot.com
and perform following actions:-
1. Mouse Hover
2. Double Click
3. Drag and Drop """
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver import ActionChains
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(2)

#mouse hover
ele1 = driver.find_element(By.XPATH,"//button[text()= 'Point Me']")
actions = ActionChains(driver)
actions.scroll_to_element(ele1).perform()
actions.scroll_by_amount(0,500).perform()
sleep(2)
actions.move_to_element(ele1).perform()
sleep(2)

# double click
double_click = driver.find_element(By.XPATH,"//button[text()='Copy Text']")
actions.double_click(double_click).perform()
sleep(2)

# drag and drop
drag = driver.find_element(By.ID,"draggable")
drop = driver.find_element(By.ID,"droppable")
actions.drag_and_drop(drag,drop).perform()
sleep(4)

driver.close()