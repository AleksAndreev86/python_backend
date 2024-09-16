from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > input:nth-child(2)')
    input1.send_keys("Aleksandr")
    input2 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > input:nth-child(4)')
    input2.send_keys("Andreev")
    input3 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > input:nth-child(6)')
    input3.send_keys("mrak808@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element(By.CSS_SELECTOR, '#file')
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)
    browser.quit()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()