"""
WebDriver Factory - gestionează inițializare și închidere WebDriver
"""

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class WebDriverFactory:
    """Factory pentru crearea și gestionarea instanțelor WebDriver"""
    
    _driver = None
    
    @staticmethod
    def create_driver():
        """Creează o nouă instanță de Chrome WebDriver"""
        if WebDriverFactory._driver is None:
            options = webdriver.ChromeOptions()
            # options.add_argument("--headless")  # Dezactivează pentru a vedea browser-ul
            options.add_argument("--start-maximized")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
            
            # Get the chromedriver directory from ChromeDriverManager
            manager = ChromeDriverManager()
            driver_dir = manager.install()  # This may return a file path
            
            # If it's a file, get the directory
            if os.path.isfile(driver_dir):
                driver_dir = os.path.dirname(driver_dir)
            
            # Now find chromedriver.exe in the directory
            chromedriver_path = None
            if os.path.isdir(driver_dir):
                for filename in os.listdir(driver_dir):
                    if filename == 'chromedriver.exe':
                        chromedriver_path = os.path.join(driver_dir, filename)
                        break
            
            if chromedriver_path is None:
                raise Exception(f"ChromeDriver not found in {driver_dir}")
            
            service = Service(chromedriver_path)
            WebDriverFactory._driver = webdriver.Chrome(service=service, options=options)
            WebDriverFactory._driver.implicitly_wait(10)
        
        return WebDriverFactory._driver
    
    @staticmethod
    def get_driver():
        """Obține instanța curentă de WebDriver"""
        if WebDriverFactory._driver is None:
            return WebDriverFactory.create_driver()
        return WebDriverFactory._driver
    
    @staticmethod
    def close_driver():
        """Închide WebDriver-ul"""
        if WebDriverFactory._driver is not None:
            WebDriverFactory._driver.quit()
            WebDriverFactory._driver = None
    
    @staticmethod
    def navigate_to(url):
        """Navighează la o adresă URL"""
        driver = WebDriverFactory.get_driver()
        driver.get(url)
    
    @staticmethod
    def refresh():
        """Reîncarcă pagina curentă"""
        driver = WebDriverFactory.get_driver()
        driver.refresh()
    
    @staticmethod
    def go_back():
        """Merge înapoi în istoric"""
        driver = WebDriverFactory.get_driver()
        driver.back()
    
    @staticmethod
    def get_current_url():
        """Obține URL-ul curent"""
        driver = WebDriverFactory.get_driver()
        return driver.current_url
    
    @staticmethod
    def get_page_title():
        """Obține titlul paginii"""
        driver = WebDriverFactory.get_driver()
        return driver.title
