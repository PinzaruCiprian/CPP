"""
Locatori generici pentru elementele web din aplicația Google Search.
Folosește căi relative pentru identificarea elementelor.
"""
from selenium.webdriver.common.by import By


class GoogleHomePageLocators:
    """Locatori pentru pagina principală Google"""

    # Search box
    SEARCH_BOX = (By.NAME, "q")
    SEARCH_BOX_ALTERNATIVE = (By.CSS_SELECTOR, "textarea[name='q']")

    # Search buttons
    GOOGLE_SEARCH_BUTTON = (By.NAME, "btnK")
    GOOGLE_SEARCH_BUTTON_ALTERNATIVE = (By.CSS_SELECTOR, "input[name='btnK']")
    FEELING_LUCKY_BUTTON = (By.NAME, "btnI")

    # Search suggestions dropdown
    SEARCH_SUGGESTIONS = (By.CSS_SELECTOR, "ul[role='listbox'] li")
    SEARCH_SUGGESTIONS_CONTAINER = (By.CSS_SELECTOR, "ul[role='listbox']")

    # Logo - multiple alternatives pentru diferite versiuni Google
    GOOGLE_LOGO = (By.CSS_SELECTOR, "img[alt*='Google']")
    GOOGLE_LOGO_ALTERNATIVE = (By.ID, "hplogo")
    GOOGLE_LOGO_ALTERNATIVE2 = (By.CSS_SELECTOR, "div[jsname] img")
    GOOGLE_LOGO_ALTERNATIVE3 = (By.XPATH, "//img[contains(@src, 'logo')]")

    # Language/region
    LANGUAGE_SELECTOR = (By.ID, "SIvCob")

    # Footer links
    FOOTER_LINKS = (By.CSS_SELECTOR, "#fbar a")


class GoogleResultsPageLocators:
    """Locatori pentru pagina de rezultate Google"""

    # Search box in results page
    SEARCH_BOX = (By.NAME, "q")
    SEARCH_BOX_ALTERNATIVE = (By.CSS_SELECTOR, "input[name='q']")

    # Search results - multiple selectors pentru robustețe
    SEARCH_RESULTS = (By.CSS_SELECTOR, "div.g, div[data-sokoban-container]")
    SEARCH_RESULTS_ALTERNATIVE = (By.CSS_SELECTOR, "div[jscontroller][lang]")
    SEARCH_RESULT_LINKS = (By.CSS_SELECTOR, "div.g a, div[data-sokoban-container] a")
    SEARCH_RESULT_TITLES = (By.CSS_SELECTOR, "h3")
    SEARCH_RESULT_DESCRIPTIONS = (By.CSS_SELECTOR, "div.VwiC3b, div[data-content-feature='1']")

    # Result stats (showing count of results)
    RESULT_STATS = (By.ID, "result-stats")
    RESULT_STATS_ALTERNATIVE = (By.CSS_SELECTOR, "#result-stats")

    # Did you mean suggestion - multiple selectors for different Google versions
    DID_YOU_MEAN = (By.CSS_SELECTOR, "a.gL9Hy")
    DID_YOU_MEAN_ALTERNATIVE = (By.XPATH, "//a[contains(@class, 'spell')]")
    DID_YOU_MEAN_TEXT = (By.CSS_SELECTOR, "a.gL9Hy")
    SHOWING_RESULTS_FOR = (By.CSS_SELECTOR, "p.card-section a")
    # New locators for modern Google design (2025)
    SHOWING_RESULTS_FOR_NEW = (By.XPATH, "//*[contains(text(), 'Vezi rezultate pentru') or contains(text(), 'Showing results for')]")
    ORIGINALLY_SEARCHED_FOR = (By.XPATH, "//*[contains(text(), 'Ai căutat inițial') or contains(text(), 'Search instead for')]")

    # Pagination
    NEXT_PAGE = (By.ID, "pnnext")
    PREVIOUS_PAGE = (By.ID, "pnprev")
    PAGE_NUMBERS = (By.CSS_SELECTOR, "td a.fl")

    # No results message
    NO_RESULTS_MESSAGE = (By.CSS_SELECTOR, "div.mnr-c")

    # Search tools
    TOOLS_BUTTON = (By.ID, "hdtb-tls")

    # Filters (Images, Videos, News, etc.)
    FILTERS = (By.CSS_SELECTOR, "div[role='navigation'] a")

    # Top navigation
    ALL_TAB = (By.CSS_SELECTOR, "a[data-hveid]")
    IMAGES_TAB = (By.LINK_TEXT, "Images")
    VIDEOS_TAB = (By.LINK_TEXT, "Videos")
    NEWS_TAB = (By.LINK_TEXT, "News")


class CommonLocators:
    """Locatori comuni folosiți în mai multe pagini"""

    # Generic button locators
    BUTTON_BY_TEXT = "//button[contains(text(), '{}')]"
    LINK_BY_TEXT = "//a[contains(text(), '{}')]"

    # Generic input locators
    INPUT_BY_NAME = "//input[@name='{}']"
    INPUT_BY_ID = "//input[@id='{}']"
    INPUT_BY_PLACEHOLDER = "//input[@placeholder='{}']"

    # Generic text locators
    TEXT_CONTAINS = "//*[contains(text(), '{}')]"
    HEADING_BY_TEXT = "//h{}[contains(text(), '{}')]"  # h1, h2, h3, etc.

    # Generic container locators
    DIV_BY_CLASS = "//div[@class='{}']"
    SPAN_BY_CLASS = "//span[@class='{}']"

    # Generic validation
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error, .error-message, [class*='error']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".success, .success-message, [class*='success']")

    # Loading indicators
    LOADING_SPINNER = (By.CSS_SELECTOR, ".loading, .spinner, [class*='loading']")

    # Modal/Dialog
    MODAL_DIALOG = (By.CSS_SELECTOR, "[role='dialog']")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "[role='dialog'] button[aria-label*='close']")


class XPathLocators:
    """XPath locatori generici pentru situații complexe"""

    @staticmethod
    def element_with_text(element_type, text):
        """Găsește element după tip și text
        Args:
            element_type: tip element (div, span, button, etc.)
            text: textul căutat
        """
        return (By.XPATH, f"//{element_type}[contains(text(), '{text}')]")

    @staticmethod
    def element_with_attribute(element_type, attribute, value):
        """Găsește element după tip și atribut
        Args:
            element_type: tip element
            attribute: numele atributului
            value: valoarea atributului
        """
        return (By.XPATH, f"//{element_type}[@{attribute}='{value}']")

    @staticmethod
    def parent_of_element(child_locator):
        """Găsește părintele unui element"""
        return f"{child_locator}/parent::*"

    @staticmethod
    def sibling_of_element(element_locator):
        """Găsește fratele următor al unui element"""
        return f"{element_locator}/following-sibling::*[1]"
