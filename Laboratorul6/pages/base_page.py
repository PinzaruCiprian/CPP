"""
Base Page - clasa de bază pentru toate paginile
Conține metode comune pentru interacțiune cu elementele web
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


class BasePage:
    """Clasa de bază pentru toate paginile"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)
    
    def log_step(self, message):
        """Logs a test step"""
        print(f"[STEP] {message}")
    
    def find_element(self, locator):
        """Găsește un element folosind CSS selector"""
        return self.driver.find_element("css selector", locator)
    
    def find_elements(self, locator):
        """Găsește mai multe elemente folosind CSS selector"""
        return self.driver.find_elements("css selector", locator)
    
    def click(self, locator):
        """Face click pe un element"""
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
        element = self.find_element(locator)
        element.click()
        return True
    
    def type_text(self, locator, text):
        """Scrie text într-un câmp"""
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        return True
    
    def get_text(self, locator):
        """Obține textul dintr-un element"""
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        element = self.find_element(locator)
        return element.text.strip()
    
    def is_displayed(self, locator):
        """Verifică dacă un element este vizibil"""
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except:
            return False
    
    def is_enabled(self, locator):
        """Verifică dacă un element este activ"""
        try:
            element = self.find_element(locator)
            return element.is_enabled()
        except:
            return False
    
    def wait_for_element(self, locator, timeout=10):
        """Așteptă ca un element să apară"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, locator))
            )
            return True
        except:
            return False
    
    def clear_field(self, locator):
        """Șterge conținutul unui câmp"""
        element = self.find_element(locator)
        element.clear()
        return True
    
    def submit_form(self, locator):
        """Trimite un formular"""
        element = self.find_element(locator)
        element.submit()
        return True
    
    def switch_to_modal(self, modal_locator):
        """Comută pe o modalitate"""
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, modal_locator)))
        return True
    
    def close_modal(self, close_button_locator):
        """Închide o modalitate"""
        self.click(close_button_locator)
        return True
    
    def scroll_to_element(self, element_or_locator):
        """Scroll to an element"""
        # Handle both WebElement objects and CSS selector strings
        if isinstance(element_or_locator, str):
            element = self.find_element(element_or_locator)
        else:
            element = element_or_locator
        
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)
        return True
    
    def get_attribute(self, locator, attribute):
        """Obține valoarea unui atribut"""
        element = self.find_element(locator)
        return element.get_attribute(attribute)
    
    def select_checkbox(self, locator):
        """Selectează un checkbox"""
        element = self.find_element(locator)
        if not element.is_selected():
            element.click()
        return True
    
    def deselect_checkbox(self, locator):
        """Deselectează un checkbox"""
        element = self.find_element(locator)
        if element.is_selected():
            element.click()
        return True
    
    def select_radio_button(self, locator):
        """Selectează un radio button"""
        element = self.find_element(locator)
        if not element.is_selected():
            element.click()
        return True
