from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time


def body_click():
    # После выбора опции кликните на ней или вне dropdown
    option.click()
    time.sleep(0.5)
    body = driver.find_element(By.TAG_NAME, "body")
    body.click()


driver = webdriver.Chrome()
driver.implicitly_wait(10)
URL = "https://ompk.gpms.naumen.ru/fx/"
USERNAME = "martin"
PASSWORD = "AlNmbH234__"
purchase_name = "automatically created"

try:
    driver.get(URL)
    driver.maximize_window()

    # Сохраняем handle основной вкладки
    main_window = driver.current_window_handle

    # заполнение поля Логин
    input1 = driver.find_element(By.XPATH, "//*[@id=\"login\"]")
    input1.send_keys(USERNAME)

    # заполнение поля Пароль
    input2 = driver.find_element(By.XPATH, "//*[@id=\"password\"]")
    input2.send_keys(PASSWORD)

    # вход в систему
    button = driver.find_element(By.XPATH, "//*[@id=\"LogonFormSubmit\"]")
    button.click()

    # ... остальной код до блока с лотом ...

    # Добавление лота
    add_lot = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id=\"Item.lots.holder.events.newInstanceForm_outer\"]"))
    )
    add_lot.click()
    time.sleep(5)

    # --- РАБОТА С ФОРМОЙ ДОБАВЛЕНИЯ ЛОТА ---

    # Переключаемся на новое окно/вкладку если нужно
    windows = driver.window_handles
    if len(windows) > 1:
        driver.switch_to.window(windows[-1])
        print(f"Переключились на новую вкладку: {driver.title}")

    # ... работа с формой лота ...

    # 7. добавление значений количества необходимых материалов и сохранение лота
    try:
        meat1 = driver.find_element(By.XPATH, "//*[@id=\"SrmProductionNomenclatureRowEditor.amount3\"]")
        meat1.send_keys("5")
        meat1 = driver.find_element(By.XPATH, "//*[@id=\"SrmProductionNomenclatureRowEditor.amount4\"]")
        meat1.send_keys("6")

        add_lot_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "commit_outer"))
        )
        add_lot_button.click()
        print("Лот успешно добавлен")
        time.sleep(5)

        # ВАЖНО: возвращаемся на основную вкладку после закрытия формы лота
        driver.switch_to.window(main_window)
        time.sleep(2)

    except Exception as e:
        print(f"Ошибка при нажатии кнопки Добавить: {e}")
        # Все равно пытаемся вернуться на основную вкладку
        try:
            driver.switch_to.window(main_window)
        except:
            pass

    # 8. добавление извещения (ТЕПЕРЬ МЫ НА ОСНОВНОЙ ВКЛАДКЕ)
    try:
        # Ждем, чтобы страница обновилась после добавления лота
        time.sleep(3)

        create_notification = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "rebiddingNoticeSubmit"))
        )

        # Прокручиваем до элемента
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                              create_notification)
        time.sleep(1)

        # Двойная проверка, что элемент кликабелен
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "rebiddingNoticeSubmit"))
        )

        create_notification.click()
        print("Кнопка 'Создать извещение' успешно нажата")

    except Exception as e:
        print(f"Ошибка при нажатии кнопки Создать извещение: {e}")

except TimeoutException:
    print("Элемент не найден в течение времени ожидания")
except NoSuchElementException:
    print("Элемент не существует на странице")
except Exception as e:
    print(f"Произошла ошибка: {str(e)}")
    driver.save_screenshot("error_screenshot.png")
finally:
    time.sleep(5)
    driver.quit()