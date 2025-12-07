"""
Helper functions pentru testele automate.
Include funcții generice pentru așteptare, screenshot, validare date, etc.
"""
import os
import time
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    StaleElementReferenceException
)


class WaitHelpers:
    """Helper-i pentru așteptări explicite"""

    @staticmethod
    def wait_for_element_visible(driver, locator, timeout=20):
        """
        Așteaptă ca un element să fie vizibil

        Args:
            driver: WebDriver instance
            locator: Tuple (By, value)
            timeout: Timeout în secunde

        Returns:
            WebElement sau None
        """
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except TimeoutException:
            print(f"Element {locator} not visible after {timeout} seconds")
            return None

    @staticmethod
    def wait_for_element_clickable(driver, locator, timeout=20):
        """
        Așteaptă ca un element să fie clickable

        Args:
            driver: WebDriver instance
            locator: Tuple (By, value)
            timeout: Timeout în secunde

        Returns:
            WebElement sau None
        """
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return element
        except TimeoutException:
            print(f"Element {locator} not clickable after {timeout} seconds")
            return None

    @staticmethod
    def wait_for_element_present(driver, locator, timeout=20):
        """
        Așteaptă ca un element să fie prezent în DOM

        Args:
            driver: WebDriver instance
            locator: Tuple (By, value)
            timeout: Timeout în secunde

        Returns:
            WebElement sau None
        """
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            print(f"Element {locator} not present after {timeout} seconds")
            return None

    @staticmethod
    def wait_for_elements_present(driver, locator, timeout=20):
        """
        Așteaptă ca multiple elemente să fie prezente în DOM

        Args:
            driver: WebDriver instance
            locator: Tuple (By, value)
            timeout: Timeout în secunde

        Returns:
            List[WebElement] sau []
        """
        try:
            elements = WebDriverWait(driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
            return elements
        except TimeoutException:
            print(f"Elements {locator} not present after {timeout} seconds")
            return []

    @staticmethod
    def wait_for_text_in_element(driver, locator, text, timeout=20):
        """
        Așteaptă ca un text specific să apară într-un element

        Args:
            driver: WebDriver instance
            locator: Tuple (By, value)
            text: Text așteptat
            timeout: Timeout în secunde

        Returns:
            bool
        """
        try:
            WebDriverWait(driver, timeout).until(
                EC.text_to_be_present_in_element(locator, text)
            )
            return True
        except TimeoutException:
            print(f"Text '{text}' not found in element {locator} after {timeout} seconds")
            return False

    @staticmethod
    def wait_for_url_contains(driver, url_fragment, timeout=20):
        """
        Așteaptă ca URL-ul să conțină un fragment specific

        Args:
            driver: WebDriver instance
            url_fragment: Fragment de URL așteptat
            timeout: Timeout în secunde

        Returns:
            bool
        """
        try:
            WebDriverWait(driver, timeout).until(
                EC.url_contains(url_fragment)
            )
            return True
        except TimeoutException:
            print(f"URL does not contain '{url_fragment}' after {timeout} seconds")
            return False


class ElementHelpers:
    """Helper-i pentru interacțiuni cu elemente"""

    @staticmethod
    def safe_click(driver, locator, timeout=20):
        """
        Click sigur pe un element cu așteptare

        Args:
            driver: WebDriver instance
            locator: Tuple (By, value)
            timeout: Timeout în secunde

        Returns:
            bool: True dacă click-ul a reușit
        """
        try:
            element = WaitHelpers.wait_for_element_clickable(driver, locator, timeout)
            if element:
                element.click()
                return True
            return False
        except Exception as e:
            print(f"Error clicking element {locator}: {e}")
            return False

    @staticmethod
    def safe_send_keys(driver, locator, text, clear_first=True, timeout=20):
        """
        Trimite text sigur la un element cu așteptare

        Args:
            driver: WebDriver instance
            locator: Tuple (By, value)
            text: Text de trimis
            clear_first: Șterge conținutul existent mai întâi
            timeout: Timeout în secunde

        Returns:
            bool: True dacă operația a reușit
        """
        try:
            element = WaitHelpers.wait_for_element_visible(driver, locator, timeout)
            if element:
                if clear_first:
                    element.clear()
                element.send_keys(text)
                return True
            return False
        except Exception as e:
            print(f"Error sending keys to element {locator}: {e}")
            return False

    @staticmethod
    def get_element_text(driver, locator, timeout=20):
        """
        Obține textul dintr-un element

        Args:
            driver: WebDriver instance
            locator: Tuple (By, value)
            timeout: Timeout în secunde

        Returns:
            str: Text-ul elementului sau empty string
        """
        try:
            element = WaitHelpers.wait_for_element_visible(driver, locator, timeout)
            if element:
                return element.text
            return ""
        except Exception as e:
            print(f"Error getting text from element {locator}: {e}")
            return ""

    @staticmethod
    def is_element_visible(driver, locator, timeout=5):
        """
        Verifică dacă un element este vizibil

        Args:
            driver: WebDriver instance
            locator: Tuple (By, value)
            timeout: Timeout în secunde

        Returns:
            bool
        """
        try:
            WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    @staticmethod
    def is_element_present(driver, locator):
        """
        Verifică dacă un element este prezent în DOM

        Args:
            driver: WebDriver instance
            locator: Tuple (By, value)

        Returns:
            bool
        """
        try:
            driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False


class ScreenshotHelpers:
    """Helper-i pentru capturi de ecran"""

    @staticmethod
    def take_screenshot(driver, name, directory="reports/screenshots"):
        """
        Ia un screenshot și îl salvează

        Args:
            driver: WebDriver instance
            name: Numele fișierului (fără extensie)
            directory: Directorul unde se salvează

        Returns:
            str: Calea către screenshot
        """
        try:
            # Creează directorul dacă nu există
            os.makedirs(directory, exist_ok=True)

            # Generează nume unic cu timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{name}_{timestamp}.png"
            filepath = os.path.join(directory, filename)

            # Salvează screenshot
            driver.save_screenshot(filepath)
            print(f"Screenshot saved: {filepath}")
            return filepath
        except Exception as e:
            print(f"Error taking screenshot: {e}")
            return None

    @staticmethod
    def take_element_screenshot(driver, locator, name, directory="reports/screenshots"):
        """
        Ia screenshot al unui element specific

        Args:
            driver: WebDriver instance
            locator: Tuple (By, value)
            name: Numele fișierului
            directory: Directorul unde se salvează

        Returns:
            str: Calea către screenshot
        """
        try:
            element = WaitHelpers.wait_for_element_visible(driver, locator)
            if element:
                os.makedirs(directory, exist_ok=True)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"{name}_{timestamp}.png"
                filepath = os.path.join(directory, filename)

                element.screenshot(filepath)
                print(f"Element screenshot saved: {filepath}")
                return filepath
            return None
        except Exception as e:
            print(f"Error taking element screenshot: {e}")
            return None


class ValidationHelpers:
    """Helper-i generici pentru validarea datelor"""

    @staticmethod
    def validate_url(driver, expected_url_fragment):
        """
        Validează că URL-ul curent conține fragmentul așteptat

        Args:
            driver: WebDriver instance
            expected_url_fragment: Fragment așteptat în URL

        Returns:
            bool
        """
        current_url = driver.current_url
        return expected_url_fragment in current_url

    @staticmethod
    def validate_page_title(driver, expected_title):
        """
        Validează titlul paginii

        Args:
            driver: WebDriver instance
            expected_title: Titlu așteptat (sau fragment)

        Returns:
            bool
        """
        current_title = driver.title
        return expected_title in current_title

    @staticmethod
    def validate_element_text(driver, locator, expected_text, timeout=20):
        """
        Validează că un element conține textul așteptat

        Args:
            driver: WebDriver instance
            locator: Tuple (By, value)
            expected_text: Text așteptat
            timeout: Timeout în secunde

        Returns:
            bool
        """
        try:
            element_text = ElementHelpers.get_element_text(driver, locator, timeout)
            return expected_text in element_text
        except Exception as e:
            print(f"Error validating element text: {e}")
            return False

    @staticmethod
    def validate_element_count(elements, expected_count, comparison="equal"):
        """
        Validează numărul de elemente

        Args:
            elements: Listă de elemente
            expected_count: Număr așteptat
            comparison: Tip comparație ('equal', 'greater', 'less')

        Returns:
            bool
        """
        actual_count = len(elements)

        if comparison == "equal":
            return actual_count == expected_count
        elif comparison == "greater":
            return actual_count > expected_count
        elif comparison == "less":
            return actual_count < expected_count
        elif comparison == "greater_equal":
            return actual_count >= expected_count
        elif comparison == "less_equal":
            return actual_count <= expected_count
        else:
            return False


class ScrollHelpers:
    """Helper-i pentru scrolling"""

    @staticmethod
    def scroll_to_element(driver, locator):
        """
        Scroll la un element specific

        Args:
            driver: WebDriver instance
            locator: Tuple (By, value)
        """
        try:
            element = driver.find_element(*locator)
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(0.5)  # Așteaptă stabilizarea
        except Exception as e:
            print(f"Error scrolling to element: {e}")

    @staticmethod
    def scroll_to_bottom(driver):
        """
        Scroll la sfârșitul paginii

        Args:
            driver: WebDriver instance
        """
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)

    @staticmethod
    def scroll_to_top(driver):
        """
        Scroll la începutul paginii

        Args:
            driver: WebDriver instance
        """
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(0.5)
