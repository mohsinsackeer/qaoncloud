from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(r"C:\Users\Jakkula Jahnavi\Downloads\geckodriver-v0.31.0-win64")
driver.get('https://www.geeksforgeeks.org/python-programming-language/')
print(driver.title)
search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
driver.close()
