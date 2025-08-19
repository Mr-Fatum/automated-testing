from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

etp = "https://acron.gpms.naumen.ru/"
portal = "https://ompk.gpms.naumen.ru/fx/"
driver = webdriver.Chrome()
driver.implicitly_wait(10)

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(portal)
    # заполнение поля Логин
    input1 = browser.find_element(By.XPATH, "//*[@id=\"login\"]")
    input1.send_keys("martin")
    # заполнение поля Пароль
    input = browser.find_element(By.XPATH, "//*[@id=\"password\"]")
    input.send_keys("AlNmbH234__")
    # вход в систему под указанный пользователем (нажали на кнопу "войти по паролю")
    button = browser.find_element(By.XPATH, "//*[@id=\"LogonFormSubmit\"]")
    button.click()

    time.sleep(5)

    button = browser.find_element(By.XPATH, "//*[@id=\"gwtAddSrmPurchase\"]")
    button.click()
    # Поиск выпадающего списка "Способ закупки"
    purchase_method_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//select[.//option[text()='Закупка (вспомогательные материалы, технические закупки)']]"))
    )

    # Создание объекта Select
    select = Select(purchase_method_dropdown)

    # Выбор опции по видимому тексту
    select.select_by_visible_text("Закупка (вспомогательные материалы, технические закупки)")

    signature_required = driver.find_element(By.XPATH, "//select[.//option[text()='да'] and .//option[text()='нет']]")
    select = Select(signature_required)
    select.select_by_value("нет")

finally:
    time.sleep(10)
    browser.close()
#     visibility: visible;
#     outline: 0 none;
#     cursor: pointer;
#     width: 100%;
#     position: relative;
#     border: 1px solid #D4DBE4;
#     border-radius: 4px 4px 4px 4px;
#     box-shadow: 0 2px 2px -1px #DBDBDB inset;
#     font-family: Arial;
#     padding: 1px 1px 1px 4px;
#     text-align: left;
#     height: 26px;
#     line-height: 26px;
#     box-sizing: border-box;
