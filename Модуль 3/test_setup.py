from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Убедитесь, что chromedriver.exe версии 143 в папке проекта
service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Ваш тест
driver.get('https://www.google.com')
print(driver.title)
driver.quit()