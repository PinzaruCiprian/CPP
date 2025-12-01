"""
Locators pentru pagina de test Elite Shoppy e-commerce
Toate locatorii sunt relativi și utilizează clase și ID-uri pentru identificare
"""

class Locators:
    """Locatori generici pentru aplicație"""
    
    # Header & Navigation
    SIGN_IN_BUTTON = '[data-toggle="modal"][data-target="#myModal"]'
    SIGN_UP_BUTTON = '[data-toggle="modal"][data-target="#myModal2"]'
    CART_BUTTON = '.w3view-cart'
    HEADER = '.header-bot'
    NAVIGATION_MENU = 'nav.navbar'
    HOME_LINK = 'a.menu__link'
    WOMENS_LINK = 'a.menu__link'
    MENS_LINK = 'a.menu__link'
    CONTACT_LINK = 'a.menu__link'
    
    # Login Modal (myModal)
    LOGIN_MODAL = '#myModal'
    LOGIN_NAME_INPUT = 'input[name="Name"]'
    LOGIN_EMAIL_INPUT = 'input[name="Email"]'
    LOGIN_SUBMIT_BUTTON = 'input[type="submit"][value="Sign In"]'
    LOGIN_MODAL_CLOSE = 'button.close'
    
    # Sign Up Modal (myModal2)
    SIGNUP_MODAL = '#myModal2'
    SIGNUP_NAME_INPUT = 'input[name="Name"]'
    SIGNUP_EMAIL_INPUT = 'input[name="Email"]'
    SIGNUP_PASSWORD_INPUT = 'input[name="password"]'
    SIGNUP_CONFIRM_PASSWORD_INPUT = 'input[name="Confirm Password"]'
    SIGNUP_SUBMIT_BUTTON = 'input[type="submit"][value="Sign Up"]'
    
    # Products
    PRODUCT_ITEMS = '.product-men'
    PRODUCT_IMAGE = '.product-men .pro-image-front'
    PRODUCT_TITLE = '.product-men h4'
    PRODUCT_PRICE = '.product-men .item_price'
    PRODUCT_LINK = '.link-product-add-cart'
    ADD_TO_CART_BUTTON = '.product-men input[type="submit"]'
    PRODUCT_COUNT = '.product-men'
    
    # Search
    SEARCH_BAR = 'input[type="search"]'
    SEARCH_BUTTON = 'input[type="submit"]'
    SEARCH_RESULTS = '.product-men'
    NO_RESULTS_MESSAGE = '.no-results, .error-message'
    
    # Community Poll
    RADIO_BUTTONS = 'input[name="radio"]'
    POLL_SUBMIT_BUTTON = 'input[value="SEND"]'
    
    # Sort & Filter
    SORT_DROPDOWN = '#country1'
    PRICE_FILTER_INPUT = '#amount'
    
    # Footer & Info
    FOOTER = '.copy-right, .footer-social'
    FOOTER_CONTACT_LINK = 'a.menu__link[href*="contact"]'
    PAGE_TITLE = 'h1, .page-head_agile_info_w3l h3'
    PHONE_LINK = 'a[href*="phone"]'
    EMAIL_LINK = 'a[href*="mailto"]'
    
    # Generic Elements
    SPINNER = '.loading'
    ERROR_MESSAGE = '.error-message'
    SUCCESS_MESSAGE = '.success-message'
    PAGE_NOT_FOUND = '.not-found, .error-404'


class ValidationMessages:
    """Mesaje de validare așteptate"""
    
    FIELD_REQUIRED = "Este obligatoriu"
    INVALID_EMAIL = "Email-ul nu este valid"
    PASSWORD_MISMATCH = "Parolele nu se potrivesc"
    LOGIN_SUCCESS = "Autentificare reușită"
    SIGNUP_SUCCESS = "Înregistrare reușită"
    LOGIN_FAILED = "Credențiale invalide"
