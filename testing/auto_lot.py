from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
URL = "https://ompk.gpms.naumen.ru/fx/"
USERNAME = "martin"
PASSWORD = "AlNmbH234__"

try:
    driver.get(URL)
    driver.maximize_window()
    # заполнение поля Логин
    input1 = driver.find_element(By.XPATH, "//*[@id=\"login\"]")
    input1.send_keys("martin")
    # заполнение поля Пароль
    input2 = driver.find_element(By.XPATH, "//*[@id=\"password\"]")
    input2.send_keys("AlNmbH234__")
    # вход в систему под указанный пользователем (нажали на кнопу "войти по паролю")
    button = driver.find_element(By.XPATH, "//*[@id=\"LogonFormSubmit\"]")
    button.click()

    # Ждем и кликаем кнопку Добавить
    button = driver.find_element(By.XPATH, "//*[@id=\"gwtAddSrmPurchase\"]")
    button.click()

    # Ждем появления dropdown
    dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[.//option[contains(text(), 'Закупка')]]"))
    )

    # Кликаем чтобы раскрыть список
    dropdown.click()
    time.sleep(1)

    # Ищем и кликаем нужную опцию
    option = driver.find_element(By.XPATH,
                                 "//option[contains(text(), 'Закупка (вспомогательные материалы, технические закупки)')]")
    option.click()

    print("Успешно выбрано!")

except TimeoutException:
    print("Элемент не найден в течение времени ожидания")
except NoSuchElementException:
    print("Элемент не существует на странице")
except Exception as e:
    print(f"Произошла ошибка: {str(e)}")
finally:
    time.sleep(10)
    driver.quit()