"""Модуль с описанием страницы авторизации SauceDemo (Page Object)."""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Page Object для страницы входа в систему SauceDemo."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует LoginPage с драйвером и локаторами.
        
        Args:
            driver: Экземпляр WebDriver для управления браузером.
        """
        self.driver = driver
        self._username_locator = (By.ID, "user-name")
        self._password_locator = (By.ID, "password")
        self._login_button_locator = (By.ID, "login-button")
        self._error_locator = (By.CSS_SELECTOR, ".error-message-container")
        self._inventory_locator = (By.CLASS_NAME, "inventory_list")

    @allure.step("Открыть страницу авторизации по URL: {url}")
    def open_page(self, url: str) -> "LoginPage":
        """Открывает страницу входа в браузере.
        
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

    @allure.step("Получить текст сообщения об ошибке")
    def get_error_message(self) -> str:
        """Возвращает текст сообщения об ошибке авторизации.
        
        Returns:
            Строка с текстом ошибки или пустая строка.
        """
        error_elements = self.driver.find_elements(*self._error_locator)
        if error_elements:
            return error_elements[0].text
        return ""

    @allure.step("Проверить наличие элемента инвентаря на странице")
    def is_inventory_present(self) -> bool:
        """Проверяет наличие списка товаров после успешного входа.
        
        Returns:
            True, если элемент найден, иначе False.
        """
        return len(self.driver.find_elements(*self._inventory_locator)) > 0

    @allure.step("Получить текущий URL страницы")
    def get_current_url(self) -> str:
        """Возвращает текущий URL в адресной строке браузера.
        
        Returns:
            Строка с текущим URL.
        """
        return self.driver.current_url