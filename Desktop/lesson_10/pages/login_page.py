"""Модуль с описанием страниц (Page Objects)."""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

class LoginPage:
    """Page Object для страницы авторизации."""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self._username_locator = (By.ID, "user-name")
        self._password_locator = (By.ID, "password")
        self._login_button_locator = (By.ID, "login-button")

    @allure.step("Открыть страницу по URL: {url}")
    def open_page(self, url: str) -> "LoginPage":
        """Открывает страницу в браузере.
        
        Args:
            url: Строка с адресом страницы.
            
        Returns:
            Экземпляр текущего класса для цепочки вызовов.
        """
        self.driver.get(url)
        return self

    @allure.step("Ввести имя пользователя: {username}")
    def enter_username(self, username: str) -> "LoginPage":
        """Вводит имя пользователя в поле ввода.
        
        Args:
            username: Строка с именем пользователя.
            
        Returns:
            Экземпляр текущего класса.
        """
        self.driver.find_element(*self._username_locator).send_keys(username)
        return self

    @allure.step("Ввести пароль: {password}")
    def enter_password(self, password: str) -> "LoginPage":
        """Вводит пароль в поле ввода.
        
        Args:
            password: Строка с паролем.
            
        Returns:
            Экземпляр текущего класса.
        """
        self.driver.find_element(*self._password_locator).send_keys(password)
        return self

    @allure.step("Нажать кнопку входа")
    def click_login_button(self) -> None:
        """Нажимает на кнопку входа. Не возвращает значения."""
        self.driver.find_element(*self._login_button_locator).click()

    @allure.step("Проверить наличие элемента на странице")
    def is_element_present(self, locator: tuple) -> bool:
        """Проверяет наличие элемента по локатору.
        
        Args:
            locator: Кортеж с типом локатора и его значением.
            
        Returns:
            True, если элемент найден, иначе False.
        """
        return len(self.driver.find_elements(*locator)) > 0