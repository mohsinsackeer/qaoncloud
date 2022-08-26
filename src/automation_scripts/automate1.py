from selenium import webdriver
from selenium.webdriver.common.by import By
# import requests
from static import url, details_dictv1

details = details_dictv1
url = url[1]


def auto1(path='chromedriver.exe'):
    driver = webdriver.Chrome(path)
    driver.get(url)
    form_element = driver.find_element(By.TAG_NAME, 'form')
    name_input = form_element.find_element(By.ID, 'name')
    name_input.send_keys(details.get('name'))
    driver.implicitly_wait(10)

    department_input = form_element.find_element(By.ID, 'department')
    department_input.send_keys(details.get('department'))

    cgpa_input = form_element.find_element(By.ID, 'CGPA')
    cgpa_input.send_keys(details.get('CGPA'))

    input_12 = form_element.find_element(By.ID, '12')
    input_12.send_keys(details.get('12'))
    driver.implicitly_wait(10)

    input_10 = form_element.find_element(By.ID, '10')
    input_10.send_keys(details.get('10'))
    driver.implicitly_wait(10)

    # gender_id=details.get('gender').lower()
    gender_element = form_element.find_element(By.ID, 'male')
    gender_element.click()
    driver.implicitly_wait(10)

    submit = form_element.find_element(By.ID, 'submit_form')
    submit.click()


if __name__ == '__main__':
    auto1()
