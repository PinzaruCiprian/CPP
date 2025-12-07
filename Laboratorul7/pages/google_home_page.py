"""
Page Object Model pentru pagina principală Google.
"""
import time
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from utils.locators import GoogleHomePageLocators


class GoogleHomePage(BasePage):
    """Page Object pentru pagina principală Google"""

    def __init__(self, driver):
        """
        Inițializează GoogleHomePage

        Args:
            driver: WebDriver instance
        """
        super().__init__(driver)
        self.locators = GoogleHomePageLocators()
        self.url = "https://www.google.co.in"

    def navigate_to_google(self):
        """
        Navighează la pagina principală Google

        Returns:
            bool: True dacă navigarea a reușit
        """
        try:
            self.open_url(self.url)
            # Așteaptă ca search box-ul să fie vizibil
            self.wait_for_element_visible(self.locators.SEARCH_BOX, timeout=10)
            return True
        except Exception as e:
            print(f"Error navigating to Google: {e}")
            return False

    def is_google_page_loaded(self):
        """
        Verifică dacă pagina Google s-a încărcat corect

        Returns:
            bool: True dacă pagina este încărcată
        """
        # Verifică dacă URL-ul conține google
        url_check = "google" in self.get_current_url().lower()

        # Verifică dacă search box-ul este vizibil
        search_box_visible = self.is_element_visible(self.locators.SEARCH_BOX, timeout=5)

        # Ambele condiții trebuie să fie îndeplinite
        return url_check and search_box_visible

    def enter_search_term(self, search_term):
        """
        Introduce un termen de căutare în search box

        Args:
            search_term: Termenul de căutare

        Returns:
            bool: True dacă operația a reușit
        """
        try:
            # Găsește search box
            search_box = self.wait_for_element_visible(self.locators.SEARCH_BOX)
            if search_box:
                # Curăță câmpul dacă are conținut
                search_box.clear()
                # Introduce textul
                search_box.send_keys(search_term)
                time.sleep(0.5)  # Așteaptă puțin pentru sugestii
                return True
            return False
        except Exception as e:
            print(f"Error entering search term: {e}")
            return False

    def click_google_search_button(self):
        """
        Click pe butonul Google Search

        Returns:
            bool: True dacă click-ul a reușit
        """
        try:
            # Așteaptă ca butonul să fie clickable
            # Uneori butonul este hidden, așa că folosim JavaScript pentru click
            search_button = self.wait_for_element_visible(
                self.locators.GOOGLE_SEARCH_BUTTON,
                timeout=10
            )

            if search_button:
                # Încearcă click normal
                try:
                    search_button.click()
                except Exception:
                    # Dacă click-ul normal eșuează, folosește JavaScript
                    self.driver.execute_script("arguments[0].click();", search_button)

                time.sleep(1)  # Așteaptă încărcarea rezultatelor
                return True
            return False
        except Exception as e:
            print(f"Error clicking search button: {e}")
            return False

    def press_enter_in_search_box(self):
        """
        Apasă Enter în search box

        Returns:
            bool: True dacă operația a reușit
        """
        try:
            search_box = self.get_element(self.locators.SEARCH_BOX)
            if search_box:
                search_box.send_keys(Keys.RETURN)
                time.sleep(1)  # Așteaptă încărcarea rezultatelor
                return True
            return False
        except Exception as e:
            print(f"Error pressing enter: {e}")
            return False

    def search_for(self, search_term, use_enter=False):
        """
        Realizează o căutare completă

        Args:
            search_term: Termenul de căutare
            use_enter: Folosește Enter în loc de click pe buton

        Returns:
            bool: True dacă căutarea a reușit
        """
        if not self.enter_search_term(search_term):
            return False

        if use_enter:
            return self.press_enter_in_search_box()
        else:
            return self.click_google_search_button()

    def click_feeling_lucky_button(self):
        """
        Click pe butonul "I'm Feeling Lucky"

        Returns:
            bool: True dacă click-ul a reușit
        """
        try:
            lucky_button = self.wait_for_element_clickable(
                self.locators.FEELING_LUCKY_BUTTON,
                timeout=10
            )
            if lucky_button:
                lucky_button.click()
                return True
            return False
        except Exception as e:
            print(f"Error clicking feeling lucky button: {e}")
            return False

    def are_search_suggestions_visible(self):
        """
        Verifică dacă sugestiile de căutare sunt vizibile

        Returns:
            bool: True dacă sugestiile sunt vizibile
        """
        try:
            # Așteaptă puțin pentru sugestii
            time.sleep(0.5)
            suggestions = self.get_elements(self.locators.SEARCH_SUGGESTIONS)
            return len(suggestions) > 0
        except Exception as e:
            print(f"Error checking search suggestions: {e}")
            return False

    def get_search_suggestions(self):
        """
        Obține lista de sugestii de căutare

        Returns:
            List[str]: Lista de sugestii
        """
        try:
            time.sleep(0.5)  # Așteaptă sugestiile
            suggestions = self.get_elements(self.locators.SEARCH_SUGGESTIONS)
            return [suggestion.text for suggestion in suggestions if suggestion.text]
        except Exception as e:
            print(f"Error getting search suggestions: {e}")
            return []

    def is_google_logo_visible(self):
        """
        Verifică dacă logo-ul Google este vizibil
        Încearcă mai multe locatori până găsește logo-ul

        Returns:
            bool: True dacă logo-ul este vizibil
        """
        # Încearcă mai multe variante de locatori
        logo_locators = [
            self.locators.GOOGLE_LOGO,
            self.locators.GOOGLE_LOGO_ALTERNATIVE,
            self.locators.GOOGLE_LOGO_ALTERNATIVE2,
            self.locators.GOOGLE_LOGO_ALTERNATIVE3,
        ]

        for locator in logo_locators:
            if self.is_element_visible(locator, timeout=2):
                return True

        return False

    def get_search_box_text(self):
        """
        Obține textul din search box

        Returns:
            str: Textul din search box
        """
        try:
            search_box = self.get_element(self.locators.SEARCH_BOX)
            if search_box:
                return search_box.get_attribute("value")
            return ""
        except Exception as e:
            print(f"Error getting search box text: {e}")
            return ""

    def clear_search_box(self):
        """
        Curăță search box-ul

        Returns:
            bool: True dacă operația a reușit
        """
        try:
            search_box = self.get_element(self.locators.SEARCH_BOX)
            if search_box:
                search_box.clear()
                return True
            return False
        except Exception as e:
            print(f"Error clearing search box: {e}")
            return False

    def is_search_box_empty(self):
        """
        Verifică dacă search box-ul este gol

        Returns:
            bool: True dacă search box-ul este gol
        """
        text = self.get_search_box_text()
        return text == "" or text is None

    def get_current_page_url(self):
        """
        Obține URL-ul paginii curente

        Returns:
            str: URL-ul curent
        """
        return self.get_current_url()
