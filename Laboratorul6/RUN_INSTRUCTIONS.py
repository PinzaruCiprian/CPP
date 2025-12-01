#!/usr/bin/env python3
"""
INSTRUCȚIUNI RULARE TESTE - LABORATORUL 6
============================================

Acest script contine instrucțiuni detaliate pentru rularea testelor
test case-urilor TC1-TC6 (pagina Mens)
"""

def print_header(text):
    print("\n" + "="*70)
    print(text.center(70))
    print("="*70 + "\n")

def print_section(title):
    print("\n" + "▶ " + title)
    print("-" * 70)

def show_instructions():
    print_header("LABORATORUL 6 - INSTRUCȚIUNI RULARE TESTE")
    
    print("Acest laborator testează 6 test case-uri pentru pagina Mens a site-ului")
    print("Elite Shoppy, utilizând framework BDD cu Behave și Selenium WebDriver.")
    
    print_section("1. VERIFICARE PREREQUISITE")
    
    print("""
✓ Python 3.8+ instalat
✓ Git instalat (optional, pentru clonare repo)
✓ Chrome Browser instalat (versiunea 120+)
✓ Conexiune internet stabilă
✓ Administrator rights (dacă e necesar pentru WebDriver)
    """)
    
    print_section("2. INSTALARE DEPENDINȚE")
    
    print("""
Rulează în terminal/PowerShell (din directorul laboratorului):

    pip install -r requirements.txt

Aceasta va instala:
    - behave==1.2.6         # BDD framework
    - selenium==4.15.2      # WebDriver
    - webdriver-manager==4.0.1  # Gestionare ChromeDriver
    - pytest==7.4.3         # Test framework
    - pytest-bdd==6.1.1     # BDD pentru pytest
    - python-dotenv==1.0.0  # Variabile mediu
    """)
    
    print_section("3. OPȚIUNI RULARE TESTE")
    
    print("""
╔════════════════════════════════════════════════════════════════════╗
║ A) RULARE CU BEHAVE (RECOMANDATĂ)                                  ║
╚════════════════════════════════════════════════════════════════════╝

Toate testele laboratorului 6:
    python run_tests.py

Doar testele paginii Mens (TC1-TC6):
    python run_tests.py --mens

Doar teste reușite (TC1, TC2, TC3, TC5):
    python run_tests.py --passed

Doar teste eșuate (TC4, TC6):
    python run_tests.py --failed

Cu Behave direct:
    behave features/05_mens_page.feature
    behave features/05_mens_page.feature --tags=@high
    behave features/05_mens_page.feature --tags=@failed
    """)
    
    print("""
╔════════════════════════════════════════════════════════════════════╗
║ B) RULARE TESTE RAPIDE (DIRECT PYTHON)                              ║
╚════════════════════════════════════════════════════════════════════╝

Toate testele rapide (inclusiv Mens):
    python quick_test.py

Doar pagina Mens:
    python quick_test.py mens

Doar alte teste:
    python quick_test.py signin
    python quick_test.py signup
    python quick_test.py homepage
    python quick_test.py validation
    """)
    
    print("""
╔════════════════════════════════════════════════════════════════════╗
║ C) RULARE BEHAVE DIRECT (ADVANCED)                                  ║
╚════════════════════════════════════════════════════════════════════╝

Toate feature-urile:
    behave features/

Cu format verbose:
    behave features/05_mens_page.feature --no-capture

Cu tag specific:
    behave features/ --tags=@high
    behave features/ --tags=@smoke
    behave features/ --tags=@failed

Cu exclude tag:
    behave features/ --tags=~@failed
    """)
    
    print_section("4. TEST CASE MAPPING")
    
    print("""
┌─────────────────────────────────────────────────────────────────┐
│ Test Case │ Denumire                        │ Status │ Priority │
├─────────────────────────────────────────────────────────────────┤
│ TC1       │ Încărcare pagină Mens           │ PASSED │ Normal   │
│ TC2       │ Funcționalitate meniu navigare  │ PASSED │ High     │
│ TC3       │ Afișare produse Mens            │ PASSED │ Normal   │
│ TC4       │ Contact link footer (BUG)       │ FAILED │ Low      │
│ TC5       │ Responsivitate pagina           │ PASSED │ High     │
│ TC6       │ Funcție căutare (BUG)           │ FAILED │ High     │
└─────────────────────────────────────────────────────────────────┘

Total: 6 test cases | Passed: 4 (66.67%) | Failed: 2 (33.33%)
    """)
    
    print_section("5. BUGS IDENTIFICATE")
    
    print("""
BUG-001: Contact Link redirecționează la YouTube
    - Severity: MEDIUM
    - Status: NOT FIXED (expected TC4 failure)
    - Impact: Contact page nu este accesibilă din footer
    
BUG-002: Search Function redirecționează la 404
    - Severity: HIGH
    - Status: NOT FIXED (expected TC6 failure)
    - Impact: Funcție de căutare nu funcționează deloc

Aceștia sunt bugs INTENȚIONALI în aplicație pentru a demonstra
test case-urile failed.
    """)
    
    print_section("6. EXPECTED TEST OUTPUT")
    
    print("""
Exemplu output test reușit (TC1):
    Feature: Verificarea funcționalităților paginii Mens
      Background:
        Given I navigate to the Mens page
      
      Scenario: TC1 - Verificarea încărcării corecte a paginii Mens
        Given the Mens page is loaded completely
        When I wait for page to load
        Then the page should load within 3 seconds
        And all main elements should be visible
        And product images should be loaded
        And CSS and JS resources should be available

Rezultat: ✓ PASSED

---

Exemplu output test eșuat (TC6):
    Scenario: TC6 - Verificarea funcției de căutare (pozitiv)
        Given the search bar is visible and active
        When I enter "shirt" in search field
        And I press Enter or click Search button
        Then search results should display relevant products
        AssertionError: BUG: Search redirected to 'Page not Found' error

Rezultat: ✗ FAILED
    """)
    
    print_section("7. TROUBLESHOOTING")
    
    print("""
Problemă: Chrome nu se deschide
    → Soluție: Verifică dacă Chrome e instalat, rulează:
               pip install --upgrade webdriver-manager

Problemă: ModuleNotFoundError
    → Soluție: Asigură-te că ai rulat `pip install -r requirements.txt`

Problemă: Element not found
    → Soluție: Verifică locatorii din utils/locators.py
               Sigur aplicația a accesat URL-ul corect?

Problemă: Timeout on element
    → Soluție: Crește timeout în WebDriverWait (base_page.py)
               URL-ul site-ului este accesibil?

Problemă: StaleElementReference
    → Soluție: Framework reîncarcă element automat
               Dacă persistă, raportează bug
    """)
    
    print_section("8. FIȘIERE IMPORTANTE")
    
    print("""
📂 Structura Proiect:

features/05_mens_page.feature      - 6 scenarii Gherkin (TC1-TC6)
steps/mens_page_steps.py            - 40+ step definitions
pages/mens_page.py                  - Page Object Model complet
utils/locators.py                   - CSS selectors (actualizat)

run_tests.py                        - Test runner principal
quick_test.py                       - Test runner rapid (Python direct)
requirements.txt                    - Dependințe Python
behave.ini                          - Config Behave
pytest.ini                          - Config pytest

TEST_REPORT_LAB6.md                 - Raport detailat (ACEST FIȘIER)
GHID_COMPLET.md                     - Ghid complet în Română
README.md                           - Ghid general
    """)
    
    print_section("9. EXEMPLE RULARE PRACTICĂ")
    
    print("""
EXEMPLU 1: Vreau să văd toate testele Mens
    $ python run_tests.py --mens
    
EXEMPLU 2: Vreau test rapid fără Behave
    $ python quick_test.py mens
    
EXEMPLU 3: Vreau doar testele care au trecut
    $ python run_tests.py --passed
    
EXEMPLU 4: Vreau doar testele care au eșuat (bug demonstrations)
    $ python run_tests.py --failed
    
EXEMPLU 5: Vreau să rulez direct cu Behave, high priority
    $ behave features/05_mens_page.feature --tags=@high
    """)
    
    print_section("10. UNDERSTANDING TEST RESULTS")
    
    print("""
✓ PASSED   - Test reușit, funcționalitate OK
✗ FAILED   - Test eșuat, bug depistat sau assertion failed
⚠ SKIPPED  - Test omis (de ex: feature not available)
? UNKNOWN  - Status neclar (error în setup)

TAGS Utilizate:
    @smoke      - Teste critique pentru smoke testing
    @high       - Prioritate High importance
    @normal     - Prioritate Standard
    @low        - Prioritate Low
    @failed     - Expected failures (bugs depistate)

TAGS din feature file pot fi combinate:
    @smoke @high        - Smoke test de prioritate HIGH
    @failed @high       - Failed test de prioritate HIGH
    """)
    
    print_section("11. VALIDARE INSTALARE")
    
    print("""
Verifică dacă tot e setup corect:

    python -m pip list | grep -i behave
    python -m pip list | grep -i selenium
    python -m pip list | grep -i webdriver

Sau:

    python -c "import behave; print(behave.__version__)"
    python -c "import selenium; print(selenium.__version__)"
    python -c "from webdriver_manager.chrome import ChromeDriverManager; print('OK')"
    """)
    
    print_section("12. REPORT GENERARE")
    
    print("""
După rulare, poți vedea:

1. Behave genereaza output în terminal
2. Errors sunt listați cu detalii
3. Pasos care eșuează sunt evidențiați
4. Execution time total e afișat

Pentru HTML report (advanced):
    behave features/ -f html -o reports/

Pentru JSON report (CI/CD):
    behave features/ -f json.pretty -o reports/report.json
    """)
    
    print_section("13. NEXT STEPS DUPĂ TESTE")
    
    print("""
După executare:

1. Consulta TEST_REPORT_LAB6.md pentru detalii complete
2. Review bugs depistate (BUG-001, BUG-002)
3. Adaugă teste suplimentare pentru edge cases
4. Implementă screenshot capture pe failure
5. Integrează în CI/CD pipeline

Pentru feature development:
    - Adaugă noi feature files în features/
    - Implementă step definitions în steps/
    - Creeaza noi Page Objects în pages/
    - Update locators în utils/locators.py
    """)
    
    print_header("GATA! EȘTI PREGĂTIT SĂ RULEZI TESTE")
    
    print("""
Recomandare inițială:
    
    $ python quick_test.py mens
    
Aceasta va rula teste rapid fără dependența de Behave CLI.

Pentru full BDD experience:
    
    $ python run_tests.py --mens
    
Baftă la testare! 🚀
    """)

if __name__ == "__main__":
    try:
        show_instructions()
    except KeyboardInterrupt:
        print("\n\nInterupere utilizator.\n")
    except Exception as e:
        print(f"\nEroare: {e}\n")
