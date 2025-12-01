"""
Sign Up Page - pagina de înregistrare (modal Sign Up)
"""

from pages.base_page import BasePage
from utils.locators import Locators


class SignUpPage(BasePage):
    """Modelul paginii de înregistrare"""
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def open_signup_modal(self):
        """Deschide modalul de Sign Up"""
        return self.wait_for_element(Locators.SIGNUP_MODAL)
    
    def is_signup_modal_displayed(self):
        """Verifică dacă modalul de Sign Up este afișat"""
        return self.is_displayed(Locators.SIGNUP_MODAL)
    
    def enter_name(self, name):
        """Introduce numele"""
        return self.type_text(Locators.SIGNUP_NAME_INPUT, name)
    
    def enter_email(self, email):
        """Introduce email-ul"""
        return self.type_text(Locators.SIGNUP_EMAIL_INPUT, email)
    
    def enter_password(self, password):
        """Introduce parola"""
        return self.type_text(Locators.SIGNUP_PASSWORD_INPUT, password)
    
    def enter_confirm_password(self, password):
        """Introduce confirmarea parolei"""
        return self.type_text(Locators.SIGNUP_CONFIRM_PASSWORD_INPUT, password)
    
    def get_name_field_value(self):
        """Obține valoarea câmpului Name"""
        return self.get_attribute(Locators.SIGNUP_NAME_INPUT, "value")
    
    def get_email_field_value(self):
        """Obține valoarea câmpului Email"""
        return self.get_attribute(Locators.SIGNUP_EMAIL_INPUT, "value")
    
    def get_password_field_value(self):
        """Obține valoarea câmpului Password"""
        return self.get_attribute(Locators.SIGNUP_PASSWORD_INPUT, "value")
    
    def get_confirm_password_field_value(self):
        """Obține valoarea câmpului Confirm Password"""
        return self.get_attribute(Locators.SIGNUP_CONFIRM_PASSWORD_INPUT, "value")
    
    def click_signup_button(self):
        """Face click pe butonul Sign Up"""
        return self.click(Locators.SIGNUP_SUBMIT_BUTTON)
    
    def is_signup_button_enabled(self):
        """Verifică dacă butonul Sign Up este activ"""
        return self.is_enabled(Locators.SIGNUP_SUBMIT_BUTTON)
    
    def close_signup_modal(self):
        """Închide modalul de Sign Up"""
        return self.close_modal(Locators.LOGIN_MODAL_CLOSE)
    
    def signup(self, name, email, password, confirm_password):
        """Efectuează înregistrarea cu datele furnizate"""
        self.enter_name(name)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        return self.click_signup_button()
    
    def clear_name_field(self):
        """Șterge câmpul Name"""
        return self.clear_field(Locators.SIGNUP_NAME_INPUT)
    
    def clear_email_field(self):
        """Șterge câmpul Email"""
        return self.clear_field(Locators.SIGNUP_EMAIL_INPUT)
    
    def clear_password_field(self):
        """Șterge câmpul Password"""
        return self.clear_field(Locators.SIGNUP_PASSWORD_INPUT)
    
    def clear_confirm_password_field(self):
        """Șterge câmpul Confirm Password"""
        return self.clear_field(Locators.SIGNUP_CONFIRM_PASSWORD_INPUT)
    
    def fill_signup_form(self, name, email, password, confirm_password):
        """Completează formularul de înregistrare"""
        self.enter_name(name)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        return True
    
    def submit_signup_form(self):
        """Trimite formularul de înregistrare"""
        return self.click_signup_button()
    
    def get_signup_modal_title(self):
        """Obține titlul modalului de Sign Up"""
        try:
            return self.get_text('.agileinfo_sign')
        except:
            return ""
    
    def verify_all_fields_empty(self):
        """Verifică dacă toate câmpurile sunt goale"""
        return (self.get_name_field_value() == "" and
                self.get_email_field_value() == "" and
                self.get_password_field_value() == "" and
                self.get_confirm_password_field_value() == "")
