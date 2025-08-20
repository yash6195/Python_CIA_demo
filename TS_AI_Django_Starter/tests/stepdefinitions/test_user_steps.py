import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_bdd import scenarios, given, when, then, parsers

scenarios('../features/users.feature')

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@given("I go to users page")
def navigate_to_user_page(driver):
    driver.get("http://127.0.0.1:5000")
    driver.find_element(By.CSS_SELECTOR, "button[data-bs-target='#users']").click()

@when(parsers.parse('I add a user "{username}" with email "{email}"'))
def add_user(driver, username, email):
    driver.find_element(By.ID, "userName").send_keys(username)
    driver.find_element(By.ID, "userEmail").send_keys(email)
    driver.find_element(By.CSS_SELECTOR, "#users .btn-primary").click()

@then(parsers.parse("I should see the user created in the UI"))
def verify_user(driver):
    driver.find_element(By.CSS_SELECTOR, "button[data-bs-target='#search']").click()
    driver.find_element(By.CSS_SELECTOR, ".btn-secondary").click()
    time.sleep(3)
    page_src = driver.page_source
    assert "ui_user" in page_src
