from selenium.webdriver.common.by import By
from PageObject.base_page import BasePage

class LoginPage(BasePage):
    LOGIN_URL = "https://www.guvi.in/"
    LOGIN_BUTTON = (By.XPATH, "//*[@id='login-btn']")  # Replace if needed
    EMAIL_INPUT = (By.XPATH, "//*[@id='email']")
    PASSWORD_INPUT = (By.XPATH, "//*[@id='password']")
    ERROR_MESSAGE = (By.XPATH, "//*[@id='emailgroup']/div")
    guvi_login_url = "https://www.guvi.in/login"

    def navigate_to_login_page(self):
        self.navigate_to(self.LOGIN_URL)

    def enter_email(self, email):
        self.find_element(self.EMAIL_INPUT).send_keys(email)

    def enter_password(self, password):
        self.find_element(self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.find_element(self.LOGIN_BUTTON).click()

    def get_error_message(self):
        element = self.find_element(self.ERROR_MESSAGE)
        return element.text if element else None

    def is_login_button_visible(self):
        return self.is_visible(self.LOGIN_BUTTON)

    def is_login_button_clickable(self):
        return self.is_clickable(self.LOGIN_BUTTON) is not None

    def login_to(self, guvi_login_url):
        pass
