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

def test_add_and_verify_task(driver):
    # Navigate to the application
    driver.get("http://127.0.0.1:8000/")

    # Navigate to tasks page
    tasks_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-bs-target='#tasks']"))
    )
    tasks_button.click()

    # Add a new task
    task_title_input = driver.find_element(By.ID, "taskTitle")
    add_task_button = driver.find_element(By.CSS_SELECTOR, "#tasks .btn-primary")

    task_title_input.send_keys("sell cars")
    add_task_button.click()

    # Verify the task was added
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-bs-target='#search']"))
    )
    search_button.click()

    search_task_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#search .btn-secondary"))
    )
    search_task_button.click()
    
    page_source = driver.page_source
    assert "sell cars" in page_source
