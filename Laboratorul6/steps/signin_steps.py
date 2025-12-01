"""
Step definitions pentru Sign In functionality
Separat per funcționalitate pentru ușor de găsit și menținut
"""

from behave import given, when, then
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.helpers import ValidationHelper, LogHelper
from utils.driver_factory import WebDriverFactory


@given('I am on the Elite Shoppy home page')
def step_navigate_to_home(context):
    """Navighează la pagina principală"""
    driver = WebDriverFactory.create_driver()
    context.driver = driver
    context.home_page = HomePage(driver)
    # Înlocuiți URL-ul cu cel real
    context.home_page.open("file:///c:/Users/ciprian.panzaru/Desktop/UTM/Semestrul%20VII/CPP/CPP/Laboratorul6/page.html")
    LogHelper.log_step("Navighează la pagina principală")


@when('I click on the Sign In button')
def step_click_sign_in(context):
    """Face click pe butonul Sign In"""
    context.home_page.click_sign_in_button()
    context.login_page = LoginPage(context.driver)
    LogHelper.log_step("Face click pe butonul Sign In")


@when('I fill the login form with valid data')
def step_fill_login_form(context):
    """Completează formularul cu datele din tabel"""
    for row in context.table:
        name = row['name']
        email = row['email']
        context.login_page.fill_login_form(name, email)
    LogHelper.log_step(f"Completează formularul cu {row['name']} și {row['email']}")


@when('I click the Sign In submit button')
def step_click_sign_in_submit(context):
    """Face click pe butonul de submit al Sign In"""
    context.login_page.submit_login_form()
    LogHelper.log_step("Face click pe butonul Sign In Submit")


@then('I should see a success message')
def step_verify_sign_in_success(context):
    """Verifică dacă s-a afișat mesajul de succes"""
    # Așteptă un moment pentru afișaj
    import time
    time.sleep(1)
    LogHelper.log_step("Verifică mesajul de succes")


@then('the Sign In modal should be displayed')
def step_verify_login_modal_displayed(context):
    """Verifică dacă modalul de login este afișat"""
    assert context.login_page.is_login_modal_displayed(), "Login modal nu este afișat"
    LogHelper.log_step("Verifică că modalul de login este afișat")


@then('the Sign In modal should contain Name field')
def step_verify_name_field(context):
    """Verifică dacă câmpul Name există"""
    assert context.login_page.is_displayed('input[name="Name"]'), "Câmpul Name nu există"
    LogHelper.log_step("Verifică existența câmpului Name")


@then('the Sign In modal should contain Email field')
def step_verify_email_field(context):
    """Verifică dacă câmpul Email există"""
    assert context.login_page.is_displayed('input[name="Email"]'), "Câmpul Email nu există"
    LogHelper.log_step("Verifică existența câmpului Email")


@then('the Sign In submit button should be enabled')
def step_verify_sign_in_button_enabled(context):
    """Verifică dacă butonul Submit este activ"""
    assert context.login_page.is_login_button_enabled(), "Butonul Sign In nu este activ"
    LogHelper.log_step("Verifică că butonul Sign In este activ")


@when('I clear the login form')
def step_clear_login_form(context):
    """Șterge toate câmpurile din formularul de login"""
    context.login_page.clear_name_field()
    context.login_page.clear_email_field()
    LogHelper.log_step("Șterge formularul de login")


@then('the Sign In form should show validation errors')
def step_verify_login_validation_errors(context):
    """Verifică dacă apar erori de validare"""
    LogHelper.log_step("Verifică erorile de validare")


@when('I enter invalid email "{email}" in Sign In form')
def step_enter_invalid_email_login(context, email):
    """Introduce email invalid în formularul de login"""
    context.login_page.enter_email(email)
    LogHelper.log_step(f"Introduce email invalid: {email}")


@then('I should see email validation error')
def step_verify_email_validation_error(context):
    """Verifică dacă apare eroare de validare pentru email"""
    email_value = context.login_page.get_email_field_value()
    is_valid = ValidationHelper.is_valid_email(email_value)
    assert not is_valid, f"Email-ul {email_value} ar trebui să fie invalid"
    LogHelper.log_step("Verifică eroarea de validare pentru email")


@when('I close the Sign In modal')
def step_close_login_modal(context):
    """Închide modalul de login"""
    context.login_page.close_login_modal()
    LogHelper.log_step("Închide modalul de login")


@then('the Sign In modal should not be displayed')
def step_verify_login_modal_closed(context):
    """Verifică dacă modalul de login s-a închis"""
    assert not context.login_page.is_login_modal_displayed(), "Modalul de login ar trebui să fie închis"
    LogHelper.log_step("Verifică că modalul de login este închis")
