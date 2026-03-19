# is_displayed() and is_enabled() method
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(5)
ele = driver.find_element(By.XPATH,"//span[text()='Log in']")
print("Displayed:",ele.is_displayed())
print("Enabled:",ele.is_enabled())
driver.close() """

# 2
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.naukri.com/registration/createAccount?othersrcp=23531&wExp=N&utm_source=google&utm_medium=cpc&utm_campaign=Brand_Login_Register&gclsrc=aw.ds&gad_source=1&gad_campaignid=292348446&gbraid=0AAAAADLp3cHQGK0hvfh6zjohfDHagIT1L&gclid=EAIaIQobChMIjM_VsbSrkwMVWco8Ah3GhwtJEAAYASAAEgLL9vD_BwE")
driver.maximize_window()
driver.implicitly_wait(5)
ele = driver.find_element(By.XPATH,"//button[@type='submit']")
print("Displayed:",ele.is_displayed())
print("Enabled:",ele.is_enabled())
driver.close() """

# is_selected method
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://the-internet.herokuapp.com/checkboxes")
driver.maximize_window()
driver.implicitly_wait(5)
ele1 = driver.find_element(By.XPATH,"//input[@type='checkbox'][1]")
ele2 = driver.find_element(By.XPATH,"//input[@type='checkbox'][2]")
print("Checkbox1 is selected:",ele1.is_selected())
print("Checkbox2 is selected:",ele2.is_selected())
driver.close() """

# filling a form
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://demoqa.com/automation-practice-form")
driver.find_element(By.ID,"firstName").send_keys("Kriti")
driver.find_element(By.ID,"lastName").send_keys("Jain")
driver.find_element(By.ID,"userEmail").send_keys("kritijain617@gmail.com")
driver.find_element(By.ID,"gender-radio-2").click()
driver.find_element(By.ID,"userNumber").send_keys("1234567890")
driver.find_element(By.ID,"dateOfBirthInput").click()
driver.find_element(By.XPATH,"//div[text()='25']").click()
driver.find_element(By.ID,"hobbies-checkbox-2").click()
# upload files in forms
driver.find_element(By.ID,"uploadPicture").send_keys(r"C:\Desktop\capegemini\Kriti Jain Photo.png") #if path has space then use r before path   
driver.find_element(By.ID,"currentAddress").send_keys("JECRC University, Jaipur")
driver.quit()