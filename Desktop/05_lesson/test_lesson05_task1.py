from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    try:
        driver.get("https://httpbin.org/")
        
        # Находим и кликаем на ссылку, ведущую на форму (HTML Forms)
        # Использование CSS-селектора по атрибуту href является наиболее надежным
        driver.find_element(By.CSS_SELECTOR, "a[href='/forms/post']").click()
        
        # Проверяем, что URL изменился на /forms/post
        assert "/forms/post" in driver.current_url, f"Ожидался /forms/post в URL, получен: {driver.current_url}"
        
        # Возвращаемся назад на главную страницу
        driver.back()
        
        # Проверяем, что вернулись на исходный URL
        assert driver.current_url == "https://httpbin.org/", f"Ожидался https://httpbin.org/, получен: {driver.current_url}"
    finally:
        # Гарантируем закрытие браузера даже в случае падения теста
        driver.quit()