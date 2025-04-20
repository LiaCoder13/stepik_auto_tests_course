from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:   
    link = "http://suninjuly.github.io/file_input.html"   
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код
    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys("Sveta")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys("Petrova")
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys("sp@gmail.com") 
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'text_lesson2-2_step8.txt')           # добавляем к этому пути имя файла 
    element = browser.find_element(By.CSS_SELECTOR, "[name='file']")
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()