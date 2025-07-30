import math
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ожидаем, когда цена уменьшится до $100 (максимум 12 секунд)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажимаем кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    x = int(browser.find_element(By.ID, "input_value").text)
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    button = browser.find_element(By.ID, "solve")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()