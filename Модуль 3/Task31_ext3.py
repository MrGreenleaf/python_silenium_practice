# 1. Откройте http://ya.ru (обратите внимание на http)
# 2. Выведите текущий URL (должен измениться на https)
# 3. Выведите заголовок страницы
# 4. Получите HTML-код страницы (page_source)
# 5. Найдите в коде слово "Яндекс" (проверьте наличие)
# 6. Закройте браузер

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)

# применил implicitly_wait потому что яндекс долго редикректился грузился

driver.get('http://ya.ru')
print(driver.current_url)
driver.implicitly_wait(5)
print(driver.title)

page_source = driver.page_source
print(f"\n4. Размер HTML: {len(page_source)} символов")

print(f"\n5. Поиск слова 'Яндекс'...")
    
    # проверка наличия
if "Яндекс" in page_source:
    print("   ✓ Слово 'Яндекс' найдено на странице")
else:
    print("   ✗ Слово 'Яндекс' НЕ найдено")

driver.close
driver.quit