"""Фикстуры для инициализации драйвера и параметров."""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

@pytest.fixture(scope="function")
def driver() -> WebDriver:
    """Создает и закрывает экземпляр WebDriver."""
    options = Options()
    # options.add_argument("--headless") # Раскомментируйте для запуска без интерфейса
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def base_url() -> str:
    """Возвращает базовый URL для тестов."""
    return "https://www.saucedemo.com/" # Замените на ваш URL из ДЗ 7