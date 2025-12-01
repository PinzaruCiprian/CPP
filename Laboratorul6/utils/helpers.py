"""
Utilități și helpers pentru testare
Conține funcții de validare, utilitare WebDriver, etc.
"""

import re
from datetime import datetime


class ValidationHelper:
    """Helper pentru validarea datelor"""
    
    @staticmethod
    def is_valid_email(email):
        """Validează dacă email-ul este în format corect"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def is_valid_name(name):
        """Validează dacă numele conține caractere valide"""
        return len(name.strip()) >= 2 and name.isalpha() or ' ' in name
    
    @staticmethod
    def is_valid_password(password):
        """Validează dacă parola îndeplinește criteriile minime"""
        return len(password) >= 6
    
    @staticmethod
    def are_passwords_matching(password1, password2):
        """Verifică dacă două parole se potrivesc"""
        return password1 == password2
    
    @staticmethod
    def validate_email_format(email):
        """Validează format email"""
        if not email:
            return False, "Email-ul este obligatoriu"
        if not ValidationHelper.is_valid_email(email):
            return False, "Email-ul nu este în format valid"
        return True, "Email-ul este valid"
    
    @staticmethod
    def validate_name_format(name):
        """Validează format nume"""
        if not name:
            return False, "Numele este obligatoriu"
        if len(name.strip()) < 2:
            return False, "Numele trebuie să aibă cel puțin 2 caractere"
        return True, "Numele este valid"
    
    @staticmethod
    def validate_password_strength(password):
        """Validează forța parolei"""
        if not password:
            return False, "Parola este obligatorie"
        if len(password) < 6:
            return False, "Parola trebuie să aibă cel puțin 6 caractere"
        return True, "Parola este validă"


class WebDriverHelper:
    """Helper pentru operații WebDriver"""
    
    @staticmethod
    def wait_for_element(driver, locator, timeout=10):
        """Așteptă ca un element să fie disponibil"""
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        
        try:
            wait = WebDriverWait(driver, timeout)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
            return True
        except:
            return False
    
    @staticmethod
    def click_element(driver, locator):
        """Găsește și face click pe un element"""
        try:
            element = driver.find_element("css selector", locator)
            element.click()
            return True
        except:
            return False
    
    @staticmethod
    def fill_input(driver, locator, text):
        """Completează un câmp de input"""
        try:
            element = driver.find_element("css selector", locator)
            element.clear()
            element.send_keys(text)
            return True
        except:
            return False
    
    @staticmethod
    def get_text(driver, locator):
        """Obține textul dintr-un element"""
        try:
            element = driver.find_element("css selector", locator)
            return element.text
        except:
            return ""
    
    @staticmethod
    def is_element_displayed(driver, locator):
        """Verifică dacă un element este afișat"""
        try:
            element = driver.find_element("css selector", locator)
            return element.is_displayed()
        except:
            return False
    
    @staticmethod
    def is_element_enabled(driver, locator):
        """Verifică dacă un element este activ"""
        try:
            element = driver.find_element("css selector", locator)
            return element.is_enabled()
        except:
            return False


class TestDataGenerator:
    """Generator de date pentru teste"""
    
    @staticmethod
    def get_test_user(index=1):
        """Generează date de utilizator pentru test"""
        timestamp = datetime.now().strftime("%H%M%S")
        return {
            'name': f'Test User {index} {timestamp}',
            'email': f'testuser{index}_{timestamp}@test.com',
            'password': f'Test123Pass{index}',
        }
    
    @staticmethod
    def get_invalid_email():
        """Returnează adrese email invalide"""
        return [
            'invalidemail',
            'test@',
            '@example.com',
            'test @example.com',
            'test@.com',
        ]
    
    @staticmethod
    def get_weak_passwords():
        """Returnează parole slabe"""
        return [
            '123',
            'abc',
            '12345',
            'pass',
        ]


class LogHelper:
    """Helper pentru logging și raportare"""
    
    @staticmethod
    def log_test_info(test_name, status, details=""):
        """Log informații despre test"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {test_name}: {status} - {details}")
    
    @staticmethod
    def log_step(step_name):
        """Log pas de test"""
        print(f"  → {step_name}")
    
    @staticmethod
    def log_assertion(expected, actual):
        """Log o asertiune"""
        status = "✓" if expected == actual else "✗"
        print(f"  {status} Expected: {expected}, Actual: {actual}")
