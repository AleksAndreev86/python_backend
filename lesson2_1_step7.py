from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    elem = x_element.get_attribute("valuex")
    y = calc(elem)

    input1 = browser.find_element(By.CSS_SELECTOR,'#answer')
    input1.send_keys(y)
    checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    checkbox.click()
    radiobutton2 = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radiobutton2.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > div > button")
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