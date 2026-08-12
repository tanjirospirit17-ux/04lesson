from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self, product_id):
        locator = f"#add-to-cart-{product_id}"
        self.driver.find_element(By.CSS_SELECTOR, locator).click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()