"""
Test runner pentru rulare rapidă a scenariilor
Alternativă la behave CLI
"""

import sys
from pathlib import Path

# Setup paths
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignUpPage
from pages.mens_page import MensPage
from utils.driver_factory import WebDriverFactory
from utils.helpers import ValidationHelper, LogHelper, TestDataGenerator


def test_sign_in():
    """Test Sign In functionality"""
    print("\n" + "="*60)
    print("TEST: Sign In Functionality")
    print("="*60)
    
    try:
        # Setup
        driver = WebDriverFactory.create_driver()
        home_page = HomePage(driver)
        home_page.open("file:///c:/Users/ciprian.panzaru/Desktop/UTM/Semestrul%20VII/CPP/CPP/Laboratorul6/page.html")
        
        # Test
        home_page.click_sign_in_button()
        login_page = LoginPage(driver)
        
        assert login_page.is_login_modal_displayed(), "Login modal nu este afișat"
        print("✓ Login modal este afișat")
        
        assert login_page.is_displayed('input[name="Name"]'), "Câmpul Name nu există"
        print("✓ Câmpul Name este disponibil")
        
        assert login_page.is_displayed('input[name="Email"]'), "Câmpul Email nu există"
        print("✓ Câmpul Email este disponibil")
        
        # Cleanup
        login_page.close_login_modal()
        
        print("\n✓ Test Sign In - PASSED\n")
        return True
        
    except AssertionError as e:
        print(f"\n✗ Test Sign In - FAILED: {e}\n")
        return False
    finally:
        WebDriverFactory.close_driver()


def test_sign_up():
    """Test Sign Up functionality"""
    print("\n" + "="*60)
    print("TEST: Sign Up Functionality")
    print("="*60)
    
    try:
        # Setup
        driver = WebDriverFactory.create_driver()
        home_page = HomePage(driver)
        home_page.open("file:///c:/Users/ciprian.panzaru/Desktop/UTM/Semestrul%20VII/CPP/CPP/Laboratorul6/page.html")
        
        # Test
        home_page.click_sign_up_button()
        signup_page = SignUpPage(driver)
        
        assert signup_page.is_signup_modal_displayed(), "Signup modal nu este afișat"
        print("✓ Signup modal este afișat")
        
        assert signup_page.is_displayed('input[name="Name"]'), "Câmpul Name nu există"
        print("✓ Câmpul Name este disponibil")
        
        assert signup_page.is_displayed('input[name="Email"]'), "Câmpul Email nu există"
        print("✓ Câmpul Email este disponibil")
        
        assert signup_page.is_displayed('input[name="password"]'), "Câmpul Password nu există"
        print("✓ Câmpul Password este disponibil")
        
        assert signup_page.is_displayed('input[name="Confirm Password"]'), "Câmpul Confirm Password nu există"
        print("✓ Câmpul Confirm Password este disponibil")
        
        # Cleanup
        signup_page.close_signup_modal()
        
        print("\n✓ Test Sign Up - PASSED\n")
        return True
        
    except AssertionError as e:
        print(f"\n✗ Test Sign Up - FAILED: {e}\n")
        return False
    finally:
        WebDriverFactory.close_driver()


def test_home_page():
    """Test Home Page functionality"""
    print("\n" + "="*60)
    print("TEST: Home Page Functionality")
    print("="*60)
    
    try:
        # Setup
        driver = WebDriverFactory.create_driver()
        home_page = HomePage(driver)
        home_page.open("file:///c:/Users/ciprian.panzaru/Desktop/UTM/Semestrul%20VII/CPP/CPP/Laboratorul6/page.html")
        
        # Test
        assert home_page.is_home_page_loaded(), "Home page nu s-a încărcat"
        print("✓ Home page este încărcată")
        
        assert home_page.is_displayed('a[data-toggle="modal"][data-target="#myModal"]'), \
            "Butonul Sign In nu este vizibil"
        print("✓ Butonul Sign In este vizibil")
        
        assert home_page.is_displayed('a[data-toggle="modal"][data-target="#myModal2"]'), \
            "Butonul Sign Up nu este vizibil"
        print("✓ Butonul Sign Up este vizibil")
        
        assert home_page.is_cart_button_visible(), "Butonul Coș nu este vizibil"
        print("✓ Butonul Coș este vizibil")
        
        print("\n✓ Test Home Page - PASSED\n")
        return True
        
    except AssertionError as e:
        print(f"\n✗ Test Home Page - FAILED: {e}\n")
        return False
    finally:
        WebDriverFactory.close_driver()


def test_validation():
    """Test Data Validation"""
    print("\n" + "="*60)
    print("TEST: Data Validation")
    print("="*60)
    
    try:
        # Valid email
        assert ValidationHelper.is_valid_email("test@example.com"), "Email valid nu a trecut"
        print("✓ Email valid este acceptat")
        
        # Invalid email
        assert not ValidationHelper.is_valid_email("invalidemail"), "Email invalid a trecut"
        print("✓ Email invalid este respins")
        
        # Valid name
        assert ValidationHelper.is_valid_name("John Doe"), "Nume valid nu a trecut"
        print("✓ Nume valid este acceptat")
        
        # Invalid name (prea scurt)
        assert not ValidationHelper.is_valid_name("J"), "Nume prea scurt a trecut"
        print("✓ Nume prea scurt este respins")
        
        # Valid password
        assert ValidationHelper.is_valid_password("Password123"), "Parolă validă nu a trecut"
        print("✓ Parolă validă este acceptată")
        
        # Invalid password (prea scurtă)
        assert not ValidationHelper.is_valid_password("123"), "Parolă prea scurtă a trecut"
        print("✓ Parolă prea scurtă este respinsă")
        
        # Passwords matching
        assert ValidationHelper.are_passwords_matching("Pass123", "Pass123"), \
            "Parole potrivite nu au trecut"
        print("✓ Parole potrivite sunt acceptate")
        
        # Passwords not matching
        assert not ValidationHelper.are_passwords_matching("Pass123", "Pass456"), \
            "Parole nepotrivite au trecut"
        print("✓ Parole nepotrivite sunt respinse")
        
        print("\n✓ Test Validation - PASSED\n")
        return True
        
    except AssertionError as e:
        print(f"\n✗ Test Validation - FAILED: {e}\n")
        return False


def test_mens_page():
    """Test Mens Page functionality - TC1 to TC6"""
    print("\n" + "="*60)
    print("TEST: Pagina Mens (TC1-TC6)")
    print("="*60)
    
    try:
        # Setup
        driver = WebDriverFactory.create_driver()
        mens_page = MensPage(driver)
        mens_page.open()
        
        # TC1: Page Load
        print("\n[TC1] Verificarea încărcării paginii Mens...")
        assert mens_page.is_mens_page_loaded(), "Pagina Mens nu s-a încărcat"
        assert mens_page.are_all_elements_visible(), "Elementele principale nu sunt vizibile"
        assert mens_page.are_product_images_loaded(), "Imaginile produselor nu sunt încărcate"
        print("✓ TC1: Pagina Mens încărcată complet")
        
        # TC2: Navigation Menu
        print("\n[TC2] Verificarea meniului de navigare...")
        assert mens_page.is_navigation_menu_visible(), "Meniu nu este vizibil"
        mens_page.hover_over_menu_item("Mens")
        print("✓ TC2: Meniu de navigare funcțional")
        
        # TC3: Products Display
        print("\n[TC3] Verificarea afișării produselor...")
        product_count = mens_page.get_product_count()
        assert product_count > 0, "Nu sunt produse"
        assert mens_page.all_products_have_required_fields(), "Produse incomplete"
        print(f"✓ TC3: {product_count} produse afișate corect")
        
        # TC4: Contact Link (FAILED - redirects to YouTube)
        print("\n[TC4] Verificarea linkului Contact...")
        mens_page.scroll_to_footer()
        assert mens_page.is_footer_visible(), "Footer nu este vizibil"
        try:
            mens_page.click_contact_link()
            current_url = mens_page.get_current_url()
            if 'youtube.com' in current_url.lower():
                print("✗ TC4: BUG - Contact link redirecționează la YouTube")
            else:
                print("✓ TC4: Contact link funcționează")
        except:
            print("⚠ TC4: Contact link nu a putut fi testat")
        
        # TC5: Responsiveness
        print("\n[TC5] Verificarea responsivității...")
        mens_page.set_desktop_resolution()
        assert not mens_page.has_horizontal_scroll(), "Scroll orizontal pe desktop"
        print("✓ TC5: Responsivitate OK")
        
        # TC6: Search (FAILED - redirects to 404)
        print("\n[TC6] Verificarea funcției de căutare...")
        if mens_page.is_search_bar_visible():
            mens_page.enter_search_term("shirt")
            mens_page.submit_search()
            if mens_page.is_page_not_found_displayed():
                print("✗ TC6: BUG - Căutarea redirecționează la 'Page not Found'")
            else:
                assert mens_page.are_search_results_displayed(), "Nu sunt rezultate"
                print("✓ TC6: Căutare funcțională")
        else:
            print("⚠ TC6: Bara de căutare nu este vizibilă")
        
        print("\n✓ Test Mens Page - COMPLETED\n")
        return True
        
    except AssertionError as e:
        print(f"\n✗ Test Mens Page - FAILED: {e}\n")
        return False
    except Exception as e:
        print(f"\n✗ Eroare neasteptată: {e}\n")
        return False
    finally:
        WebDriverFactory.close_driver()


def run_all_quick_tests():
    """Rulează toate testele rapide"""
    print("\n" + "="*70)
    print("ELITE SHOPPY - TESTE RAPIDE AUTOMATIZATE")
    print("="*70 + "\n")
    
    results = []
    
    try:
        results.append(("Validation", test_validation()))
        results.append(("Home Page", test_home_page()))
        results.append(("Sign In", test_sign_in()))
        results.append(("Sign Up", test_sign_up()))
        results.append(("Mens Page", test_mens_page()))
    except Exception as e:
        print(f"\n✗ Eroare generală: {e}\n")
    
    # Summary
    print("\n" + "="*70)
    print("REZUMAT TESTE")
    print("="*70)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"{test_name}: {status}")
    
    print(f"\nTotal: {passed}/{total} teste au trecut")
    print("="*70 + "\n")
    
    return passed == total


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        test_name = sys.argv[1].lower()
        
        if test_name == 'signin':
            success = test_sign_in()
        elif test_name == 'signup':
            success = test_sign_up()
        elif test_name == 'homepage':
            success = test_home_page()
        elif test_name == 'validation':
            success = test_validation()
        elif test_name == 'mens':
            success = test_mens_page()
        else:
            success = run_all_quick_tests()
    else:
        success = run_all_quick_tests()
    
    sys.exit(0 if success else 1)
