import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_bdd import scenarios, given, when, then, parsers

scenarios('../features/tasks.feature')

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@given("I go to tasks page")
def navigate_to_user_page(driver):
    driver.get("http://127.0.0.1:5000")
    driver.find_element(By.CSS_SELECTOR, "button[data-bs-target='#tasks']").click()

@when(parsers.parse('I add a task with title "{title}"'))
def add_user(driver, title):
    driver.find_element(By.ID, "taskTitle").send_keys(title)
    driver.find_element(By.CSS_SELECTOR, "#tasks .btn-primary").click()

@then(parsers.parse("I should see the task created in the UI"))
def verify_user(driver):
    driver.find_element(By.CSS_SELECTOR, "button[data-bs-target='#search']").click()
    driver.find_element(By.CSS_SELECTOR, ".btn-secondary").click()
    time.sleep(3)
    page_src = driver.page_source
    assert "sell cars" in page_src


