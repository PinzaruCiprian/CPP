"""
README - Ghid pentru rularea testelor BDD cu Cucumber (Behave) și Selenium

STRUCTURA PROIECTULUI
=====================

/Laboratorul6/
├── features/              # Feature files (Gherkin - limbajul BDD)
│   ├── 01_sign_in.feature
│   ├── 02_sign_up.feature
│   ├── 03_data_validation.feature
│   └── 04_home_page.feature
│
├── steps/                 # Step definitions (implementare pași)
│   ├── environment.py     # Setup și teardown pentru testare
│   ├── signin_steps.py    # Pași pentru Sign In
│   ├── signup_steps.py    # Pași pentru Sign Up
│   ├── validation_steps.py # Pași pentru validare date
│   └── homepage_steps.py  # Pași pentru Home Page
│
├── pages/                 # Page Object Models
│   ├── base_page.py       # Clasa de bază cu metode comune
│   ├── home_page.py       # Modelul paginii principale
│   ├── login_page.py      # Modelul paginii de login
│   └── signup_page.py     # Modelul paginii de Sign Up
│
├── utils/                 # Utilități și helpers
│   ├── locators.py        # Locatori generici pentru elemente
│   ├── helpers.py         # Helpers pentru validare și WebDriver
│   └── driver_factory.py  # Factory pentru gestionare WebDriver
│
├── requirements.txt       # Dependințe Python
├── behave.ini            # Configurare Behave
├── run_tests.py          # Script pentru rularea testelor
└── page.html             # Pagina HTML pentru testare


INSTALARE DEPENDINȚE
====================

1. Asigurați-vă că aveți Python 3.8+ instalat
2. Instalați dependințele:

   pip install -r requirements.txt


RULAREA TESTELOR
================

1. Rularea tuturor testelor:
   
   python run_tests.py

2. Rularea unui feature specific:
   
   python run_tests.py --feature 01_sign_in

3. Rularea testelor cu tag-uri specifice:
   
   python run_tests.py --tags @smoke

4. Rularea directă cu behave:
   
   behave features/


STRUCTURA FEATURE FILES
=======================

Fiecare feature file utilizează Gherkin (limbaj natural BDD):

Feature: Descriere funcționalitate
  As a [persoană]
  I want to [acțiune]
  So that [beneficiu]

  Background:
    [Setup comun pentru toate scenariile]

  Scenario: Descriere scenariu
    Given [condiție inițială]
    When [acțiune]
    Then [rezultat așteptat]


LOCATORI GENERICI
=================

Toți locatorii sunt definiți în utils/locators.py și utilizează:
- CSS Selectors (pentru simplitate și viteză)
- Clase HTML și ID-uri
- Cai relative pentru identificare

Exemplu:
  LOGIN_NAME_INPUT = 'input[name="Name"]'
  LOGIN_EMAIL_INPUT = 'input[name="Email"]'


PAGE OBJECT MODEL
=================

Fiecare pagină are propria clasă care extinde BasePage:

class HomePage(BasePage):
    def click_sign_in_button(self):
        return self.click(Locators.SIGN_IN_BUTTON)


VALIDARE GENERICĂ
=================

Funcții de validare generice în helpers.py:

ValidationHelper.is_valid_email(email)
ValidationHelper.is_valid_name(name)
ValidationHelper.is_valid_password(password)
ValidationHelper.are_passwords_matching(pwd1, pwd2)


WEBDRIVER FACTORY
=================

Gestionare WebDriver centralizată:

WebDriverFactory.create_driver()   # Creare driver
WebDriverFactory.get_driver()      # Obține driver
WebDriverFactory.close_driver()    # Închide driver


TEST EXECUTION FLOW
===================

1. before_all() - Inițializare globală
2. before_scenario() - Setup pentru fiecare scenariu
3. Step implementations - Executia pașilor
4. after_scenario() - Cleanup pentru fiecare scenariu
5. after_all() - Cleanup global


CARACTERISTICI
==============

✓ Testare BDD cu Gherkin
✓ Selenium WebDriver cu Chrome Browser
✓ Page Object Model pattern
✓ Validare de date generică
✓ Locatori generici și ușor de menținut
✓ Pasii sunt bine organizați pe funcționalități
✓ Suport pentru tabel de date în Gherkin
✓ Logging și raportare test


TIPURI DE TESTE
===============

1. Sign In - Testează funcționalitatea de autentificare
2. Sign Up - Testează funcționalitatea de înregistrare
3. Data Validation - Testează validarea datelor introduse
4. Home Page - Testează interacțiunile pe pagina principală


NOTE IMPORTANTE
===============

- URL-ul paginii HTML este setat în step 'I am on the Elite Shoppy home page'
- Chrome trebuie instalat pe sistem
- WebDriverManager descarcă automat ChromeDriver
- Testele rulează pe Chrome în mod normal (nu headless)


TROUBLESHOOTING
===============

Dacă testele nu funcționează:

1. Verificați dacă Chrome este instalat
2. Verificați dependințele: pip install -r requirements.txt
3. Verificați URL-ul paginii HTML
4. Verificați locatorii din locators.py
5. Rulați cu output verbose: behave --no-capture


CONTACT
=======

Pentru întrebări sau probleme, consultați documentația Behave:
https://behave.readthedocs.io/
"""

print(__doc__)
