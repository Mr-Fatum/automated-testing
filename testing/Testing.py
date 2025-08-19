from selenium import webdriver
from selenium.webdriver.common.by import By
import time


etp = "https://acron.gpms.naumen.ru/"
portal = "https://ompk.gpms.naumen.ru/fx/"

try:
    browser = webdriver.Chrome()
    browser.get(portal)
    # заполнение поля Логин
    input = browser.find_element(By.XPATH, "//*[@id=\"login\"]")
    input.send_keys("artin")
    # заполнение поля Пароль
    input = browser.find_element(By.XPATH, "//*[@id=\"password\"]")
    input.send_keys("123456")
    # вход в систему под указанный пользователем (нажали на кнопу "войти по паролю")
    button = browser.find_element(By.XPATH, "//*[@id=\"LogonFormSubmit\"]")
    button.click()

    time.sleep(5)

    button = browser.find_element(By.XPATH, "//*[@id=\"gwtAddSrmPurchase\"]")
    button.click

finally:
    time.sleep(2)