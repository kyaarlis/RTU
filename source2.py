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

    studiju_prog = driver.find_element(By.CLASS_NAME, "dropdown-menu.inner.show")
    for a in studiju_prog.find_elements(By.TAG_NAME, "a"):
        span = a.find_element(By.TAG_NAME, "span")
        if span.text == study_program:
            a.click()

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

    time.sleep(20.0)


study_program_input = input("Enter the study program: ")
course_input = input("Enter the course: ")
group_input = input("Enter the group: ")


studiju_grafiks(study_program_input, course_input, group_input)

driver.quit()
