"""
Login Page - pagina de autentificare (modal Sign In)
"""

from pages.base_page import BasePage
from utils.locators import Locators


class LoginPage(BasePage):
    """Modelul paginii de login"""
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def open_login_modal(self):
        """Deschide modalul de login"""
        return self.wait_for_element(Locators.LOGIN_MODAL)
    
    def is_login_modal_displayed(self):
        """Verifică dacă modalul de login este afișat"""
        return self.is_displayed(Locators.LOGIN_MODAL)
    
    def enter_username(self, username):
        """Introduce username-ul"""
        return self.type_text(Locators.LOGIN_NAME_INPUT, username)
    
    def enter_email(self, email):
        """Introduce email-ul"""
        return self.type_text(Locators.LOGIN_EMAIL_INPUT, email)
    
    def get_name_field_value(self):
        """Obține valoarea câmpului Name"""
        return self.get_attribute(Locators.LOGIN_NAME_INPUT, "value")
    
    def get_email_field_value(self):
        """Obține valoarea câmpului Email"""
        return self.get_attribute(Locators.LOGIN_EMAIL_INPUT, "value")
    
    def click_login_button(self):
        """Face click pe butonul Sign In"""
        return self.click(Locators.LOGIN_SUBMIT_BUTTON)
    
    def is_login_button_enabled(self):
        """Verifică dacă butonul Sign In este activ"""
        return self.is_enabled(Locators.LOGIN_SUBMIT_BUTTON)
    
    def close_login_modal(self):
        """Închide modalul de login"""
        return self.close_modal(Locators.LOGIN_MODAL_CLOSE)
    
    def login(self, username, email):
        """Efectuează login cu datele furnizate"""
        self.enter_username(username)
        self.enter_email(email)
        return self.click_login_button()
    
    def clear_name_field(self):
        """Șterge câmpul Name"""
        return self.clear_field(Locators.LOGIN_NAME_INPUT)
    
    def clear_email_field(self):
        """Șterge câmpul Email"""
        return self.clear_field(Locators.LOGIN_EMAIL_INPUT)
    
    def fill_login_form(self, name, email):
        """Completează formularul de login"""
        self.enter_username(name)
        self.enter_email(email)
        return True
    
    def submit_login_form(self):
        """Trimite formularul de login"""
        return self.click_login_button()
    
    def get_login_modal_title(self):
        """Obține titlul modalului de login"""
        try:
            return self.get_text('.agileinfo_sign')
        except:
            return ""
