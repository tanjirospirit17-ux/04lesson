from selenium import webdriver
from calculator_page import CalculatorPage


def test_calculator():
    driver = webdriver.Chrome()
    driver.maximize_window()
    page = CalculatorPage(driver)
    try:
        page.open()
        page.set_delay(45)
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

        # Ожидаем появления результата (с запасом по времени)
        page.wait_for_result("15", timeout=50)
        assert page.get_result() == "15"
    finally:
        driver.quit()