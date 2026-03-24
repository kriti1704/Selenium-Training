""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(2) """

""" alert1 = driver.find_element(By.ID,"alertBtn")
alert1.click()
sleep(2)
driver.switch_to.alert.accept() """

""" alert2 = driver.find_element(By.ID,"confirmBtn")
alert2.click()
sleep(2)
#driver.switch_to.alert.accept() # OK
driver.switch_to.alert.dismiss() # cancel
sleep(2) """

""" alert3 = driver.find_element(By.ID,"promptBtn")
alert3.click()
sleep(2)
a = driver.switch_to.alert
a.send_keys("Kriti Jain") 
a.accept()
sleep(2)
driver.close() """

# upload and download
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://demoqa.com/upload-download")
driver.maximize_window()
driver.find_element(By.ID,"uploadFile").send_keys(r"C:\Desktop\capegemini\Kriti Jain Photo.png")
sleep(2)
driver.find_element(By.ID,"downloadButton").click()
sleep(2)
driver.close()"""

# download python - enable safe browsing
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option("detach",True)

# to enable safe browsing
o.add_experimental_option("prefs",{"safebrowsing.enabled":True})

driver=Chrome(options=o)
driver.get("https://www.python.org/downloads/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[text()='Download Python install manager']").click()
sleep(2) """

# disable notifications
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--disable-notifications")
driver=Chrome(options=o)
driver.get("https://www.easemytrip.com/flights.html?utm_campaign=788997081&utm_source=g_c&utm_medium=cpc&utm_term=e_easemytrip&adgroupid=39319940377&gad_source=1&gad_campaignid=788997081&gbraid=0AAAAADo_0-h3QJ-p11y-Kv-NZh2sT2JIk&gclid=EAIaIQobChMIqpaKoKO4kwMVOi17Bx0fQjEVEAAYASAAEgLnrfD_BwE")
driver.maximize_window()
sleep(2)
driver.close() """

# irctc setting date
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--disable-notifications")
driver=Chrome(options=o)
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").click()
driver.find_element(By.XPATH,"//span[contains(@class,'ui-datepicker-next')]").click()
driver.find_element(By.XPATH,"//a[text()='14']").click()
sleep(2)
driver.close() """

# demoqa - date in forms
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select
o=ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--disable-notifications")
driver=Chrome(options=o)
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.ID,"dateOfBirthInput").click()
select = Select(driver.find_element(By.XPATH,"//select[@class='react-datepicker__month-select']"))
select.select_by_visible_text("June")
select1 = Select(driver.find_element(By.XPATH,"//select[@class='react-datepicker__year-select']"))
select1.select_by_visible_text("2004")
driver.find_element(By.XPATH,"//div[text()='17']").click()
sleep(2)
driver.close()