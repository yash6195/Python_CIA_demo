# tests/pages/product_page.py
from tests.pages.base_page import BasePage
from tests.locators.product_locators import ProductLocators

class ProductPage(BasePage):
    def open(self):
        self.driver.get("http://localhost:8000/products")

    def add_product(self, name, price, stock):
        self.click(*ProductLocators.ADD_BTN)
        self.type(*ProductLocators.NAME_INPUT, name)
        self.type(*ProductLocators.PRICE_INPUT, price)
        self.type(*ProductLocators.STOCK_INPUT, stock)
        self.click(*ProductLocators.SUBMIT_BTN)
