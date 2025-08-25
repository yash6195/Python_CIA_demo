import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # Setup WebDriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    # Teardown WebDriver
    driver.quit()

def test_add_and_verify_product(driver):
    # Navigate to the application
    driver.get("http://127.0.0.1:8000/")

    # Navigate to products page
    products_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-bs-target='#products']"))
    )
    products_button.click()

    # Add a new product
    product_name_input = driver.find_element(By.ID, "productName")
    product_price_input = driver.find_element(By.ID, "productPrice")
    add_product_button = driver.find_element(By.CSS_SELECTOR, "#products .btn-primary")

    product_name_input.send_keys("car")
    product_price_input.send_keys("100000")
    add_product_button.click()

    # Verify the product was added
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-bs-target='#search']"))
    )
    search_button.click()

    search_product_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#search .btn-secondary"))
    )
    search_product_button.click()
    
    page_source = driver.page_source
    assert "car" in page_source
    assert "100000" in page_source
