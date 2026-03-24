""" Task 4 : Open internet.herokuapp.com
Open JS alerts
Practice on all 3 alert options and also print the text from those alerts """
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://the-internet.herokuapp.com/")
sleep(2)
driver.find_element(By.XPATH,"//a[text()='JavaScript Alerts']").click()

# alert1
driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']").click()
alert1=driver.switch_to.alert
print(alert1.text)
alert1.accept()
sleep(2)

# alert2
driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']").click()
alert2=driver.switch_to.alert
print(alert2.text)
alert2.accept()
sleep(2)

# alert3
driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
alert3=driver.switch_to.alert
print(alert3.text)
alert3.send_keys("Kriti Jain")
alert3.accept()
sleep(2)

driver.close()