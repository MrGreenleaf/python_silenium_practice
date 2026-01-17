# 1. Откройте https://ya.ru
# 2. Выведите текущий URL и заголовок
# 3. Обновите страницу (refresh)
# 4. Выведите новый заголовок для проверки
# 5. Закройте браузер

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('http://google.com')
print(driver.title)
driver.refresh()
page_title = driver.title
print(page_title)
driver.quit