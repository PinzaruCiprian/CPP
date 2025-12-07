"""
Factory pentru crearea și configurarea WebDriver.
Toate testele rulează în browserul Chrome.
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class DriverFactory:
    """Factory class pentru gestionarea WebDriver"""

    @staticmethod
    def get_chrome_driver(headless=False, maximize=True):
        """
        Creează și configurează un Chrome WebDriver

        Args:
            headless (bool): Rulează browser în mod headless
            maximize (bool): Maximizează fereastra browser-ului

        Returns:
            WebDriver: Instanță configurată de Chrome WebDriver
        """
        # Configurare opțiuni Chrome
        chrome_options = Options()

        # Setări pentru performanță și stabilitate
        chrome_options.add_argument("--incognito")  # Mod incognito
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Evită detecția automation

        # Dezactivează notificările
        chrome_options.add_experimental_option(
            "prefs", {
                "profile.default_content_setting_values.notifications": 2,
                "profile.default_content_settings.popups": 0,
                "download.prompt_for_download": False
            }
        )

        # Exclude logging și automation flags pentru a evita detecția
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
        chrome_options.add_experimental_option('useAutomationExtension', False)

        # Mod headless (optional)
        if headless:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window-size=1920,1080")

        # User agent pentru a evita bot detection
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )

        # Folosește webdriver-manager pentru a gestiona automat ChromeDriver
        # NU SE FOLOSESC CĂILE ABSOLUTE - se lasă managerul să gestioneze
        import os

        # Verifică dacă există chromedriver în directorul curent sau în PATH
        chromedriver_path = None
        local_paths = [
            os.path.join("drivers", "chromedriver.exe"),  # Cale relativă la proiect
            "chromedriver.exe"  # În directorul curent sau PATH
        ]

        for path in local_paths:
            if os.path.exists(path):
                chromedriver_path = os.path.abspath(path)
                print(f"[OK] Found ChromeDriver at: {path}")
                break

        if chromedriver_path:
            service = Service(chromedriver_path)
        else:
            # Folosește webdriver-manager (gestionează automat descărcarea)
            try:
                import platform
                print("[INFO] Using webdriver-manager to download ChromeDriver...")

                # Forțează descărcarea versiunii win64 pentru Windows 64-bit
                if platform.system() == "Windows" and platform.machine().endswith('64'):
                    # Șterge cache-ul vechi win32 și forțează win64
                    import shutil
                    cache_path = os.path.join(os.path.expanduser("~"), ".wdm", "drivers", "chromedriver")
                    if os.path.exists(cache_path):
                        try:
                            shutil.rmtree(cache_path)
                            print("[INFO] Cleared old ChromeDriver cache")
                        except:
                            pass

                service = Service(ChromeDriverManager().install())
                print("[OK] ChromeDriver installed successfully")
            except Exception as e:
                print(f"[ERROR] WebDriver Manager failed: {e}")
                raise Exception("ChromeDriver not found! Please install Chrome browser or add chromedriver.exe to drivers/ folder")

        # Creează WebDriver
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Elimină flag-ul webdriver pentru a evita detecția bot
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {
            "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        # Setări suplimentare
        if maximize:
            driver.maximize_window()

        # Timeouts
        driver.implicitly_wait(10)  # Implicit wait
        driver.set_page_load_timeout(30)  # Page load timeout

        return driver

    @staticmethod
    def quit_driver(driver):
        """
        Închide și curăță WebDriver

        Args:
            driver: Instanța WebDriver de închis
        """
        if driver:
            try:
                driver.quit()
            except Exception as e:
                print(f"Error closing driver: {e}")


class DriverConfig:
    """Configurații pentru WebDriver"""

    # Implicit wait time (seconds)
    IMPLICIT_WAIT = 10

    # Explicit wait time (seconds)
    EXPLICIT_WAIT = 20

    # Page load timeout (seconds)
    PAGE_LOAD_TIMEOUT = 30

    # Script timeout (seconds)
    SCRIPT_TIMEOUT = 30

    # Screenshot settings
    SCREENSHOT_ON_FAILURE = True
    SCREENSHOT_FORMAT = "png"

    # Browser settings
    BROWSER = "chrome"
    HEADLESS = False
    MAXIMIZE_WINDOW = True

    # URL settings
    BASE_URL = "https://www.google.co.in"

    @classmethod
    def get_driver(cls):
        """Convenience method pentru a obține driver cu configurații default"""
        return DriverFactory.get_chrome_driver(
            headless=cls.HEADLESS,
            maximize=cls.MAXIMIZE_WINDOW
        )
