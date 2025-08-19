from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

etp = "https://acron.gpms.naumen.ru/"
portal = "https://ompk.gpms.naumen.ru/fx/"

try:
    # Инициализация Edge WebDriver
    browser = webdriver.Edge()
    browser.get(portal)

    # заполнение поля Логин
    input = browser.find_element(By.XPATH, "//*[@id=\"login\"]")
    input.send_keys("martin")

    # заполнение поля Пароль
    input = browser.find_element(By.XPATH, "//*[@id=\"password\"]")
    input.send_keys("123456")

    # вход в систему под указанный пользователем (нажали на кнопу "войти по паролю")
    button = browser.find_element(By.XPATH, "//*[@id=\"LogonFormSubmit\"]")
    button.click()

    time.sleep(5)

    # Нажимаем кнопку создания закупки
    button = browser.find_element(By.XPATH, "//*[@id=\"gwtAddSrmPurchase\"]")
    button.click()

    time.sleep(2)

    # Заполняем название лота
    input = browser.find_element(By.XPATH, "//input[@name='name']")
    input.send_keys("Auto test")

    # Выбираем способ закупки
    purchase_method = Select(browser.find_element(By.XPATH, "//select[@name='purchaseMethod']"))
    purchase_method.select_by_visible_text("Закупка (вспомогательные материалы, технические закупки)")

    time.sleep(1)  # Ждем обновления формы

    # Устанавливаем "нет" в поле "Подпись предложение обязательно"
    signature_required = Select(browser.find_element(By.XPATH, "//select[@name='signatureRequired']"))
    signature_required.select_by_visible_text("нет")

    # Нажимаем кнопку сохранения
    save_button = browser.find_element(By.XPATH, "//button[contains(text(), 'Сохранить')]")
    save_button.click()

    time.sleep(3)  # Ждем сохранения

    print("Лот закупки успешно создан")

finally:
    time.sleep(2)
    browser.quit()