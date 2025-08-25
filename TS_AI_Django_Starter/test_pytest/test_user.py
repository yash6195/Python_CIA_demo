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

def test_add_and_verify_user(driver):
    # Navigate to the application
    driver.get("http://127.0.0.1:5000/")

    # Navigate to users page
    users_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-bs-target='#users']"))
    )
    users_button.click()

    # Add a new user
    user_name_input = driver.find_element(By.ID, "userName")
    user_email_input = driver.find_element(By.ID, "userEmail")
    add_user_button = driver.find_element(By.CSS_SELECTOR, "#users .btn-primary")

    user_name_input.send_keys("ui_user")
    user_email_input.send_keys("ui_user@example.com")
    add_user_button.click()

    # Verify the user was added
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-bs-target='#search']"))
    )
    search_button.click()

    search_user_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#search .btn-secondary"))
    )
    search_user_button.click()
    
    page_source = driver.page_source
    assert "ui_user" in page_source
    assert "ui_user@example.com" in page_source
