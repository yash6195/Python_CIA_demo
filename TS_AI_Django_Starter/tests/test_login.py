import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.visit("http://localhost:8000/login")  # Adjust URL
    login_page.login("alice", "password123")         # Adjust credentials
    assert "Dashboard" in driver.page_source
