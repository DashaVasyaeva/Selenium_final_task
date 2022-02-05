from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.IS_NOT_PRODUCTS), "There are products in your basket"

    def guest_should_go_to_basket(self):
        view_basket_button = self.browser.find_element(*BasketPageLocators.VIEW_BASKET)
        view_basket_button.click()

    def guest_should_see_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), "Your basket is not empty"
