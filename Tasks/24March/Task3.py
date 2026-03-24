""" Task 3 : Open 3 tabs with different websites
Print each tabs title and url
Close all except the first tab """
from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.google.com/")
driver.maximize_window()
sleep(2)
driver.switch_to.new_window("tab")
driver.get("https://www.facebook.com/")
sleep(2)
driver.switch_to.new_window("tab")
driver.get("https://www.youtube.com/")
sleep(2)

# Print title and URL of each tab
tabs = driver.window_handles
for tab in tabs:
    driver.switch_to.window(tab)
    print(driver.title)
    print(driver.current_url)
sleep(2)

# Closing all tabs except first
driver.switch_to.window(tabs[2])
sleep(2)
driver.close()
sleep(2)
driver.switch_to.window(tabs[1])
sleep(2)
driver.close()
sleep(2)
driver.switch_to.window(tabs[0])