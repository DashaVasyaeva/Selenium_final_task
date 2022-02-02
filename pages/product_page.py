import time

from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def adding_an_product_to_basket(self):
        product_link = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT)
        product_link.click()
        self.solve_quiz_and_get_code()

