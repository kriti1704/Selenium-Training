# 1. ID locator
#send_keys() and click() element method
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
sleep(1)
driver.find_element(By.ID,"userName").send_keys("Kriti Jain")
driver.find_element(By.ID,"userEmail").send_keys("kritijain617@gmail.com")
driver.find_element(By.ID,"currentAddress").send_keys("JECRC university, Jaipur")
driver.find_element(By.ID,"permanentAddress").send_keys("Kishangarh, Ajmer")
driver.find_element(By.ID,"submit").click()
sleep(2)
driver.close() """

# search in amazon for shirts
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("shirts")
driver.find_element(By.ID,"nav-search-submit-button").click()
sleep(2)
driver.close() """

# 2. NAME locator
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(1)
driver.find_element(By.NAME,"field-keywords").send_keys("sneakers")
driver.find_element(By.ID,"nav-search-submit-button").click()
sleep(1)
driver.close() """

# 3. CLASS_NAME locator
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(1)
#in compound class name space should be replaced with '.'
driver.find_element(By.CLASS_NAME,"nav-input.nav-progressive-attribute").send_keys("i phone 15") 
driver.find_element(By.ID,"nav-search-submit-button").click()
sleep(1)
driver.close() """

# 4. TAG_NAME locator(least used)
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
sleep(1)
driver.find_element(By.TAG_NAME,"input").send_keys("Kriti Jain") # enters the value in first input tag
driver.find_element(By.TAG_NAME,"input").send_keys("kritijain617@gmail.com") # enters the value in the first input tag only
driver.find_element(By.TAG_NAME,"textarea").send_keys("Jaipur")# enters the value in first textarea
sleep(2)
driver.close() """

# 5. LINK_TEXT locator(works for only anchor tags)
#It is case sensitive and space sensitive
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(1)
driver.find_element(By.LINK_TEXT,"Mobiles").click() #use visible text as locator_value
sleep(2)
driver.close() """

# 6. PARTIAL_LINK_TEXT locator(works for only anchor tags)
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT,"Mob").click() #use visible text as locator_value
sleep(2)
driver.close()  """

# 7. CSS_SELECTOR locator
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(1)
driver.find_element(By.CSS_SELECTOR,"#twotabsearchtextbox").send_keys("sneakers")
driver.find_element(By.CSS_SELECTOR,"#nav-search-submit-button").click()
sleep(1)
driver.close()