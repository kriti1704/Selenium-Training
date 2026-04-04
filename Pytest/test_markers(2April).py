import pytest
# skip marker
""" @pytest.mark.skip
def test_skip(reason="Practicing skip marker"):
    print("This test is skipped")
    assert False # asssertion error """

# skipif marker
# if condition satisfied then test is skipped
""" @pytest.mark.skipif(True, reason="Practicing skipif marker") # test will skip
def test_skipif1():
    print("This test is skipped")
    assert True # assert passed

@pytest.mark.skipif(False, reason="Practicing skipif marker") # test will not skip
def test_skipif2():
    print("This test is not skipped")
    assert True # assert passed """

# parametrized marker
# it will run 2 times as two items are passed
""" @pytest.mark.parametrize("a,b",[(2,3),(7,2)])
def test_add(a,b):
    print(a,b) """

# logging in to saucedemo.com
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

@pytest.mark.parametrize("uname,password", [("standard_user","secret_sauce"),("locked_out_user","secret_sauce"),("","")])
def test_login(uname,password):
    driver = Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID,"user-name").send_keys(uname)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.ID,"login-button").click()
    assert "inventory" in driver.current_url, "Login failed" # asserting if login is successful
    sleep(2)
    driver.quit() """

# Pytest fixtures
""" @pytest.fixture(autouse=True)
def greet():
    print("Hello")
    yield
    print("Bye")

def test_morning():
    print("Good Morning")

def test_evening():
    print("Good Evening") """

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="class")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://demowebshop.tricentis.com/register")
    sleep(2)
    yield driver
    driver.close()

class TestRegister():

    def test_gender(self,setup):
        setup.find_element(By.ID,"gender-female").click()
        sleep(2)
    
    def test_FirstName(self,setup):
        setup.find_element(By.ID,"FirstName").send_keys("Kriti")
        sleep(2)
    
    def test_LastName(self,setup):
        setup.find_element(By.ID,"LastName").send_keys("Jain")
        sleep(2)
    
    def test_Email(self,setup):
        setup.find_element(By.ID,"Email").send_keys("kritijain617@gmail.com")
        sleep(2)
    
    def test_Password(self,setup):
        setup.find_element(By.ID,"Password").send_keys("kriti@123")
        sleep(2)
    
    def test_ConfirmPassword(self,setup):
        setup.find_element(By.ID,"ConfirmPassword").send_keys("kriti@123")
        sleep(2)
    
    def test_Register(self,setup):
        setup.find_element(By.NAME,"register-button").click()
        sleep(2)
    
    

    
