from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math, time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.ID, 'book')
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID,
                                                                            'price'), '$100'))
    button.click()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.CSS_SELECTOR, '#answer')
    input.send_keys(y)
    button2 = browser.find_element(By.CSS_SELECTOR, '#solve')
    button2.click()

    time.sleep(10)
    browser.quit()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()