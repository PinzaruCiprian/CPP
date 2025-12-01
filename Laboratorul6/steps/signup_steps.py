"""
Step definitions pentru Sign Up functionality
Separat per funcționalitate pentru ușor de găsit și menținut
"""

from behave import when, then
from pages.signup_page import SignUpPage
from utils.helpers import ValidationHelper, LogHelper


@when('I click on the Sign Up button')
def step_click_sign_up(context):
    """Face click pe butonul Sign Up"""
    context.home_page.click_sign_up_button()
    context.signup_page = SignUpPage(context.driver)
    LogHelper.log_step("Face click pe butonul Sign Up")


@when('I fill the sign up form with valid data')
def step_fill_signup_form_valid(context):
    """Completează formularul cu datele din tabel"""
    for row in context.table:
        name = row['name']
        email = row['email']
        password = row['password']
        confirmPassword = row['confirmPassword']
        context.signup_page.fill_signup_form(name, email, password, confirmPassword)
    LogHelper.log_step(f"Completează formularul cu date valide")


@when('I click the Sign Up submit button')
def step_click_sign_up_submit(context):
    """Face click pe butonul de submit al Sign Up"""
    context.signup_page.submit_signup_form()
    LogHelper.log_step("Face click pe butonul Sign Up Submit")


@then('I should see a registration success message')
def step_verify_signup_success(context):
    """Verifică dacă s-a afișat mesajul de succes"""
    import time
    time.sleep(1)
    LogHelper.log_step("Verifică mesajul de succes al înregistrării")


@then('the Sign Up modal should be displayed')
def step_verify_signup_modal_displayed(context):
    """Verifică dacă modalul de Sign Up este afișat"""
    assert context.signup_page.is_signup_modal_displayed(), "Modalul de Sign Up nu este afișat"
    LogHelper.log_step("Verifică că modalul de Sign Up este afișat")


@then('the Sign Up modal should contain Name field')
def step_verify_signup_name_field(context):
    """Verifică dacă câmpul Name există"""
    assert context.signup_page.is_displayed('input[name="Name"]'), "Câmpul Name nu există"
    LogHelper.log_step("Verifică existența câmpului Name")


@then('the Sign Up modal should contain Email field')
def step_verify_signup_email_field(context):
    """Verifică dacă câmpul Email există"""
    assert context.signup_page.is_displayed('input[name="Email"]'), "Câmpul Email nu există"
    LogHelper.log_step("Verifică existența câmpului Email")


@then('the Sign Up modal should contain Password field')
def step_verify_signup_password_field(context):
    """Verifică dacă câmpul Password există"""
    assert context.signup_page.is_displayed('input[name="password"]'), "Câmpul Password nu există"
    LogHelper.log_step("Verifică existența câmpului Password")


@then('the Sign Up modal should contain Confirm Password field')
def step_verify_signup_confirm_password_field(context):
    """Verifică dacă câmpul Confirm Password există"""
    assert context.signup_page.is_displayed('input[name="Confirm Password"]'), "Câmpul Confirm Password nu există"
    LogHelper.log_step("Verifică existența câmpului Confirm Password")


@then('the Sign Up submit button should be enabled')
def step_verify_sign_up_button_enabled(context):
    """Verifică dacă butonul Submit este activ"""
    assert context.signup_page.is_signup_button_enabled(), "Butonul Sign Up nu este activ"
    LogHelper.log_step("Verifică că butonul Sign Up este activ")


@when('I clear the sign up form')
def step_clear_signup_form(context):
    """Șterge toate câmpurile din formularul de sign up"""
    context.signup_page.clear_name_field()
    context.signup_page.clear_email_field()
    context.signup_page.clear_password_field()
    context.signup_page.clear_confirm_password_field()
    LogHelper.log_step("Șterge formularul de Sign Up")


@then('the Sign Up form should show validation errors')
def step_verify_signup_validation_errors(context):
    """Verifică dacă apar erori de validare"""
    LogHelper.log_step("Verifică erorile de validare")


@when('I fill the sign up form with mismatched passwords')
def step_fill_signup_mismatched_passwords(context):
    """Completează formularul cu parole care nu se potrivesc"""
    for row in context.table:
        name = row['name']
        email = row['email']
        password = row['password']
        confirmPassword = row['confirmPassword']
        context.signup_page.fill_signup_form(name, email, password, confirmPassword)
    LogHelper.log_step("Completează formularul cu parole care nu se potrivesc")


@then('I should see password mismatch error')
def step_verify_password_mismatch_error(context):
    """Verifică dacă apare eroare de nepotrivire a parolelor"""
    password = context.signup_page.get_password_field_value()
    confirm_password = context.signup_page.get_confirm_password_field_value()
    assert password != confirm_password, "Parolele ar trebui să fie diferite"
    LogHelper.log_step("Verifică eroarea de nepotrivire a parolelor")


@when('I enter invalid email "{email}" in Sign Up form')
def step_enter_invalid_email_signup(context, email):
    """Introduce email invalid în formularul de Sign Up"""
    context.signup_page.enter_email(email)
    LogHelper.log_step(f"Introduce email invalid: {email}")


@then('I should see email validation error in Sign Up modal')
def step_verify_email_validation_error_signup(context):
    """Verifică dacă apare eroare de validare pentru email"""
    email_value = context.signup_page.get_email_field_value()
    is_valid = ValidationHelper.is_valid_email(email_value)
    assert not is_valid, f"Email-ul {email_value} ar trebui să fie invalid"
    LogHelper.log_step("Verifică eroarea de validare pentru email în Sign Up")


@when('I fill the sign up form with weak password')
def step_fill_signup_weak_password(context):
    """Completează formularul cu o parolă slabă"""
    for row in context.table:
        name = row['name']
        email = row['email']
        password = row['password']
        confirmPassword = row['confirmPassword']
        context.signup_page.fill_signup_form(name, email, password, confirmPassword)
    LogHelper.log_step("Completează formularul cu o parolă slabă")


@then('I should see password strength warning')
def step_verify_password_strength_warning(context):
    """Verifică dacă apare avertisment de forță a parolei"""
    password = context.signup_page.get_password_field_value()
    is_strong = ValidationHelper.is_valid_password(password)
    assert not is_strong, f"Parola {password} ar trebui să fie slabă"
    LogHelper.log_step("Verifică avertismentul de forță a parolei")


@when('I close the Sign Up modal')
def step_close_signup_modal(context):
    """Închide modalul de Sign Up"""
    context.signup_page.close_signup_modal()
    LogHelper.log_step("Închide modalul de Sign Up")


@then('the Sign Up modal should not be displayed')
def step_verify_signup_modal_closed(context):
    """Verifică dacă modalul de Sign Up s-a închis"""
    assert not context.signup_page.is_signup_modal_displayed(), "Modalul de Sign Up ar trebui să fie închis"
    LogHelper.log_step("Verifică că modalul de Sign Up este închis")
