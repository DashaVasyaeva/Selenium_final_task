from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTR_EMAIL)
        email_field.send_keys(email)
        pass_field = self.browser.find_element(*LoginPageLocators.REGISTR_PASS)
        pass_field.send_keys(password)
        rep_pass_field = self.browser.find_element(*LoginPageLocators.REP_REGISTR_PASS)
        rep_pass_field.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTR_BUTTON)
        reg_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' is not in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
