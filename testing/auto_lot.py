from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Настройки
URL = "https://ompk.gpms.naumen.ru/fx/"
USERNAME = "martin"
PASSWORD = "AlNmbH234__"

# Инициализация
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

try:
    # 1. Открыть сайт
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(URL)

    # 2. Ввести логин и пароль
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "login"))).send_keys("martin")
    browser.find_element(By.ID, "password").send_keys("AlNmbH234__")
    browser.find_element(By.ID, "LogonFormSubmit").click()

    # 3. Добавление новой закупки (примерный путь — уточнить селекторы!)
    add_procurement_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Добавить закупку")]')))
    add_procurement_btn.click()

    # Ввести название
    name_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="purchaseName"]')))
    name_input.send_keys("AutoTest")

    # Выбрать способ закупки
    method_select = driver.find_element(By.XPATH, '//select[@name="purchaseMethod"]')
    method_select.click()
    option = driver.find_element(By.XPATH, '//option[contains(text(), "Закупка (вспомогательные материалы, технические закупки)")]')
    option.click()

    # Подпись предложения обязательно = "нет"
    signature_select = driver.find_element(By.XPATH, '//select[@name="signatureRequired"]')
    signature_select.click()
    driver.find_element(By.XPATH, '//option[contains(text(), "нет")]').click()

    # 4. Добавление лота
    add_lot_btn = driver.find_element(By.XPATH, '//button[contains(text(), "Добавить лот")]')
    add_lot_btn.click()

    # Лот: говядина 1 сорт
    lot1_name = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="lotName"]')))
    lot1_name.send_keys("Говядина 1 сорт")
    lot1_qty = driver.find_element(By.XPATH, '//input[@name="lotQuantity"]')
    lot1_qty.send_keys("5")

    # Добавить ещё один лот
    add_lot_btn.click()
    lot2_name = wait.until(EC.presence_of_element_located((By.XPATH, '(//input[@name="lotName"])[last()]')))
    lot2_name.send_keys("Говядина высший сорт")
    lot2_qty = driver.find_element(By.XPATH, '(//input[@name="lotQuantity"])[last()]')
    lot2_qty.send_keys("6")

    # Установить чекбокс "невозможно определить начальную стоимость"
    checkbox = driver.find_element(By.XPATH, '//input[@name="undefinedPrice"]')
    if not checkbox.is_selected():
        checkbox.click()

    # Сохранить закупку
    save_btn = driver.find_element(By.XPATH, '//button[contains(text(), "Сохранить")]')
    save_btn.click()

finally:
    # Закрыть браузер после работы
    driver.quit()
