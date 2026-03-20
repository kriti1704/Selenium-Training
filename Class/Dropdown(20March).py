# Select dropdown
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome()
driver.get("file:///C:/Desktop/Selenium/E22_Dropdowns.html")
driver.maximize_window()
driver.implicitly_wait(5)

# single select dropdown
dropdown = driver.find_element(By.ID,"state")
s = Select(dropdown)
s.select_by_visible_text("West Bengal")
s.select_by_index(3) #Maharashtra selected
s.select_by_value("KL") #Kerala selected
sleep(3)

# multi select dropdown
hobbies = driver.find_element(By.ID,"hobby")
s1 = Select(hobbies)
s1.select_by_visible_text("Dance")
s1.select_by_index(2)
s1.select_by_value("read")
s1.select_by_value("music")
s1.deselect_by_visible_text("Yoga")
s1.deselect_by_index(6)
s1.deselect_by_value("music")
s1.deselect_all()
sleep(2)
driver.quit() """

# to print all options in dropdown
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
o = ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--headless")
driver = Chrome(options=o)
driver.get("file:///C:/Desktop/Selenium/E22_Dropdowns.html")
driver.maximize_window()
driver.implicitly_wait(5)
dropdown = driver.find_element(By.ID,"state")
s = Select(dropdown)
all_options = s.options
for option in all_options:
    print(option.text) """

# Custom dropdowns
# searching shoes in amazon and selecting from the search list dropdown
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("shoes for women")
sleep(2)
dropdown = driver.find_elements(By.XPATH,"//div[@class='s-suggestion-container']")
for i in dropdown:
    print(i.text)

dropdown[2].click()
sleep(2)
driver.quit()

