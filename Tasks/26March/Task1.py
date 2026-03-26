""" Task 1: Write a Selenium script to open a website take screenshots.

1) Open https://in.pinterest.com/
2) Take the screenshot of entire page
3) Scroll to a picture and caputure the screenshot of the picture """
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://in.pinterest.com/")
driver.maximize_window()
sleep(2)

# ss of a page
driver.save_screenshot("pinterest.png")
sleep(2)

# ss of an element
ele = driver.find_element(By.XPATH,"//img[contains(@alt,'cherry')]")
ele.screenshot("element.png")
driver.close()
