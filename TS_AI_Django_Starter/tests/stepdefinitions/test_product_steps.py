import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_bdd import scenarios, given, when, then, parsers

scenarios('../features/product.feature')

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@given("I go to products page")
def navigate_to_product_page(driver):
    driver.get("http://127.0.0.1:5000")
    driver.find_element(By.CSS_SELECTOR, "button[data-bs-target='#products']").click()

@when(parsers.parse('I add a product "{name}" with price "{price}"'))
def add_product(driver, name, price):
    driver.find_element(By.ID, "productName").send_keys(name)
    driver.find_element(By.ID, "productPrice").send_keys(price)
    driver.find_element(By.CSS_SELECTOR, "#products .btn-primary").click()

@then(parsers.parse("I should see the product created in the UI"))
def verify_product(driver):
    driver.find_element(By.CSS_SELECTOR, "button[data-bs-target='#search']").click()
    driver.find_element(By.CSS_SELECTOR, ".btn-secondary").click()
    page_src = driver.page_source
    assert "car" in page_src
