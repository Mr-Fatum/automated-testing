from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time


def debug_scroll_issue(driver):
    """Диагностика проблем с прокруткой"""
    try:
        # Проверяем основные параметры
        page_height = driver.execute_script("return document.body.scrollHeight")
        viewport_height = driver.execute_script("return window.innerHeight")
        current_scroll = driver.execute_script("return window.pageYOffset")

        print(f"Высота страницы: {page_height}")
        print(f"Высота окна: {viewport_height}")
        print(f"Текущая позиция: {current_scroll}")
        print(f"Макс. прокрутка: {page_height - viewport_height}")

        # Проверяем, есть ли вообще что прокручивать
        if page_height <= viewport_height:
            print("Страница не требует прокрутки")
            return False

        return True

    except Exception as e:
        print(f"Ошибка диагностики: {e}")
        return False


def switch_to_correct_frame(driver):
    """Переключение на правильный iframe если он существует"""
    try:
        # Ищем iframe с формой
        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        for iframe in iframes:
            driver.switch_to.frame(iframe)
            # Проверяем, есть ли нужные элементы
            if driver.find_elements(By.ID, "commit"):
                return True
            driver.switch_to.default_content()
    except:
        pass
    return False

def scroll_to_element(driver, element, offset=0):
    """Прокрутить до элемента с возможным смещением"""
    driver.execute_script(f"""
        var element = arguments[0];
        var elementPosition = element.getBoundingClientRect().top;
        var offsetPosition = elementPosition + window.pageYOffset - {offset};

        window.scrollTo({{
            top: offsetPosition,
            behavior: 'smooth'
        }});
    """, element)
    time.sleep(0.5)


def body_click():
    # После выбора опции кликните на ней или вне dropdown
    option.click()
    time.sleep(0.5)

    # Клик в любое другое место страницы чтобы свернуть
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

    # заполнение поля Логин
    input1 = driver.find_element(By.XPATH, "//*[@id=\"login\"]")
    input1.send_keys(USERNAME)

    # заполнение поля Пароль
    input2 = driver.find_element(By.XPATH, "//*[@id=\"password\"]")
    input2.send_keys(PASSWORD)

    # вход в систему
    button = driver.find_element(By.XPATH, "//*[@id=\"LogonFormSubmit\"]")
    button.click()

    # Ждем и кликаем кнопку Добавить
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id=\"gwtAddSrmPurchase\"]"))
    )
    button.click()

    # Ждем появления dropdown метода закупки
    dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[.//option[contains(text(), 'Закупка')]]"))
    )
    dropdown.click()
    time.sleep(1)

    # Выбираем опцию закупки
    option = driver.find_element(By.XPATH,
                                 "//option[contains(text(), 'Закупка (вспомогательные материалы, технические закупки)')]")
    option.click()

    # Кликаем на body чтобы свернуть dropdown
    body = driver.find_element(By.TAG_NAME, "body")
    body.click()
    time.sleep(1)

    # Настройка подписи предложения
    signature_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//td[contains(text(), 'Подпись предложения обязательна')]/following-sibling::td//select"))
    )
    signature_dropdown.click()
    time.sleep(1)

    option_sign = driver.find_element(By.XPATH, "//option[contains(text(), 'нет')]")
    option_sign.click()
    time.sleep(1)

    body.click()
    time.sleep(1)

    # Заполнение наименования закупки
    name_textarea = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//td[contains(text(), 'Наименование закупки')]/following-sibling::td//textarea"))
    )
    name_textarea.clear()
    name_textarea.send_keys(purchase_name)
    time.sleep(1)

    # Нажатие кнопки добавления
    add_button_submit = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "/html/body/div[9]/div/table/tbody/tr[2]/td[2]/div/div/table[2]/tbody/tr/td[1]/button/div/span[1]"))
    )
    add_button_submit.click()
    print("Закупка успешно создана")

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

    # Ждем загрузки формы добавления лота
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "Item.lots.holder.events.newInstanceForm"))
    )

    # 1. Добавление имени лота
    print("Добавляем имя лота...")
    title_textarea = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "title"))
    )
    title_textarea.clear()
    title_textarea.send_keys("Автоматически созданный лот для тестирования")
    print("Имя лота добавлено")

    # 2. Работа с чекбоксом невозможности определения цены
    print("Работаем с чекбоксом невозможности определения цены...")
    price_checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "priceInpossibility"))
    )

    if not price_checkbox.is_selected():
        price_checkbox.click()
        print("Чекбокс отмечен")
    else:
        print("Чекбокс уже отмечен")

    # Заполнение информации о цене
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "priceInfoString"))
    )
    price_info_textarea = driver.find_element(By.ID, "priceInfoString")
    price_info_textarea.clear()
    price_info_textarea.send_keys("Цена будет определена по результатам торгов")
    print("Информация о цене добавлена")

    # 3. Добавление предметов в лот
    print("Ищем кнопку добавления предметов...")

    # Поиск кнопки добавления через GWT компонент
    try:
        add_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class, 'gwt-PushButton') and contains(@title, 'добавить позицию лота')]"))
        )
        add_button.click()
        print("Кнопка добавления предметов найдена и нажата")
        time.sleep(3)
    except:
        print("Кнопка не найдена, пробуем альтернативный способ")
        try:
            add_button = driver.find_element(By.XPATH, "//div[.//img[contains(@src, 'add.png')]]")
            add_button.click()
            print("Кнопка найдена по изображению")
            time.sleep(3)
        except:
            print("Не удалось найти кнопку добавления")

    # 4. Работа с диалоговым окном выбора номенклатуры
    print("Работаем с диалоговым окном выбора номенклатуры...")

    # Ждем появления диалогового окна
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'gwt-DialogBox')]"))
    )

    # Используем поиск для быстрого нахождения элементов
    try:
        search_field = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@class='gwt-TextBox textField']"))
        )
        search_field.clear()
        search_field.send_keys("Говядина 1 сорт")
        time.sleep(2)

        # Ищем элемент в дереве
        beef_1_sort = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Говядина 1 сорт')]"))
        )
        beef_1_sort.click()
        print("Добавлена Говядина 1 сорт")
        time.sleep(1)

        # Очищаем поиск и ищем второй элемент
        search_field.clear()
        search_field.send_keys("Говядина высший сорт")
        time.sleep(2)

        beef_highest_sort = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Говядина высший сорт')]"))
        )
        beef_highest_sort.click()
        print("Добавлена Говядина высший сорт")
        time.sleep(1)

    except Exception as e:
        print(f"Ошибка при поиске элементов: {e}")
        # Альтернативный способ - ручная навигация по дереву
        try:
            # Раскрываем категории
            categories = driver.find_elements(By.XPATH, "//div[contains(@class, 'gwt-TreeItem')]")
            for category in categories:
                if "Товары" in category.text:
                    category.click()
                    time.sleep(1)
                    break

            # Ищем конкретные элементы
            items = driver.find_elements(By.XPATH, "//div[contains(@class, 'gwt-TreeItem')]")
            for item in items:
                if "Говядина 1 сорт" in item.text:
                    item.click()
                    time.sleep(1)
                elif "Говядина высший сорт" in item.text:
                    item.click()
                    time.sleep(1)

        except Exception as e2:
            print(f"Ошибка при ручной навигации: {e2}")

    # 5. Сохранение выбора
    try:
        save_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(), 'Сохранить')]]"))
        )
        save_button.click()
        print("Элементы добавлены в лот")
        time.sleep(3)
    except Exception as e:
        print(f"Не удалось найти кнопку Сохранить: {e}")

    # 6. Заполнение обязательных полей
    print("Заполняем обязательные поля лота...")

    try:
        supply_periods = driver.find_element(By.ID, "supplyPeriods")
        supply_periods.clear()
        supply_periods.send_keys("В течение 30 дней после заключения договора")
        print("Срок поставки указан")
    except Exception as e:
        print(f"Ошибка при заполнении срока поставки: {e}")

    try:
        requirements = driver.find_element(By.ID, "requirementsRelatedWork")
        requirements.clear()
        requirements.send_keys("Соответствие ГОСТ. Упаковка должна обеспечивать сохранность товара.")
        print("Дополнительные условия указаны")
    except Exception as e:
        print(f"Ошибка при заполнении дополнительных условий: {e}")

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
    except Exception as e:
        print(f"Ошибка при нажатии кнопки Добавить: {e}")

    # 8. добавление извещения
    try:
        # Переключаемся на основное окно
        main_window = driver.window_handles[0]
        driver.switch_to.window(main_window)

        # Ждем кнопку создания извещения
        create_notification = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[contains(@id, 'rebiddingNoticeSubmit') or contains(text(), 'Извещение')]"))
        )

        create_notification.click()
        print("Открываем окно извещения...")
        time.sleep(5)

        # Переключаемся на новое окно
        new_windows = driver.window_handles
        if len(new_windows) > 1:
            driver.switch_to.window(new_windows[-1])
            print("Переключились на окно извещения")

        # Ждем загрузки формы
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # Проверяем iframe
        if switch_to_correct_frame(driver):
            print("Нашли форму в iframe")

        # Работа с формой извещения
        try:
            # Чекбокс "Совпадает с датой"
            time_checkbox = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "//input[@type='checkbox' and (contains(@id, 'equalPublication') or contains(@name, 'equalPublication'))]"))
            )
            time_checkbox.click()

            # Кнопка сохранения
            safe_button = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "//input[@type='submit' and (contains(@id, 'commit') or contains(@value, 'Сохранить'))] | //button[contains(text(), 'Сохранить')]"))
            )
            driver.execute_script("window.scrollBy(0, 41);")
            safe_button.click()
            print("Извещение сохранено")

        except Exception as e:
            debug_scroll_issue(driver)
            print(f"Ошибка в форме извещения: {e}")
            driver.save_screenshot("form_error.png")


        # Возвращаемся к основному окну
        driver.switch_to.window(main_window)

    except Exception as e:
        print(f"Ошибка при работе с извещением: {e}")

except TimeoutException:
    print("Элемент не найден в течение времени ожидания")
except NoSuchElementException:
    print("Элемент не существует на странице")
except Exception as e:
    print(f"Произошла ошибка: {str(e)}")
    # Делаем скриншот для отладки
    driver.save_screenshot("error_screenshot.png")
finally:
    time.sleep(5)
    driver.quit()
