**`Чтобы воспользоваться этой программой сначала надо установить: Python и ChromeDriver`**


                                                    Установка Python
- С сайта `https://www.python.org/downloads/`  скачативаем **Python 3.13**, так как при написании этого кода я использовал именно эту версию. После чего проходим стандартный этап установки программы на компьютер, главное на этапе установки не забыть утановить калочку в поле `Add "bin" folder to the PATH`<img width="425" height="209" alt="image" src="https://github.com/user-attachments/assets/6dc42c6a-49ca-46e5-b3a8-78ae6ad5ac51" />
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
