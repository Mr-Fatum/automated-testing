<img width="656" height="405" alt="image" src="https://github.com/user-attachments/assets/448202f8-adee-4750-8b09-6d49cf510b10" />**`Чтобы воспользоваться этой программой сначала надо установить: Python и ChromeDriver`**


                                                    Установка Python
- С сайта `https://www.python.org/downloads/`  скачативаем **Python 3.13**, так как при написании этого кода я использовал именно эту версию. После чего проходим стандартный этап установки программы на компьютер, главное на этапе установки не забыть утановить калочку в поле `Add python.exe to PATH` <img width="656" height="405" alt="image" src="https://github.com/user-attachments/assets/535ffebb-2e44-45fd-8d66-387ee45712cb" />

- При необходимости более удобного использования и доработки кода советую установить среду разработки PyCharm

                                                Установка ChromeDriver
- С сайта `https://sites.google.com/chromium.org/driver/ (старая версия сайта https://sites.google.com/a/chromium.org/chromedriver/downloads)` скачиваем ту версию драйвера, которая соответсвтует версии вашего браузера(её можно проверить написав в поисковой строке `chrome://version/`
- Создайте на диске C: папку chromedriver и положите разархивированный ранее файл chromedriver.exe в папку C:\chromedriver.
- Добавьте в системную переменную PATH папку C:\chromedriver. Как это сделать в разных версиях Windows, описано здесь: `https://www.computerhope.com/issues/ch000549.htm`.

                                Пример: как добавить путь в системную переменную PATH на Windows 10

**1. Откройте настройки системы.**

**2. В настройках откройте вкладку About, затем System info:**

<img width="841" height="407" alt="image" src="https://github.com/user-attachments/assets/645f489f-108f-4dd6-a5fa-f1e388dcde8b" />

**3. Выберите Advanced system settings:**

<img width="495" height="413" alt="image" src="https://github.com/user-attachments/assets/6639207d-17fd-42e6-afb5-238e5fcf51ed" />

**4. Выберите Environment Variables:**

<img width="499" height="616" alt="image" src="https://github.com/user-attachments/assets/889362ca-42b2-4c4b-a985-12bfa6bb346c" />

**5. Кликните два раза на строчке Path в System variables:**

<img width="616" height="581" alt="image" src="https://github.com/user-attachments/assets/72f58130-5ee9-4103-852d-d5f9e4514799" />

**6. Нажмите кнопку New. Введите в новую строку путь к ChromeDriver — C:\chromedriver. Нажмите Enter. У вас должна появится строка с указанным путем:**

<img width="618" height="585" alt="image" src="https://github.com/user-attachments/assets/2b4c7f34-13c4-4678-b900-1e2f0592ec8a" />

**7. Если у вас была открыта командная строка Windows, не забудьте ее закрыть. Затем откройте новую командную строку, чтобы изменения переменной окружения стали доступны. Активируйте снова виртуальное окружение selenium_env, которое мы создали в предыдущих шагах.**

**Давайте убедимся в том, что вебдрайвер установлен правильно.**

**Для начала проверим содержимое переменной path, для этого наберем в командной строке Path:** 

<img width="664" height="171" alt="image" src="https://github.com/user-attachments/assets/ffedf28a-822d-4996-b1fa-3bffa275af18" />

**Ура, там есть папка с chromedriver! Попробуем вызвать его напрямую из командной строки:** 

<img width="647" height="94" alt="image" src="https://github.com/user-attachments/assets/0149a5a7-673d-47dd-ad05-1a69629acfe3" />

**Магия переменной path: хотя программа chromedriver находится где-то в другом каталоге, мы можем напрямую открывать её, используя имя chromedriver. Чтобы завершить процесс в консоли, нажмите Ctrl+C.** 

**Знак на этом этапе, что пошло что-то не так:** 

<img width="485" height="47" alt="image" src="https://github.com/user-attachments/assets/faf8b398-2672-433a-a355-c1795a9b2b4e" />

**В таком случае попробуйте перезапустить консоль, перезапустить компьютер, перепроверить и добавить заново по инструкциям папку с chromedriver в переменную path.**

**`P.S. вся информация по устрановке chromedriver была взята из курса на платформе Stepik:  https://stepik.org/lesson/25969/step/8`**

                                Устанавливаем PyCharm для более удоьбного и быстрого взаимодействия с кодом
- Скачиваем с сайта JetBrains `https://www.jetbrains.com/pycharm/download/?section=windows` установщик для своего компьютера
- При установке не забываем снова изменить значение чекбокса `Add "bin" folder to the PATH`
  
<img width="499" height="388" alt="image" src="https://github.com/user-attachments/assets/200df839-4be7-4860-9bcc-616d83064b2d" />

- Далее всё без изменений, проходим уже знакомую процедуру установки приложения

                            Открываем репозиторий в PyCharm и запускаем код
  
- Чтобы клонировать репозиторий на свой компьютер, заходим в приложение и переходим во вкладку "Clone Repository"

<img width="984" height="712" alt="image" src="https://github.com/user-attachments/assets/23f49666-2d63-4fbe-85b3-63be4eee01dd" />

- Копируем ссылку на репозиторий нажав на кнопку `Code` и вставляем в соответствующее поле для клонирования репозитория в PyCharm и нажимаем кнопку `clone`

  <img width="2560" height="1316" alt="image" src="https://github.com/user-attachments/assets/f077e2a3-1b58-4bda-9207-890935f29a5f" />

  <img width="1000" height="720" alt="image" src="https://github.com/user-attachments/assets/2fa50ac5-0198-4c89-9af8-644ed339da4f" />

- После открытия репозитория необходимо добавить интерпретатор python. Открываем файл с названием `auto_lot.py`, он находится в папке `testing` и видим в окне с кодом надпись "No Python interpreter for the project", справа от неё будет кликабельная надпись "Configure Python interpreter".

<img width="1384" height="992" alt="image" src="https://github.com/user-attachments/assets/d5512f53-bd0a-41bb-909c-afd6c32759d3" />

- Далее нажимаем "Add New Interpreter" -> "Add Local Interpreter"

<img width="1384" height="992" alt="image" src="https://github.com/user-attachments/assets/11bd66dc-baec-4028-9fc8-c6525c1332a4" />

- Автоматически будет выбран ранее установленный python 3.13 и нам остаётся только нажать `OK`

<img width="624" height="312" alt="image" src="https://github.com/user-attachments/assets/b65b506a-6b28-4c94-99f1-7a5966905fd6" />

- Дождавшись установки всех файлов смотрим на добавленные библиотеки в файле `auto_lot.py`, так как без из добавления программа просто не запустится. Наводим курсор на слово selenium и нажимаем на него правой кнопкой мышки далее в открывшемся контекстном меню заходим в `Show Context Actions` и нажимаем `install package selenium`

<img width="1384" height="992" alt="image" src="https://github.com/user-attachments/assets/e02e6125-628b-42ae-818d-af9eff343fbf" />

<img width="1384" height="992" alt="image" src="https://github.com/user-attachments/assets/dceb98d4-9b8f-40a1-83cf-1281c16f72dd" />

- Снова дожидаемся установки и теперь мы можеи запустить файл нажав на кнопку Run на верхней панели

<img width="1384" height="992" alt="image" src="https://github.com/user-attachments/assets/0efd53a4-38df-4818-899d-aaa3a16160fd" />
