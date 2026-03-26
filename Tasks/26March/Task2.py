""" Task 2: Write a Selenium script in Python to open the Lenskart website,

1) Open the lenskart
2) Click on Eyeglasses
3) Validate the url using assert
4) Locate the Sort By and select the option Most Viewed
5) Capture a screenshot of the webpage and save it to your local system """
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)

#open lenskart
driver.get("https://www.lenskart.com/")
driver.maximize_window()
sleep(2)

# open eyeglasses
driver.find_element(By.XPATH,"//a[text()='EYEGLASSES']").click()
sleep(2)

# validate url
expected = "https://www.lenskart.com/eyeglasses.html"
actual = driver.current_url
assert actual == expected, "URL is not matching"
sleep(2)

# select most viewed
dropdown = driver.find_element(By.ID,"sortByDropdown")
s = Select(dropdown)
s.select_by_visible_text("Most Viewed")
sleep(2)
driver.save_screenshot("lenskart.png")
sleep(2)
driver.close()