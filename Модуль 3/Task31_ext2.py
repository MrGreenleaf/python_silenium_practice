# 1. Откройте https://google.com
# 2. Перейдите на https://yandex.ru (get)
# 3. Вернитесь назад (back) на Google
# 4. Выведите URL после возврата
# 5. Перейдите вперёд (forward) обратно на Яндекс
# 6. Закройте браузер

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)

# применил implicitly_wait потому что яндекс долго редикректился грузился
driver.get('https://google.com')
driver.implicitly_wait(10)
print(driver.title)

driver.get('https://yandex.ru')
driver.implicitly_wait(10)
print(driver.title)

driver.back()
driver.implicitly_wait(10)
print(driver.title)

driver.forward()
driver.implicitly_wait(10)
print(driver.title)
driver.close()