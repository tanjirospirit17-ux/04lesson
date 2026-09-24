from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    URL = (
        "https://bonigarcia.dev/selenium-webdriver-java/"
        "slow-calculator.html"
    )

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, delay_value):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(delay_value))

    def click_button(self, value):
        xpath = f"//span[text()='{value}']"
        button = self.driver.find_element(By.XPATH, xpath)
        button.click()

    def wait_for_result(self, result_text, timeout=50):
        result_locator = (By.CSS_SELECTOR, ".screen")
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(
                result_locator, result_text
            )
        )

    def get_result(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text