import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PageObject.login_page import LoginPage
from PageObject.base_page import BasePage


@pytest.fixture(scope="function")
def driver():
   """Setup WebDriver"""
   driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
   driver.maximize_window()
   """Test Executes Here"""
   yield driver
   """Cleanup after Test"""
   driver.quit()


# Test Case 1: Verify if the home URL is valid
def test_verify_home_url(driver):
    base_page = BasePage(driver)
    base_page.navigate_to("https://www.guvi.in/")
    time.sleep(30)
    assert driver.current_url == "https://www.guvi.in/", f"URL mismatch! Expected: https://www.guvi.in/, Found: {driver.current_url}"
    print("SUCCESS: URL is valid.")

    time.sleep(30)
# Test Case 2: Verify webpage title
def test_verify_webpage_title(driver):
    base_page = BasePage(driver)
    base_page.navigate_to("https://www.guvi.in")
    expected_title = "GUVI | Learn to code in your native language"
    actual_title = base_page.get_title()
    assert actual_title == expected_title, f"Title mismatch! Expected: '{expected_title}', Found: '{actual_title}'"
    print("SUCCESS: Title matches.")

# Test Case 3: Verify login button visibility & clickability
def test_verify_login_button(driver):
    login_page = LoginPage(driver)
    login_page.navigate_to_login_page()
    assert login_page.is_login_button_visible(), "Login button is NOT visible!"
    assert login_page.is_login_button_clickable(), "Login button is NOT clickable!"
    print("SUCCESS: Login button is visible and clickable.")

# Test Case 4: Verify sign-up button visibility & clickability
def test_verify_signup_button(driver):
    base_page = BasePage(driver)
    base_page.navigate_to("https://www.guvi.in")
    sign_up_button = (By.XPATH, "//a[text()='Sign up']")   # Replace if needed
    assert base_page.is_visible(sign_up_button), "Sign-up button is NOT visible!"
    assert base_page.is_clickable(sign_up_button) is not None, "Sign-up button is NOT clickable!"
    print("SUCCESS: Sign-up button is visible and clickable.")


# Test Case 5: Verify navigation to sign-in page via Sign-Up button
def test_verify_signin_navigation(driver):
    base_page = BasePage(driver)
    base_page.navigate_to("https://www.guvi.in/sign-in/")
    assert driver.current_url == "https://www.guvi.in/sign-in/", f"Navigation failed! Expected URL: https://www.guvi.in/sign-in/, Found: {driver.current_url}"
    print("SUCCESS: Navigation to sign-in page confirmed.")


# Test Case 6: Verify login and logout functionality
def test_verify_login_logout(driver):
    login_page = LoginPage(driver)
    login_page.navigate_to_login_page()
    login_page.click_login()

    # Login with valid credentials
    login_page.enter_email("gdekate103@gmail.com")
    login_page.enter_password("Gani@103@G")
    login_page.click_login()
    time.sleep(30)

    assert driver.current_url == "https://www.guvi.in/courses/?current_tab=myCourses", "Login failed!"
    print("SUCCESS: Login successful.")

    time.sleep(30)
    # Logout (Assuming logout button is present after login)
    logout_button_1 = (By.XPATH,"//*[@id = 'dropdown_title']")  # Replace if needed
    base_page = BasePage(driver)
    base_page.click(logout_button_1)

    logout_button_2 = (By.XPATH,"//div[text()='Sign Out']")  # Replace if needed
    base_page = BasePage(driver)
    base_page.click(logout_button_2)
    time.sleep(30)

    assert driver.current_url == "https://www.guvi.in/courses/?current_tab=myCourses", "Logout failed!"
    print("SUCCESS: Logout successful.")


# Test Case 7: Verify invalid login and error message
def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.navigate_to_login_page()
    login_page.click_login()

    login_page.enter_email("gdekate104@gmail.com")
    login_page.enter_password("Gani@103@D")
    login_page.click_login()
    time.sleep(40)

    error_message = login_page.get_error_message()
    assert error_message, "Error message not found for invalid login"
    print(f"SUCCESS: Captured error message -> {error_message}")
