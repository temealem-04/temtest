import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

@pytest.fixture(scope="module")
def browser():
    # Initialize the Chrome WebDriver instance
    driver = webdriver.Chrome()
    yield driver
    # Quit the WebDriver instance after the test completes
    driver.quit()

def test_facebook_login(browser):
    # Open the Facebook login page
    browser.get("https://www.facebook.com")

    # Enter the username and password in the login form
    sleep(5)
    username_input = browser.find_element_by_id("email")
    password_input = browser.find_element_by_id("pass")
    username_input.send_keys("")
    password_input.send_keys("your_password")

    # Submit the login form
    password_input.send_keys(Keys.RETURN)

    # Verify successful login by checking for the presence of a specific element on the logged-in page
    assert browser.find_element_by_id("userNavigationLabel").is_displayed()

