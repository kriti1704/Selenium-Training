""" Task 3: Write a script to:

1) navigate to amazon
2) search a product through send_keys BUT dont click on search icon
3) Wait for the suggestions to appear
4) Click on 4th suggestion
5) Click on Sort By and click on newest arrivals
6) Click on free shipping check box
7) wait for first product and return the name=price """
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)

# open amazon
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(5)

# search
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Sunscreen")

# wait for suggestions
wait = WebDriverWait(driver,20)
dropdown = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='s-suggestion-container']")))

# click on 4th suggestion
dropdown[3].click()

# click on sort by and newest arrivals
driver.find_element(By.XPATH,"//span[@class='a-button-text a-declarative']").click()
driver.find_element(By.XPATH,"//a[text()='Newest Arrivals']").click()
sleep(2)

# click on free shipping
wait.until(EC.element_to_be_clickable((By.XPATH,"(//i[@class='a-icon a-icon-checkbox'])[3]"))).click()

# wait for first product and print name=price
name = wait.until(EC.visibility_of_element_located((By.XPATH,"(//h2[@class='a-size-base-plus a-spacing-none a-color-base a-text-normal'])[1]")))
price = wait.until(EC.visibility_of_element_located((By.XPATH,"(//span[@class='a-price-whole'])[1]")))
print(name.text,"= Rs",price.text)
driver.close()
