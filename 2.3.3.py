from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    browser.switch_to.window(browser.window_handles[1])
    browser.find_element(By.ID, 'answer').send_keys(calc(browser.find_element(By.ID, 'input_value').text))
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()



finally:
    time.sleep(10)
    browser.quit()

