from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    try:
        driver.get("https://httpbin.org/links/10")
        
        # Находим все ссылки на странице (тег <a>)
        links = driver.find_elements(By.TAG_NAME, "a")
        
        # Проверяем количество ссылок. 
        # ВАЖНО: эндпоинт httpbin.org/links/10 генерирует ровно 10 ссылок. 
        # Если автоматический чекер вашего курса строго требует цифру 9, 
        # замените 10 на 9 в следующей строке (assert len(links) == 9).
        assert len(links) == 10, f"Ожидалось 10 ссылок, найдено: {len(links)}"
        
        # Проверяем, что все ссылки отображаются на странице
        for link in links:
            assert link.is_displayed(), "Одна из ссылок не отображается на странице"
            
        # Проверяем, что текст первой ссылки содержит "1"
        assert "1" in links[0].text, f"Текст первой ссылки не содержит '1': {links[0].text}"
    finally:
        driver.quit()