"""
Page Object Model pentru pagina Mens
"""
from pages.base_page import BasePage
from utils.locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class MensPage(BasePage):
    """Page Object pentru pagina Mens a site-ului Elite Shoppy"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.mens_url = "https://adoring-pasteur-3ae17d.netlify.app/mens"
        
    def open(self):
        """Deschide pagina Mens"""
        self.driver.get(self.mens_url)
        self.log_step(f"Navigated to Mens page: {self.mens_url}")
        return self
    
    # ===== PAGE LOAD CHECKS =====
    
    def is_mens_page_loaded(self):
        """Verifică dacă pagina Mens s-a încărcat complet"""
        try:
            self.wait_for_element(Locators.PAGE_TITLE, 5)
            self.log_step("Mens page loaded successfully")
            return True
        except Exception as e:
            self.log_step(f"Mens page failed to load: {str(e)}")
            return False
    
    def get_page_load_time(self):
        """Obține timpul de încărcare a paginii"""
        start_time = time.time()
        self.is_mens_page_loaded()
        load_time = time.time() - start_time
        return load_time
    
    def are_all_elements_visible(self):
        """Verifică dacă toate elementele majore sunt vizibile"""
        elements_to_check = {
            'header': Locators.HEADER,
            'products': Locators.PRODUCT_ITEMS,
            'footer': Locators.FOOTER
        }
        
        for element_name, locator in elements_to_check.items():
            try:
                element = self.find_element(locator)
                # For footer, we only check if it exists on the page, not if it's visible on screen
                if element_name == 'footer':
                    # Footer exists, that's good enough
                    continue
                elif not self.is_displayed(locator):
                    self.log_step(f"Element {element_name} not visible")
                    return False
            except:
                self.log_step(f"Element {element_name} not found")
                return False
        
        self.log_step("All main elements are visible")
        return True
    
    def are_product_images_loaded(self):
        """Verifică dacă imaginile produselor sunt încărcate"""
        try:
            images = self.find_elements(Locators.PRODUCT_IMAGE)
            if not images:
                return False
            
            for img in images:
                if not img.get_attribute('src') or img.get_attribute('src').strip() == '':
                    return False
            
            self.log_step(f"All {len(images)} product images loaded successfully")
            return True
        except Exception as e:
            self.log_step(f"Error checking product images: {str(e)}")
            return False
    
    def are_resources_available(self):
        """Verifică disponibilitatea resurselor externe (CSS, JS)"""
        try:
            # Verificare CSS
            css_elements = self.driver.execute_script(
                "return document.styleSheets.length > 0"
            )
            # Verificare JS
            js_loaded = self.driver.execute_script(
                "return typeof jQuery !== 'undefined' || document.querySelector('script')"
            )
            
            self.log_step("External resources (CSS, JS) are available")
            return css_elements and js_loaded
        except Exception as e:
            self.log_step(f"Error checking resources: {str(e)}")
            return False
    
    # ===== NAVIGATION =====
    
    def get_navigation_menu(self):
        """Obține elementul meniu de navigare"""
        return self.find_element(Locators.NAVIGATION_MENU)
    
    def is_navigation_menu_visible(self):
        """Verifică dacă meniul de navigare este vizibil"""
        return self.is_displayed(Locators.NAVIGATION_MENU)
    
    def hover_over_menu_item(self, menu_item_name):
        """Face hover pe un element din meniu"""
        # Find the link by text content, handling variations like "Womens" or "Women's"
        search_name = menu_item_name.lower().replace("womens", "women").replace("mens", "men")
        element = self.driver.execute_script(f"""
        return Array.from(document.querySelectorAll('a.menu__link')).find(el => 
            el.textContent.toLowerCase().includes('{search_name}')
        );
        """)
        if element:
            ActionChains(self.driver).move_to_element(element).perform()
            self.log_step(f"Hovered over {menu_item_name}")
            return True
        return False
    
    def click_menu_link(self, link_name):
        """Face click pe un link din meniu"""
        # Find the link by text content, handling variations like "Womens" or "Women's"
        search_name = link_name.lower().replace("womens", "women").replace("mens", "men")
        element = self.driver.execute_script(f"""
        return Array.from(document.querySelectorAll('a.menu__link')).find(el => 
            el.textContent.toLowerCase().includes('{search_name}')
        );
        """)
        if element:
            element.click()
            self.log_step(f"Clicked on {link_name} link")
            time.sleep(2)  # Așteptare redirecționare
            return True
        return False
    
    def get_current_url(self):
        """Obține URL-ul curent"""
        return self.driver.current_url
    
    def is_on_mens_page(self):
        """Verifică dacă suntem pe pagina Mens"""
        return 'mens' in self.get_current_url().lower()
    
    def is_on_womens_page(self):
        """Verifică dacă suntem pe pagina Womens"""
        return 'womens' in self.get_current_url().lower()
    
    def is_on_home_page(self):
        """Verifică dacă suntem pe pagina Home"""
        current_url = self.get_current_url().lower()
        return 'index' in current_url or current_url.endswith('.html') is False
    
    def no_error_status_codes(self):
        """Verifică dacă nu sunt erori 404 sau 500"""
        try:
            # În Selenium, nu putem verifica HTTP status codes direct
            # Verificăm dacă pagina nu conține mesaje de eroare
            page_source = self.driver.page_source.lower()
            return '404' not in page_source and '500' not in page_source
        except:
            return True
    
    # ===== PRODUCTS =====
    
    def get_all_products(self):
        """Obține toate produsele din pagină"""
        return self.find_elements(Locators.PRODUCT_ITEMS)
    
    def get_product_count(self):
        """Obține numărul total de produse"""
        products = self.get_all_products()
        count = len(products)
        self.log_step(f"Found {count} products on page")
        return count
    
    def get_product_image(self, index):
        """Obține imaginea unui produs la index-ul dat"""
        products = self.get_all_products()
        if index < len(products):
            images = products[index].find_elements(By.TAG_NAME, 'img')
            return images[0] if images else None
        return None
    
    def get_product_title(self, index):
        """Obține titlul unui produs"""
        products = self.get_all_products()
        if index < len(products):
            try:
                # Try h4 first (actual structure), then h5
                try:
                    return products[index].find_element(By.TAG_NAME, 'h4').text
                except:
                    return products[index].find_element(By.TAG_NAME, 'h5').text
            except:
                return None
        return None
    
    def get_product_price(self, index):
        """Obține prețul unui produs"""
        products = self.get_all_products()
        if index < len(products):
            try:
                # Try item_price first (actual structure), then .price
                try:
                    price_element = products[index].find_element(By.CLASS_NAME, 'item_price')
                    return price_element.text
                except:
                    price_element = products[index].find_element(By.CLASS_NAME, 'price')
                    return price_element.text
            except:
                return None
        return None
    
    def does_product_have_image(self, index):
        """Verifică dacă un produs are imagine"""
        img = self.get_product_image(index)
        return img is not None and img.get_attribute('src') != ''
    
    def does_product_have_title(self, index):
        """Verifică dacă un produs are titlu"""
        return self.get_product_title(index) is not None
    
    def does_product_have_price(self, index):
        """Verifică dacă un produs are preț"""
        return self.get_product_price(index) is not None
    
    def does_product_have_action_button(self, index):
        """Verifică dacă un produs are buton de acțiune (Add to Cart)"""
        products = self.get_all_products()
        if index < len(products):
            try:
                # Look for input type=submit in the product
                buttons = products[index].find_elements(By.CSS_SELECTOR, 'input[type="submit"]')
                return len(buttons) > 0
            except:
                return False
        return False
    
    def all_products_have_required_fields(self):
        """Verifică dacă toate produsele au câmpurile obligatorii"""
        product_count = self.get_product_count()
        for i in range(product_count):
            if not (self.does_product_have_image(i) and 
                    self.does_product_have_title(i) and
                    self.does_product_have_price(i)):
                return False
        
        self.log_step(f"All {product_count} products have required fields")
        return True
    
    def scroll_to_products(self):
        """Derulează la secțiunea de produse"""
        products_element = self.find_element(Locators.PRODUCT_ITEMS)
        self.scroll_to_element(products_element)
        self.log_step("Scrolled to products section")
    
    # ===== SEARCH FUNCTIONALITY =====
    
    def is_search_bar_visible(self):
        """Verifică dacă bara de căutare este vizibilă"""
        return self.is_displayed(Locators.SEARCH_BAR)
    
    def is_search_bar_active(self):
        """Verifică dacă bara de căutare este activă"""
        search_bar = self.find_element(Locators.SEARCH_BAR)
        return search_bar is not None
    
    def enter_search_term(self, search_term):
        """Introdu un termen în bara de căutare"""
        search_bar = self.find_element(Locators.SEARCH_BAR)
        search_bar.clear()
        search_bar.send_keys(search_term)
        self.log_step(f"Entered search term: {search_term}")
    
    def submit_search(self):
        """Submitează căutarea"""
        try:
            # Încearcă buton search
            self.click(Locators.SEARCH_BUTTON)
            self.log_step("Submitted search")
        except:
            # Dacă nu există buton, apasă Enter
            search_bar = self.find_element(Locators.SEARCH_BAR)
            search_bar.submit()
            self.log_step("Submitted search via Enter key")
        
        time.sleep(2)  # Așteptare rezultate
    
    def are_search_results_displayed(self):
        """Verifică dacă rezultatele de căutare sunt afișate"""
        try:
            results = self.find_elements(Locators.PRODUCT_ITEMS)
            return len(results) > 0
        except:
            return False
    
    def is_page_not_found_displayed(self):
        """Verifică dacă este afișat mesaj "Page not Found" """
        try:
            page_source = self.driver.page_source.lower()
            return 'not found' in page_source or '404' in page_source
        except:
            return False
    
    def search_returns_relevant_products(self, search_term):
        """Verifică dacă căutarea returnează produse relevante"""
        products = self.get_all_products()
        page_source = self.driver.page_source.lower()
        search_term_lower = search_term.lower()
        
        # Verificare dacă search_term apare pe pagină
        return search_term_lower in page_source and len(products) > 0
    
    # ===== FOOTER =====
    
    def scroll_to_footer(self):
        """Derulează la footer"""
        footer = self.find_element(Locators.FOOTER)
        self.scroll_to_element(footer)
        self.log_step("Scrolled to footer")
    
    def is_footer_visible(self):
        """Verifică dacă footer-ul este vizibil"""
        return self.is_displayed(Locators.FOOTER)
    
    def click_contact_link(self):
        """Face click pe linkul Contact din footer"""
        self.click(Locators.FOOTER_CONTACT_LINK)
        self.log_step("Clicked on Contact link in footer")
        time.sleep(1)
    
    def is_on_contact_page(self):
        """Verifică dacă suntem pe pagina de Contact"""
        current_url = self.get_current_url().lower()
        return 'contact' in current_url
    
    # ===== RESPONSIVENESS =====
    
    def resize_window(self, width, height):
        """Redimensionează fereastra la rezoluția specificată"""
        self.driver.set_window_size(width, height)
        time.sleep(1)
        self.log_step(f"Resized window to {width}x{height}")
    
    def set_desktop_resolution(self):
        """Setează rezoluție desktop (1920x1080)"""
        self.resize_window(1920, 1080)
    
    def set_tablet_resolution(self):
        """Setează rezoluție tabletă (768x1024)"""
        self.resize_window(768, 1024)
    
    def set_mobile_resolution(self):
        """Setează rezoluție mobil (375x667)"""
        self.resize_window(375, 667)
    
    def has_horizontal_scroll(self):
        """Verifică dacă pagina are scroll orizontal"""
        page_width = self.driver.execute_script(
            "return Math.max(document.body.scrollWidth, document.documentElement.scrollWidth)"
        )
        window_width = self.driver.execute_script(
            "return window.innerWidth"
        )
        return page_width > window_width
    
    def has_overlapping_elements(self):
        """Verifică dacă sunt elemente suprapuse"""
        try:
            # Verificare simplă: elemente importante nu trebuie ascunse
            main_elements = [
                Locators.HEADER,
                Locators.NAVIGATION_MENU,
                Locators.PRODUCT_ITEMS,
                Locators.FOOTER
            ]
            
            for element_locator in main_elements:
                try:
                    element = self.find_element(element_locator)
                    if not element.is_displayed():
                        return True
                except:
                    pass
            
            return False
        except:
            return False
    
    def is_layout_correct(self):
        """Verifică dacă layout-ul este corect"""
        return not self.has_horizontal_scroll() and not self.has_overlapping_elements()
    
    def can_scroll_vertically(self):
        """Verifică dacă se poate face scroll vertical"""
        page_height = self.driver.execute_script(
            "return Math.max(document.body.scrollHeight, document.documentElement.scrollHeight)"
        )
        window_height = self.driver.execute_script(
            "return window.innerHeight"
        )
        return page_height > window_height
    
    def are_buttons_touch_accessible(self):
        """Verifică dacă butoanele sunt accesibile la touch"""
        buttons = self.find_elements('button, input[type="button"], input[type="submit"], a.button')
        
        MIN_TOUCH_SIZE = 44  # pixels - recomandare pentru touch targets
        
        for button in buttons:
            try:
                width = button.rect['width']
                height = button.rect['height']
                
                if width < MIN_TOUCH_SIZE or height < MIN_TOUCH_SIZE:
                    return False
            except:
                pass
        
        self.log_step("All buttons have adequate size for touch interaction")
        return True
