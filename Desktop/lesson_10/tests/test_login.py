"""Модуль с автотестами для функционала авторизации SauceDemo."""
import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from pages.login_page import LoginPage


@allure.feature("Авторизация")
class TestLogin:
    """Класс с тестами для проверки функционала входа в систему SauceDemo."""

    @allure.title("Успешный вход в систему с валидными данными")
    @allure.description(
        "Этот тест проверяет возможность успешного входа пользователя "
        "standard_user с корректным паролем secret_sauce. "
        "После входа пользователь должен попасть на страницу инвентаря."
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_login(self, driver: WebDriver, base_url: str) -> None:
        """Тест на успешную авторизацию с валидными данными.
        
        Args:
            driver: Экземпляр WebDriver из фикстуры.
            base_url: Базовый URL приложения из фикстуры.
        """
        page = LoginPage(driver)

        with allure.step("Открыть страницу авторизации SauceDemo"):
            page.open_page(base_url)

        with allure.step("Ввести валидные учетные данные"):
            page.enter_username("standard_user").enter_password("secret_sauce")

        with allure.step("Нажать кнопку 'Login'"):
            page.click_login_button()

        with allure.step("Проверить наличие списка товаров на странице"):
            assert page.is_inventory_present(), "Список товаров не найден после входа!"

        with allure.step("Проверить, что URL изменился на страницу инвентаря"):
            assert "inventory" in page.get_current_url(), "URL не изменился на /inventory.html!"

    @allure.title("Вход в систему с невалидным паролем")
    @allure.description(
        "Этот тест проверяет, что при вводе некорректного пароля "
        "система показывает сообщение об ошибке и не пускает пользователя внутрь."
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_with_invalid_password(self, driver: WebDriver, base_url: str) -> None:
        """Тест на вход с неверным паролем.
        
        Args:
            driver: Экземпляр WebDriver из фикстуры.
            base_url: Базовый URL приложения из фикстуры.
        """
        page = LoginPage(driver)

        with allure.step("Открыть страницу авторизации SauceDemo"):
            page.open_page(base_url)

        with allure.step("Ввести валидный логин и невалидный пароль"):
            page.enter_username("standard_user").enter_password("wrong_password")

        with allure.step("Нажать кнопку 'Login'"):
            page.click_login_button()

        with allure.step("Получить текст сообщения об ошибке"):
            error_message = page.get_error_message()

        with allure.step("Проверить, что сообщение об ошибке не пустое"):
            assert error_message != "", "Сообщение об ошибке не появилось!"

        with allure.step("Проверить содержание сообщения об ошибке"):
            assert "Username and password do not match" in error_message
