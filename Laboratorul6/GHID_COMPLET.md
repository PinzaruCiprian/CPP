"""
GHID COMPLET - LABORATORUL 6: Automatizare cu Cucumber BDD

==============================================================================
INTRODUCERE
==============================================================================

Acest proiect implementează automatizare BDD (Behavior-Driven Development) 
utilizând:
- Cucumber BDD (prin framework-ul Behave pentru Python)
- Selenium WebDriver
- Chrome Browser
- Pattern-ul Page Object Model

Testele automatizează funcționalitățile site-ului e-commerce "Elite Shoppy".


==============================================================================
CERINȚE SISTEM
==============================================================================

1. Python 3.8 sau mai nou
2. Chrome Browser instalat
3. pip (Python package manager)


==============================================================================
INSTALARE
==============================================================================

1. Deschideți terminal / PowerShell în directorul proiectului

2. Instalați dependințele:
   
   pip install -r requirements.txt

   Dependencies:
   - behave==1.2.6         - Framework BDD pentru Python
   - selenium==4.15.2      - WebDriver pentru automatizare
   - webdriver-manager==4.0.1 - Gestionare automată ChromeDriver
   - pytest==7.4.3         - Testing framework
   - pytest-bdd==6.1.1     - BDD pentru pytest
   - python-dotenv==1.0.0  - Variabile de mediu


==============================================================================
STRUCTURA PROIECTULUI
==============================================================================

/Laboratorul6/
│
├── features/                      # Feature files (Gherkin language)
│   ├── 01_sign_in.feature        # Teste Sign In
│   ├── 02_sign_up.feature        # Teste Sign Up
│   ├── 03_data_validation.feature # Teste validare date
│   └── 04_home_page.feature      # Teste Home Page
│
├── steps/                         # Step definitions (implementări)
│   ├── environment.py             # Setup/teardown Behave
│   ├── signin_steps.py            # Pași Sign In
│   ├── signup_steps.py            # Pași Sign Up
│   ├── validation_steps.py        # Pași validare
│   └── homepage_steps.py          # Pași Home Page
│
├── pages/                         # Page Object Models
│   ├── base_page.py              # Clasa de bază
│   ├── home_page.py              # Home Page model
│   ├── login_page.py             # Login/Sign In model
│   └── signup_page.py            # Sign Up model
│
├── utils/                         # Utilități
│   ├── locators.py               # Locatori generici (CSS selectors)
│   ├── helpers.py                # Helpers validare și WebDriver
│   ├── driver_factory.py         # Factory WebDriver Chrome
│   └── __init__.py
│
├── page.html                      # Pagina HTML pentru testare
├── requirements.txt               # Dependințe Python
├── behave.ini                    # Configurare Behave
├── pytest.ini                    # Configurare pytest
├── run_tests.py                  # Runner BDD (Behave)
├── quick_test.py                 # Teste rapide (direct Python)
└── README.md                     # Ghid general


==============================================================================
RULAREA TESTELOR
==============================================================================

### Opțiunea 1: Behave CLI (Recommended)

1. Rularea tuturor feature-urilor:
   
   behave features/
   
   sau
   
   python run_tests.py

2. Rularea unui feature specific:
   
   behave features/01_sign_in.feature
   
   sau
   
   python run_tests.py --feature 01_sign_in

3. Rularea cu verbose output:
   
   behave features/ --no-capture --tags @


### Opțiunea 2: Teste Rapide (Direct Python)

1. Rularea tuturor testelor rapide:
   
   python quick_test.py

2. Rularea unui test specific:
   
   python quick_test.py signin
   python quick_test.py signup
   python quick_test.py homepage
   python quick_test.py validation


### Opțiunea 3: pytest

1. Rularea tuturor testelor:
   
   pytest

2. Rularea cu verbose:
   
   pytest -v

3. Rularea cu output:
   
   pytest -s


==============================================================================
DESCRIEREA FEATURE-URILOR
==============================================================================

### 01_sign_in.feature - Funcționalitate Sign In

Scenarii testate:
1. Sign In reușit cu credențiale valide
2. Deschiderea corectă a modalului Sign In
3. Sign In cu câmpuri goale (validare)
4. Sign In cu email invalid
5. Închiderea modalului Sign In

Locatori utilizați:
- Sign In Button: data-toggle="modal"[data-target="#myModal"]
- Modal ID: myModal
- Câmpu Name: input[name="Name"]
- Câmpul Email: input[name="Email"]


### 02_sign_up.feature - Funcționalitate Sign Up

Scenarii testate:
1. Sign Up reușit cu date valide
2. Deschiderea corectă a modalului Sign Up
3. Sign Up cu câmpuri goale
4. Sign Up cu parole care nu se potrivesc
5. Sign Up cu email invalid
6. Sign Up cu parolă slabă
7. Închiderea modalului Sign Up

Validări:
- Lungime parolă minimum 6 caractere
- Format email valid
- Parole potrivite


### 03_data_validation.feature - Validare Date

Scenarii testate:
1. Validare format email
2. Validare format nume
3. Validare forță parolă
4. Validare email în formular Sign In
5. Validare nume în formular Sign Up
6. Validare potrivire parole
7. Validare câmpuri obligatorii

Funcții de validare (din helpers.py):
- is_valid_email()
- is_valid_name()
- is_valid_password()
- are_passwords_matching()


### 04_home_page.feature - Funcționalitate Home Page

Scenarii testate:
1. Pagina principală se încarcă corect
2. Butoane vizibile (Sign In, Sign Up, Cart)
3. Interacțiune sondaj comunitate
4. Vizualizare produse
5. Sortare produse


==============================================================================
LOCATORI GENERICI
==============================================================================

Toți locatorii sunt definiți în utils/locators.py utilizând CSS Selectors.

Exemple de locatori:

# Header & Navigation
SIGN_IN_BUTTON = '[data-toggle="modal"][data-target="#myModal"]'
SIGN_UP_BUTTON = '[data-toggle="modal"][data-target="#myModal2"]'

# Login Modal
LOGIN_MODAL = '#myModal'
LOGIN_NAME_INPUT = 'input[name="Name"]'
LOGIN_EMAIL_INPUT = 'input[name="Email"]'
LOGIN_SUBMIT_BUTTON = 'input[type="submit"][value="Sign In"]'

# Sign Up Modal
SIGNUP_MODAL = '#myModal2'
SIGNUP_NAME_INPUT = 'input[name="Name"]'
SIGNUP_PASSWORD_INPUT = 'input[name="password"]'
SIGNUP_CONFIRM_PASSWORD_INPUT = 'input[name="Confirm Password"]'


==============================================================================
PAGE OBJECT MODEL
==============================================================================

Fiecare pagină are o clasă care extinde BasePage:

Structură clasă:
```python
class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def click_sign_in_button(self):
        return self.click(Locators.SIGN_IN_BUTTON)
    
    def is_sign_in_button_visible(self):
        return self.is_displayed(Locators.SIGN_IN_BUTTON)
```

Metode disponibile în BasePage:
- click(locator) - Face click
- type_text(locator, text) - Scrie text
- get_text(locator) - Obține text
- is_displayed(locator) - Verifică vizibilitate
- is_enabled(locator) - Verifică activitate
- wait_for_element(locator, timeout) - Aștepts element
- clear_field(locator) - Șterge câmp
- get_attribute(locator, attribute) - Obține atribut


==============================================================================
VALIDARE GENERICĂ
==============================================================================

Funcții de validare în utils/helpers.py:

ValidationHelper.validate_email_format(email)
- Returnează: (bool, message)
- Verifică format valid email

ValidationHelper.validate_password_strength(password)
- Returnează: (bool, message)
- Verifică parolă minimum 6 caractere

ValidationHelper.validate_name_format(name)
- Returnează: (bool, message)
- Verifică nume minimum 2 caractere


==============================================================================
WEBDRIVER CHROME
==============================================================================

WebDriver este gestionat de WebDriverFactory în utils/driver_factory.py

Caracteristici:
✓ Utilizează Chrome Browser
✓ Descarcă automat ChromeDriver cu webdriver-manager
✓ Configurare automată pentru Chrome
✓ Implicit wait de 10 secunde
✓ Start maximized window

Utilizare:
```python
driver = WebDriverFactory.create_driver()
driver.get("http://example.com")
WebDriverFactory.close_driver()
```


==============================================================================
FLOW-ul TESTĂRII BDD
==============================================================================

1. Feature file (Gherkin) - Descriere test în limbaj natural
   ↓
2. Step definition - Implementare pas în Python
   ↓
3. Page Object Model - Interacțiune cu pagina
   ↓
4. Locators - Identificare element
   ↓
5. WebDriver - Executie comanda în browser
   ↓
6. Validation Helper - Verificare rezultat
   ↓
7. Assertion - Rapoartă succes/eșec


==============================================================================
EXEMPLU COMPLET: TEST SIGN IN
==============================================================================

1. Feature File (01_sign_in.feature):
```gherkin
Scenario: Successful sign in with valid credentials
  Given I am on the Elite Shoppy home page
  When I click on the Sign In button
  And I fill the login form with valid data:
    | name            | email              |
    | Test User       | testuser@test.com  |
  And I click the Sign In submit button
  Then I should see a success message
```

2. Step Definition (signin_steps.py):
```python
@when('I click on the Sign In button')
def step_click_sign_in(context):
    context.home_page.click_sign_in_button()
    context.login_page = LoginPage(context.driver)
```

3. Page Object (login_page.py):
```python
def click_sign_in_button(self):
    return self.click(Locators.SIGN_IN_BUTTON)
```

4. Locator (locators.py):
```python
SIGN_IN_BUTTON = '[data-toggle="modal"][data-target="#myModal"]'
```

5. WebDriver (base_page.py):
```python
def click(self, locator):
    element = self.find_element(locator)
    element.click()
```


==============================================================================
SEPARAREA PAȘILOR PER FUNCȚIONALITATE
==============================================================================

Pașii sunt separați în fișiere dedicate pentru ușor de găsit și menținut:

- signin_steps.py       - Pași pentru Sign In
- signup_steps.py       - Pași pentru Sign Up
- validation_steps.py   - Pași pentru validare date
- homepage_steps.py     - Pași pentru Home Page

Fiecare fișier conține doar pași relevanți unei funcționalități.


==============================================================================
MESAJE DE LOGGING
==============================================================================

Fiecare pas este logat pentru urmărire:

```
LogHelper.log_step("Face click pe butonul Sign In")
LogHelper.log_assertion(expected, actual)
```

Output exemplu:
  → Face click pe butonul Sign In
  → Completează formularul cu test@example.com
  ✓ Expected: modal visible, Actual: modal visible


==============================================================================
RULAREA RAPIDĂ A TESTELOR
==============================================================================

Pentru testare rapidă fără behave CLI, utilizați quick_test.py:

python quick_test.py            # Toate testele
python quick_test.py signin     # Doar Sign In
python quick_test.py signup     # Doar Sign Up
python quick_test.py homepage   # Doar Home Page
python quick_test.py validation # Doar validare

Avantaje:
✓ Mai rapid la execuție
✓ Output clar și ușor de citit
✓ Nu necesită instalare behave
✓ Ideal pentru debugging


==============================================================================
TROUBLESHOOTING
==============================================================================

### Problem: Chrome nu se deschide
Soluție:
1. Verificați dacă Chrome este instalat
2. Rulați: pip install -r requirements.txt
3. webdriver-manager va descărca ChromeDriver

### Problem: Element nu găsit
Soluție:
1. Verificați locatorul în locators.py
2. Deschideți pagina HTML în Chrome
3. Utilizați Developer Tools (F12) pentru a verifica selector-ul

### Problem: Timeout pe element
Soluție:
1. Verificați dacă pagina s-a încărcat complet
2. Creșteți timeout în WebDriverWait
3. Adăugați sleep() dacă este necesar

### Problem: StaleElementReference
Soluție:
1. Căutați element din nou după refresh
2. Utilizați WebDriverWait cu expected_conditions


==============================================================================
BEST PRACTICES
==============================================================================

1. Ponderi locatori după atribute unice (id, name, class)
2. Evitați xpath complex
3. Utilizați CSS selectors
4. Separați pașii per funcționalitate
5. Refolosiți date de test
6. Logheze toate acțiunile importante
7. Utilizați Page Object Model
8. Validați datele input
9. Testați cazuri limită (empty, invalid)
10. Închideți resursele după teste


==============================================================================
DOCUMENTAȚIE EXTERNĂ
==============================================================================

Behave BDD:
https://behave.readthedocs.io/

Selenium Python:
https://selenium-python.readthedocs.io/

Gherkin Language:
https://cucumber.io/docs/gherkin/reference/


==============================================================================
CONTACT ȘI SUPORT
==============================================================================

Pentru întrebări sau probleme, consultați:
- README.md - Ghid general
- Docstring-uri în cod
- Exemplele în fișierele de test


==============================================================================
FINALIZARE
==============================================================================

Proiectul implementează cu succes:
✓ Cucumber BDD cu Behave
✓ Selenium WebDriver cu Chrome
✓ Pași separați pe funcționalități
✓ Locatori generici și ușor de menținut
✓ Page Object Model pattern
✓ Validare generică a datelor
✓ Logging și urmărire test
✓ Teste comprehensive pentru E-Commerce site

Toate cerințele laboratorului 6 au fost îndeplinite!
"""

print(__doc__)
