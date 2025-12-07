"""
Base Page Object Model class.
Toate paginile vor moșteni din această clasă.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.helpers import (
    WaitHelpers,
    ElementHelpers,
    ScreenshotHelpers,
    ValidationHelpers,
    ScrollHelpers
)


class BasePage:
    """Clasa de bază pentru toate Page Objects"""

    def __init__(self, driver):
        """
        Inițializează BasePage

        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.wait_helpers = WaitHelpers()
        self.element_helpers = ElementHelpers()
        self.screenshot_helpers = ScreenshotHelpers()
        self.validation_helpers = ValidationHelpers()
        self.scroll_helpers = ScrollHelpers()

    def open_url(self, url):
        """
        Deschide un URL

        Args:
            url: URL-ul de deschis
        """
        self.driver.get(url)

    def get_current_url(self):
        """
        Obține URL-ul curent

        Returns:
            str: URL-ul curent
        """
        return self.driver.current_url

    def get_page_title(self):
        """
        Obține titlul paginii

        Returns:
            str: Titlul paginii
        """
        return self.driver.title

    def wait_for_element_visible(self, locator, timeout=20):
        """
        Așteaptă ca un element să fie vizibil

        Args:
            locator: Tuple (By, value)
            timeout: Timeout în secunde

        Returns:
            WebElement sau None
        """
        return self.wait_helpers.wait_for_element_visible(self.driver, locator, timeout)

    def wait_for_element_clickable(self, locator, timeout=20):
        """
        Așteaptă ca un element să fie clickable

        Args:
            locator: Tuple (By, value)
            timeout: Timeout în secunde

        Returns:
            WebElement sau None
        """
        return self.wait_helpers.wait_for_element_clickable(self.driver, locator, timeout)

    def wait_for_elements_present(self, locator, timeout=20):
        """
        Așteaptă ca multiple elemente să fie prezente

        Args:
            locator: Tuple (By, value)
            timeout: Timeout în secunde

        Returns:
            List[WebElement]
        """
        return self.wait_helpers.wait_for_elements_present(self.driver, locator, timeout)

    def click_element(self, locator, timeout=20):
        """
        Click pe un element

        Args:
            locator: Tuple (By, value)
            timeout: Timeout în secunde

        Returns:
            bool: True dacă click-ul a reușit
        """
        return self.element_helpers.safe_click(self.driver, locator, timeout)

    def send_keys_to_element(self, locator, text, clear_first=True, timeout=20):
        """
        Trimite text la un element

        Args:
            locator: Tuple (By, value)
            text: Text de trimis
            clear_first: Șterge conținutul existent
            timeout: Timeout în secunde

        Returns:
            bool: True dacă operația a reușit
        """
        return self.element_helpers.safe_send_keys(self.driver, locator, text, clear_first, timeout)

    def get_element_text(self, locator, timeout=20):
        """
        Obține textul dintr-un element

        Args:
            locator: Tuple (By, value)
            timeout: Timeout în secunde

        Returns:
            str: Text-ul elementului
        """
        return self.element_helpers.get_element_text(self.driver, locator, timeout)

    def is_element_visible(self, locator, timeout=5):
        """
        Verifică dacă un element este vizibil

        Args:
            locator: Tuple (By, value)
            timeout: Timeout în secunde

        Returns:
            bool
        """
        return self.element_helpers.is_element_visible(self.driver, locator, timeout)

    def is_element_present(self, locator):
        """
        Verifică dacă un element este prezent în DOM

        Args:
            locator: Tuple (By, value)

        Returns:
            bool
        """
        return self.element_helpers.is_element_present(self.driver, locator)

    def get_elements(self, locator):
        """
        Obține toate elementele care corespund locatorului

        Args:
            locator: Tuple (By, value)

        Returns:
            List[WebElement]
        """
        try:
            return self.driver.find_elements(*locator)
        except NoSuchElementException:
            return []

    def get_element(self, locator):
        """
        Obține un element

        Args:
            locator: Tuple (By, value)

        Returns:
            WebElement sau None
        """
        try:
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            return None

    def take_screenshot(self, name):
        """
        Ia un screenshot

        Args:
            name: Numele screenshot-ului

        Returns:
            str: Calea către screenshot
        """
        return self.screenshot_helpers.take_screenshot(self.driver, name)

    def scroll_to_element(self, locator):
        """
        Scroll la un element

        Args:
            locator: Tuple (By, value)
        """
        self.scroll_helpers.scroll_to_element(self.driver, locator)

    def scroll_to_bottom(self):
        """Scroll la sfârșitul paginii"""
        self.scroll_helpers.scroll_to_bottom(self.driver)

    def scroll_to_top(self):
        """Scroll la începutul paginii"""
        self.scroll_helpers.scroll_to_top(self.driver)

    def validate_url_contains(self, url_fragment):
        """
        Validează că URL-ul conține fragmentul specificat

        Args:
            url_fragment: Fragment de URL

        Returns:
            bool
        """
        return self.validation_helpers.validate_url(self.driver, url_fragment)

    def validate_page_title_contains(self, title_fragment):
        """
        Validează că titlul paginii conține fragmentul specificat

        Args:
            title_fragment: Fragment din titlu

        Returns:
            bool
        """
        return self.validation_helpers.validate_page_title(self.driver, title_fragment)

    def refresh_page(self):
        """Reîmprospătează pagina"""
        self.driver.refresh()

    def go_back(self):
        """Navighează înapoi în istoric"""
        self.driver.back()

    def go_forward(self):
        """Navighează înainte în istoric"""
        self.driver.forward()
