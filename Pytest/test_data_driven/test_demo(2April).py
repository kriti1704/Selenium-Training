from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
import pytest
from test_data_driven import get_test_data
@pytest.mark.parametrize("uname,password", get_test_data())
def test_login(driver,uname,password):
    driver.find_element(By.ID,"user-name").send_keys(uname)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.ID,"login-button").click()
    assert "inventory" in driver.current_url, "Login failed" # asserting if login is successful
    sleep(2)

