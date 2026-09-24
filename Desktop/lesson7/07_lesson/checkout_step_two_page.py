from selenium.webdriver.common.by import By


class CheckoutStepTwoPage:
    def __init__(self, driver):
        self.driver = driver

    def get_total_price(self):
        total_element = self.driver.find_element(
            By.CLASS_NAME, "summary_total_label"
        )
        return total_element.text