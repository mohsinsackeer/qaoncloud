from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# driver = webdriver.Firefox(r"C:\Users\Jakkula Jahnavi\Downloads\geckodriver-v0.31.0-win64")
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://127.0.0.1:5002')
print(driver.title)
# search_bar = driver.find_element_by_name("q")
search_bar = driver.find_element(By.NAME, "q")
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
driver.close()
