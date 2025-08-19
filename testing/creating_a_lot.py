from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

portal = "https://ompk.gpms.naumen.ru/fx/"

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(portal)

    # --- Авторизация ---
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "login"))).send_keys("martin")
    browser.find_element(By.ID, "password").send_keys("AlNmbH234__")
    browser.find_element(By.ID, "LogonFormSubmit").click()

    # --- Ждём загрузки кнопки "Добавить закупку" ---
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.ID, "gwtAddSrmPurchase"))
    )
    browser.find_element(By.ID, "gwtAddSrmPurchase").click()

    # --- Ждём появления формы создания закупки ---
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.NAME, "purchaseName"))
    )

    # 1. Название закупки
    name_input = browser.find_element(By.XPATH, "/html/body/div[9]/div/table/tbody/tr[2]/td[2]/div/div/table[1]/tbody/tr[2]/td/div/div/div/div/div/table/tbody/tr[9]/td[2]/table/tbody/tr[2]/td")
    name_input.send_keys("Auto test")

    # 2. Выбор способа закупки
    method_field = browser.find_element(By.NAME, "purchaseMethod")
    method_field.click()
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[contains(text(), 'Закупка (вспомогательные материалы, технические закупки)')]"))
    ).click()

    # 3. Подпись предложения обязательно = "нет"
    signature_field = browser.find_element(By.NAME, "proposalSignatureRequired")
    signature_field.click()
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[contains(text(), 'нет')]"))
    ).click()

    # 4. Добавление лота
    add_lot_btn = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "gwtAddLot"))
    )
    add_lot_btn.click()

    # --- Заполняем данные лота ---
    lot_name = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "lotName"))
    )
    lot_name.clear()
    lot_name.send_keys("Лот 1 автотест")

    # (по желанию можно добавить описание лота и другие поля)
    # browser.find_element(By.NAME, "lotDescription").send_keys("Описание лота для автотеста")

    # --- Сохраняем закупку ---
    save_btn = browser.find_element(By.ID, "savePurchaseBtn")
    save_btn.click()

    print("✅ Закупка и лот успешно созданы!")

finally:
    time.sleep(500000)
    browser.quit()
