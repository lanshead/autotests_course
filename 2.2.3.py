from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


'''В этом задании в форме регистрации требуется загрузить текстовый файл.

Напишите скрипт, который будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"
Если все сделано правильно и быстро, вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.'''

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]').send_keys('Tommas')
    browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]').send_keys('Raddle')
    browser.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys('mortdevolanlord@hogwarts.com')
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'ООП 9.1.13.txt')
    browser.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()


finally:
    time.sleep(10)
    browser.quit()

