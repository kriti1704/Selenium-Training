#Opening Chrome browser
""" from time import sleep
from selenium.webdriver import Chrome
driver = Chrome()
sleep(5) """

#Opening edge browser
""" from time import sleep
from selenium.webdriver import Edge
driver = Edge()
sleep(5) #not the standard way """

#Opening Chrome browser and keeping it open after execution
""" from selenium.webdriver import Chrome,ChromeOptions
o = ChromeOptions() #object of ChromeOptions class
o.add_experimental_option("detach",True) #to keep the browser open after execution
driver = Chrome(options=o) #driver is the object holding Chrome browser

#to open google.com
driver.get("https://www.google.com/") #return type is None

# Browser window management methods

#to maximize the browser window
driver.maximize_window() #return type is None
#to minimize the browser window
driver.minimize_window() #return type is None
#to set full screen
driver.fullscreen_window() #return type is None
 """

#To open amazon.com
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.com/")
driver.maximize_window()
sleep(2)
driver.minimize_window()

#Page information properties

#to fetch the title of the page for validation
print(driver.title) #return type is string
#to fetch the current url of the page
print(driver.current_url) #return type is string
#to fetch the page source of the page
print(driver.page_source) #return type is string """

# to open demoqa.com
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://demoqa.com/")
print(driver.title)
print(driver.current_url)
sleep(2)

#return name of browser
print(driver.name) #return type is string """

#to close the browser(only the current tab)
""" driver.close() #return type is None """

#to quit the browser(all the tabs)
""" driver.quit() #return type is None """

#to navigate to a new url
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.com/")
driver.maximize_window()
sleep(4)
driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.refresh()
sleep(2)
driver.close()







