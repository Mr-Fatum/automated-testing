from selenium import webdriver
from selenium.webdriver.common.by import By
import time


etp = "https://acron.gpms.naumen.ru/"
portal = "https://ompk.gpms.naumen.ru/fx/"

# try:
#     browser = webdriver.Chrome()
#     browser.get(etp)
#
#     input1 = browser.find_element(By.XPATH, "//*[@id=\"login\"]")
#     input1.send_keys("admin")
#     input1 = browser.find_element(By.XPATH, "//*[@id=\"password\"]")
#     input1.send_keys("123456")
#
#     # Отправляем заполненную форму
#     button = browser.find_element(By.XPATH, "//*[@id=\"Submit\"]")
#     button.click()
#
#     link = browser.find_element(By.XPATH, "//*[@id=\"DirectLink_0\"]")
#     link.click()
#
#     time.sleep(5)
#
#     # link2 = browser.find_element(By.XPATH, "//*[@id=\"DirectLink\"]")
#     # link2.click()
#
#     button2 = browser.find_element(By.XPATH, "//*[@id=\"Body\"]/div[7]/span")
#     button2.click()
try:
    browser = webdriver.Chrome()
    browser.get(portal)

    input = browser.find_element(By.XPATH, "//*[@id=\"login\"]")
    input.send_keys("Сидоров")

    input = browser.find_element(By.XPATH, "//*[@id=\"password\"]")
    input.send_keys("123456")

    button = browser.find_element(By.XPATH, "//*[@id=\"LogonFormSubmit\"]")
    button.click()

    link = browser.find_element(By.XPATH, "//*[@id=\"LogonFormSubmit\"]")
    link.click()
finally:
    time.sleep(100000)