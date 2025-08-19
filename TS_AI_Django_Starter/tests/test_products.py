# tests/test_products.py
from tests.pages.product_page import ProductPage

def test_add_product(driver):
    product_page = ProductPage(driver)
    product_page.open()
    product_page.add_product("Test Product", "199", "10")
    assert product_page.is_text_present("Test Product")
