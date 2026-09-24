from selenium import webdriver

from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_step_one_page import CheckoutStepOnePage
from checkout_step_two_page import CheckoutStepTwoPage


def test_shop():
    driver = webdriver.Firefox()
    driver.maximize_window()

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_step_one = CheckoutStepOnePage(driver)
    checkout_step_two = CheckoutStepTwoPage(driver)

    try:
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page.add_product_to_cart("sauce-labs-backpack")
        inventory_page.add_product_to_cart("sauce-labs-bolt-t-shirt")
        inventory_page.add_product_to_cart("sauce-labs-onesie")
        inventory_page.go_to_cart()

        # Проверка содержимого корзины (инкапсулирована в PO, assert в тесте)
        assert len(cart_page.get_cart_items()) == 3
        cart_page.click_checkout()

        checkout_step_one.fill_info("Иван", "Иванов", "12345")

        total_price = checkout_step_two.get_total_price()
        assert total_price == "Total: $58.29"
    finally:
        driver.quit()