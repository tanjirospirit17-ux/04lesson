"""Модуль с автотестами для функционала авторизации."""
import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from pages.login_page import LoginPage

@allure.feature("Авторизация")
class TestLogin:
    """Класс с тестами для проверки функционала входа в систему."""

    @allure.title("Успешный вход в систему с валидными данными")
    @allure.description("Проверка возможности успешного входа пользователя с корректным логином и паролем.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_login(self, driver: WebDriver, base_url: str) -> None:
        """Тест на успешную авторизацию.
        
        Args:
            driver: Экземпляр WebDriver из фикстуры.
            base_url: Базовый URL приложения из фикстуры.
        """
        page = LoginPage(driver)

        with allure.step("Открыть главную страницу приложения"):
            page.open_page(base_url)

        with allure.step("Ввести валидные учетные данные"):
            page.enter_username("standard_user").enter_password("secret_sauce")

        with allure.step("Нажать кнопку 'Войти'"):
            page.click_login_button()

        with allure.step("Проверить, что вход выполнен успешно (проверка URL или элемента)"):
            # Замени 'inventory' на часть URL или локатор элемента из твоего ДЗ №7
            assert "inventory" in driver.current_url, "Перенаправление после входа не сработало!"