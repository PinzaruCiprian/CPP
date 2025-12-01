"""
Home Page - pagina principală cu butoane Sign In și Sign Up
"""

from pages.base_page import BasePage
from utils.locators import Locators


class HomePage(BasePage):
    """Modelul paginii principale"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.page_title = "Elite Shoppy"
    
    def open(self, url):
        """Deschide pagina principală"""
        self.driver.get(url)
        self.wait_for_element(Locators.SIGN_IN_BUTTON)
        return True
    
    def click_sign_in_button(self):
        """Fă click pe butonul Sign In"""
        return self.click(Locators.SIGN_IN_BUTTON)
    
    def click_sign_up_button(self):
        """Face click pe butonul Sign Up"""
        return self.click(Locators.SIGN_UP_BUTTON)
    
    def is_home_page_loaded(self):
        """Verifică dacă pagina principală s-a încărcat"""
        return self.is_displayed(Locators.SIGN_IN_BUTTON) and \
               self.is_displayed(Locators.SIGN_UP_BUTTON)
    
    def get_page_title(self):
        """Obține titlul paginii"""
        return self.driver.title
    
    def click_cart_button(self):
        """Face click pe butonul coș"""
        return self.click(Locators.CART_BUTTON)
    
    def is_cart_button_visible(self):
        """Verifică dacă butonul coș este vizibil"""
        return self.is_displayed(Locators.CART_BUTTON)
    
    def select_poll_option(self, option_index):
        """Selectează o opțiune din sondajul comunității"""
        radio_buttons = self.find_elements(Locators.RADIO_BUTTONS)
        if option_index < len(radio_buttons):
            return self.select_radio_button(Locators.RADIO_BUTTONS)
        return False
    
    def submit_poll(self):
        """Trimite sondajul comunității"""
        return self.click(Locators.POLL_SUBMIT_BUTTON)
    
    def get_products(self):
        """Obține lista de produse"""
        return self.find_elements(Locators.PRODUCT_ITEMS)
    
    def click_product_quick_view(self, product_index):
        """Face click pe Quick View pentru un produs"""
        products = self.get_products()
        if product_index < len(products):
            product = products[product_index]
            links = product.find_elements("css selector", Locators.PRODUCT_LINK)
            if links:
                links[0].click()
                return True
        return False
    
    def sort_products(self, sort_value):
        """Sortează produsele"""
        return self.driver.find_element("css selector", Locators.SORT_DROPDOWN).send_keys(sort_value)
