import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.NAME, "firstname")
    name.send_keys("Ilia")
    lastname = browser.find_element(By.NAME, "lastname")
    lastname.send_keys("Kuzminykh")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("6762534@rambler.ru")
    input_file= browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file_1.txt')  # добавляем к этому пути имя файла
    input_file.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()