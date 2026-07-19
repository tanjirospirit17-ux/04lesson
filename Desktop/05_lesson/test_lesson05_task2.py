from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    try:
        driver.get("https://httpbin.org/forms/post")
        
        # Находим поле ввода с названием custname и вводим имя
        driver.find_element(By.NAME, "custname").send_keys("Huy")
        
        # Находим кнопку Submit и нажимаем на нее
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        # Проверяем, что после нажатия URL изменился (должен стать /post)
        assert "/post" in driver.current_url, f"Ожидался /post в URL, получен: {driver.current_url}"
    finally:
        driver.quit()