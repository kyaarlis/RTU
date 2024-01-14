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

def studiju_grafiks(study_program, course, group):
    visas_studiju_prog_button = driver.find_element(By.CLASS_NAME, "btn.dropdown-toggle.btn-light") 
    visas_studiju_prog_button.click()

    studiju_prog = driver.find_element(By.ID, study_program)
    studiju_prog.click()

    select_course = driver.find_element(By.ID, "course-id")
    select_course.click()
    course_options = select_course.find_elements(By.TAG_NAME, "option")

    for option in course_options:
        if option.text == course:
            option.click()

    select_group = driver.find_element(By.ID, "group-id")
    select_group.click()
    group_options = select_group.find_elements(By.TAG_NAME, "option")

    for group_option in group_options:
        if group_option.text == group:
            group_option.click()

    time.sleep(5.0)


studiju_grafiks("bs-select-1-10", "1", "2")
driver.quit()