# open demo workshop and fill the registration form using pytest
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(5)

# clicking on register
def test_registration():
    driver.find_element(By.LINK_TEXT,"Register").click()

# filling gender female
def test_gender():
    driver.find_element(By.ID,"gender-female").click()

# filling first name
def test_firstname():
    driver.find_element(By.ID,"FirstName").send_keys("Kriti")

# filling last name
def test_lastname():
    driver.find_element(By.ID,"LastName").send_keys("Jain")

# filling email
def test_email():    
    driver.find_element(By.ID,"Email").send_keys("kritijain67@gmail.com")

# filling password
def test_password():
    driver.find_element(By.ID,"Password").send_keys("kriti@123")

# filling confirm password
def test_confirmpassword():
    driver.find_element(By.ID,"ConfirmPassword").send_keys("kriti@123")

# clicking on register button
def test_register():
    driver.find_element(By.NAME,"register-button").click()

driver.close()
