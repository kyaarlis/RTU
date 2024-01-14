from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from db import insert_data, retrieve_data

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

def user_inputs():
    study_program_input = input("Ievadiet studiju programmas nosaukumu: ")
    course_input = input("Ievadiet kursa numuru: ")
    group_input = input("Ievadiet grupas numuru: ")

    insert_data(study_program_input, course_input, group_input)

def studiju_grafiks(study_program, course, group):
    url = "https://nodarbibas.rtu.lv/"
    driver.get(url)

    visas_studiju_prog_button = driver.find_element(By.CLASS_NAME, "btn.dropdown-toggle.btn-light") 
    visas_studiju_prog_button.click()

    studiju_prog = driver.find_element(By.CLASS_NAME, "dropdown-menu.inner.show")
    for a in studiju_prog.find_elements(By.TAG_NAME, "a"):
        span = a.find_element(By.TAG_NAME, "span")
        if span.text == study_program:
            a.click()

    select_course = driver.find_element(By.ID, "course-id")
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

    time.sleep(20.0)

retrieved_data = retrieve_data()

print("Retrieved data:", len(retrieved_data))
print(retrieved_data)

if len(retrieved_data) == 0:
    user_inputs()

retrieved_data = retrieve_data()

study_program = retrieved_data[-1]['study_program']
course = retrieved_data[-1]['study_course']
group = retrieved_data[-1]['study_group']

    
studiju_grafiks(study_program, course, group)

driver.quit()