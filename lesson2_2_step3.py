from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    label1 = browser.find_element(By.CSS_SELECTOR,'#num1').text
    label2 = browser.find_element(By.CSS_SELECTOR,'#num2').text
    counter = str(int(label1) + int(label2))
    select = Select(browser.find_element(By.CSS_SELECTOR, '#dropdown'))
    select.select_by_value(counter)

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