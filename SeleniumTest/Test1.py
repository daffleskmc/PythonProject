from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/Users/indeztruk/PycharmProjects/MyProject/Drivers/chromedriver.exe")

driver.set_page_load_timeout("10")
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("Automation Step by Step")
driver.find_element_by_name("q").send_keys(Keys.ENTER)

driver.maximize_window()
driver.refresh()

time.sleep(4)
driver.quit()


# print("Hello World")
# a = 10
# b = 20
# c = a + b
# print(c)
