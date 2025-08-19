# tests/locators/product_locators.py
from selenium.webdriver.common.by import By

class ProductLocators:
    ADD_BTN = (By.ID, "add-product-btn")
    NAME_INPUT = (By.NAME, "name")
    PRICE_INPUT = (By.NAME, "price")
    STOCK_INPUT = (By.NAME, "stock")
    SUBMIT_BTN = (By.ID, "submit-btn")
