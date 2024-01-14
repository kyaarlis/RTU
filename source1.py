from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://nodarbibas.rtu.lv/"
driver.get(url)
time.sleep(2.0)

studiju_prog_button = driver.find_element(By.CLASS_NAME, "btn.dropdown-toggle.btn-light") 
studiju_prog_button.click()

a_elem = driver.find_element(By.ID, "bs-select-1-10")

a_elem.click()

select_course = driver.find_element(By.ID, "course-id")
select_course.click()
course_options = driver.find_elements(By.TAG_NAME, "option")
print("Text inside the div:", course_options.text)

time.sleep(2.0)
driver.quit()