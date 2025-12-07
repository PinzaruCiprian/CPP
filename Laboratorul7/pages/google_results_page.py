"""
Page Object Model pentru pagina de rezultate Google.
"""
import time
import re
from pages.base_page import BasePage
from utils.locators import GoogleResultsPageLocators


class GoogleResultsPage(BasePage):
    """Page Object pentru pagina de rezultate Google"""

    def __init__(self, driver):
        """
        Inițializează GoogleResultsPage

        Args:
            driver: WebDriver instance
        """
        super().__init__(driver)
        self.locators = GoogleResultsPageLocators()

    def is_results_page_loaded(self):
        """
        Verifică dacă pagina de rezultate s-a încărcat

        Returns:
            bool: True dacă pagina este încărcată
        """
        try:
            # Verifică URL-ul
            url_check = "search?" in self.get_current_url()

            # Verifică prezența search box-ului
            search_box_present = self.is_element_present(self.locators.SEARCH_BOX)

            return url_check and search_box_present
        except Exception as e:
            print(f"Error checking if results page is loaded: {e}")
            return False

    def wait_for_results_to_load(self, timeout=5):
        """
        Așteaptă ca rezultatele să se încarce

        Args:
            timeout: Timeout în secunde

        Returns:
            bool: True dacă rezultatele s-au încărcat
        """
        try:
            # Simplu: doar așteaptă ca URL-ul să conțină 'search?'
            time.sleep(2)  # Așteaptă încărcarea paginii
            return "search?" in self.get_current_url()
        except Exception as e:
            print(f"Error waiting for results to load: {e}")
            return False

    def get_search_results(self):
        """
        Obține toate rezultatele de căutare

        Returns:
            List[WebElement]: Lista de rezultate
        """
        try:
            # Așteaptă ca rezultatele să se încarce
            time.sleep(1)

            # Caută titluri H3 - acestea sunt mai stabile ca locatori
            from selenium.webdriver.common.by import By
            h3_elements = self.get_elements((By.CSS_SELECTOR, "h3"))

            if h3_elements:
                return h3_elements

            # Fallback la locatorul original
            results = self.get_elements(self.locators.SEARCH_RESULTS)
            if not results:
                results = self.get_elements(self.locators.SEARCH_RESULTS_ALTERNATIVE)

            return results
        except Exception as e:
            print(f"Error getting search results: {e}")
            return []

    def get_number_of_results_on_page(self):
        """
        Obține numărul de rezultate de pe pagina curentă

        Returns:
            int: Numărul de rezultate
        """
        try:
            # Simplu: numără titlurile H3 care sunt rezultate
            from selenium.webdriver.common.by import By
            h3_elements = self.get_elements((By.CSS_SELECTOR, "h3"))

            # Filtrează doar H3-urile care au părinte cu link
            valid_count = 0
            for h3 in h3_elements:
                try:
                    # Verifică dacă are text și este vizibil
                    if h3.text and h3.is_displayed():
                        valid_count += 1
                except:
                    continue

            return valid_count
        except Exception as e:
            print(f"Error getting number of results: {e}")
            return 0

    def get_result_stats_text(self):
        """
        Obține textul cu statisticile rezultatelor (ex: "About 1,234 results")

        Returns:
            str: Textul cu statistici
        """
        try:
            stats_element = self.wait_for_element_visible(
                self.locators.RESULT_STATS,
                timeout=10
            )
            if stats_element:
                return stats_element.text
            return ""
        except Exception as e:
            print(f"Error getting result stats: {e}")
            return ""

    def get_total_results_count(self):
        """
        Extrage numărul total de rezultate din textul cu statistici

        Returns:
            int: Numărul total de rezultate sau 0
        """
        try:
            stats_text = self.get_result_stats_text()
            # Extrage numărul din text (ex: "About 1,234 results" -> 1234)
            numbers = re.findall(r'[\d,]+', stats_text)
            if numbers:
                # Ia primul număr și îndepărtează virgulele
                total = int(numbers[0].replace(',', ''))
                return total
            return 0
        except Exception as e:
            print(f"Error extracting total results count: {e}")
            return 0

    def is_did_you_mean_visible(self):
        """
        Verifică dacă linkul "Did you mean" este vizibil

        Returns:
            bool: True dacă este vizibil
        """
        try:
            # Încearcă toate locatorii posibili pentru diferite versiuni Google
            locators_to_try = [
                self.locators.DID_YOU_MEAN,
                self.locators.DID_YOU_MEAN_ALTERNATIVE,
                self.locators.SHOWING_RESULTS_FOR,
                self.locators.SHOWING_RESULTS_FOR_NEW,
                self.locators.ORIGINALLY_SEARCHED_FOR
            ]

            for locator in locators_to_try:
                if self.is_element_visible(locator, timeout=2):
                    print(f"Found 'did you mean' element with locator: {locator}")
                    return True

            return False
        except Exception as e:
            print(f"Error checking did you mean: {e}")
            return False

    def get_did_you_mean_text(self):
        """
        Obține textul din linkul "Did you mean"

        Returns:
            str: Textul sugestiei
        """
        try:
            # Încearcă să găsească elementul "Did you mean"
            did_you_mean_element = None

            if self.is_element_visible(self.locators.DID_YOU_MEAN, timeout=3):
                did_you_mean_element = self.get_element(self.locators.DID_YOU_MEAN)
            elif self.is_element_visible(self.locators.DID_YOU_MEAN_ALTERNATIVE, timeout=3):
                did_you_mean_element = self.get_element(self.locators.DID_YOU_MEAN_ALTERNATIVE)

            if did_you_mean_element:
                return did_you_mean_element.text

            return ""
        except Exception as e:
            print(f"Error getting did you mean text: {e}")
            return ""

    def click_did_you_mean(self):
        """
        Click pe linkul "Did you mean"

        Returns:
            bool: True dacă click-ul a reușit
        """
        try:
            if self.is_element_visible(self.locators.DID_YOU_MEAN, timeout=3):
                return self.click_element(self.locators.DID_YOU_MEAN)
            elif self.is_element_visible(self.locators.DID_YOU_MEAN_ALTERNATIVE, timeout=3):
                return self.click_element(self.locators.DID_YOU_MEAN_ALTERNATIVE)
            return False
        except Exception as e:
            print(f"Error clicking did you mean: {e}")
            return False

    def get_search_result_titles(self):
        """
        Obține titlurile rezultatelor de căutare

        Returns:
            List[str]: Lista de titluri
        """
        try:
            titles = self.get_elements(self.locators.SEARCH_RESULT_TITLES)
            return [title.text for title in titles if title.text]
        except Exception as e:
            print(f"Error getting result titles: {e}")
            return []

    def click_search_result(self, index=0):
        """
        Click pe un rezultat de căutare

        Args:
            index: Indexul rezultatului (0-based)

        Returns:
            bool: True dacă click-ul a reușit
        """
        try:
            results = self.get_search_results()
            if index < len(results):
                result = results[index]
                links = result.find_elements(*self.locators.SEARCH_RESULT_LINKS)
                if links:
                    links[0].click()
                    return True
            return False
        except Exception as e:
            print(f"Error clicking search result: {e}")
            return False

    def is_next_page_button_visible(self):
        """
        Verifică dacă butonul "Next" este vizibil

        Returns:
            bool: True dacă este vizibil
        """
        return self.is_element_visible(self.locators.NEXT_PAGE, timeout=5)

    def click_next_page(self):
        """
        Click pe butonul "Next" pentru a merge la pagina următoare

        Returns:
            bool: True dacă click-ul a reușit
        """
        return self.click_element(self.locators.NEXT_PAGE)

    def is_previous_page_button_visible(self):
        """
        Verifică dacă butonul "Previous" este vizibil

        Returns:
            bool: True dacă este vizibil
        """
        return self.is_element_visible(self.locators.PREVIOUS_PAGE, timeout=5)

    def click_previous_page(self):
        """
        Click pe butonul "Previous" pentru a merge la pagina anterioară

        Returns:
            bool: True dacă click-ul a reușit
        """
        return self.click_element(self.locators.PREVIOUS_PAGE)

    def get_search_box_value(self):
        """
        Obține valoarea din search box-ul de pe pagina de rezultate

        Returns:
            str: Valoarea din search box
        """
        try:
            search_box = self.get_element(self.locators.SEARCH_BOX)
            if search_box:
                return search_box.get_attribute("value")
            return ""
        except Exception as e:
            print(f"Error getting search box value: {e}")
            return ""

    def has_results(self):
        """
        Verifică dacă există rezultate pe pagină

        Returns:
            bool: True dacă există rezultate
        """
        results = self.get_search_results()
        return len(results) > 0

    def is_no_results_message_visible(self):
        """
        Verifică dacă mesajul "No results" este vizibil

        Returns:
            bool: True dacă este vizibil
        """
        return self.is_element_visible(self.locators.NO_RESULTS_MESSAGE, timeout=5)

    def scroll_to_result(self, index=0):
        """
        Scroll la un rezultat specific

        Args:
            index: Indexul rezultatului (0-based)

        Returns:
            bool: True dacă scroll-ul a reușit
        """
        try:
            results = self.get_search_results()
            if index < len(results):
                result = results[index]
                self.driver.execute_script("arguments[0].scrollIntoView(true);", result)
                time.sleep(0.5)
                return True
            return False
        except Exception as e:
            print(f"Error scrolling to result: {e}")
            return False
