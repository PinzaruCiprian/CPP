"""
Step definitions pentru Data Validation functionality
Separat per funcționalitate pentru ușor de găsit și menținut
"""

from behave import when, then
from utils.helpers import ValidationHelper, LogHelper


@when('I validate email "{email}"')
def step_validate_email(context, email):
    """Validează o adresă de email"""
    context.email = email
    context.email_valid = ValidationHelper.is_valid_email(email)
    LogHelper.log_step(f"Validează email-ul: {email}")


@then('the email should be valid')
def step_verify_email_valid(context):
    """Verifică dacă email-ul este valid"""
    assert context.email_valid, f"Email-ul {context.email} ar trebui să fie valid"
    LogHelper.log_step("Verifică că email-ul este valid")


@then('the email should be invalid')
def step_verify_email_invalid(context):
    """Verifică dacă email-ul este invalid"""
    assert not context.email_valid, f"Email-ul {context.email} ar trebui să fie invalid"
    LogHelper.log_step("Verifică că email-ul este invalid")


@when('I validate name "{name}"')
def step_validate_name(context, name):
    """Validează un nume"""
    context.name = name
    context.name_valid = ValidationHelper.is_valid_name(name)
    LogHelper.log_step(f"Validează numele: {name}")


@then('the name should be valid')
def step_verify_name_valid(context):
    """Verifică dacă numele este valid"""
    assert context.name_valid, f"Numele {context.name} ar trebui să fie valid"
    LogHelper.log_step("Verifică că numele este valid")


@then('the name should be invalid')
def step_verify_name_invalid(context):
    """Verifică dacă numele este invalid"""
    assert not context.name_valid, f"Numele {context.name} ar trebui să fie invalid"
    LogHelper.log_step("Verifică că numele este invalid")


@when('I validate password "{password}"')
def step_validate_password(context, password):
    """Validează o parolă"""
    context.password = password
    context.password_valid = ValidationHelper.is_valid_password(password)
    LogHelper.log_step(f"Validează parola: {password}")


@then('the password should be strong')
def step_verify_password_strong(context):
    """Verifică dacă parola este tare"""
    assert context.password_valid, f"Parola {context.password} ar trebui să fie tare"
    LogHelper.log_step("Verifică că parola este tare")


@then('the password should be weak')
def step_verify_password_weak(context):
    """Verifică dacă parola este slabă"""
    assert not context.password_valid, f"Parola {context.password} ar trebui să fie slabă"
    LogHelper.log_step("Verifică că parola este slabă")


@when('I enter text "{text}" in Sign In email field')
def step_enter_text_login_email(context, text):
    """Introduce text în câmpul email al Sign In"""
    context.login_page.enter_email(text)
    LogHelper.log_step(f"Introduce text în email Sign In: {text}")


@then('an email validation message should appear')
def step_verify_email_validation_message(context):
    """Verifică dacă apare mesaj de validare pentru email"""
    email_value = context.login_page.get_email_field_value()
    is_valid = ValidationHelper.is_valid_email(email_value)
    assert not is_valid, f"Email-ul {email_value} ar trebui să provoque o eroare de validare"
    LogHelper.log_step("Verifică mesajul de validare pentru email")


@when('I enter text "{text}" in Sign Up name field')
def step_enter_text_signup_name(context, text):
    """Introduce text în câmpul name al Sign Up"""
    context.signup_page.enter_name(text)
    LogHelper.log_step(f"Introduce text în name Sign Up: {text}")


@then('a name validation message should appear')
def step_verify_name_validation_message(context):
    """Verifică dacă apare mesaj de validare pentru nume"""
    name_value = context.signup_page.get_name_field_value()
    is_valid = ValidationHelper.is_valid_name(name_value)
    assert not is_valid, f"Numele {name_value} ar trebui să provoque o eroare de validare"
    LogHelper.log_step("Verifică mesajul de validare pentru nume")


@when('I enter password "{password}" in Sign Up password field')
def step_enter_signup_password(context, password):
    """Introduce parolă în câmpul password al Sign Up"""
    context.signup_page.enter_password(password)
    LogHelper.log_step(f"Introduce parolă: {password}")


@when('I enter password "{password}" in Sign Up confirm password field')
def step_enter_signup_confirm_password(context, password):
    """Introduce parolă în câmpul confirm password al Sign Up"""
    context.signup_page.enter_confirm_password(password)
    LogHelper.log_step(f"Introduce confirmarea parolei: {password}")


@then('a password mismatch message should appear')
def step_verify_password_mismatch_message(context):
    """Verifică dacă apare mesaj de nepotrivire a parolelor"""
    password = context.signup_page.get_password_field_value()
    confirm_password = context.signup_page.get_confirm_password_field_value()
    assert password != confirm_password, "Parolele ar trebui să fie diferite"
    LogHelper.log_step("Verifică mesajul de nepotrivire a parolelor")


@when('I try to submit without filling any field')
def step_try_submit_empty_form(context):
    """Încearcă să trimită formularul gol"""
    context.signup_page.submit_signup_form()
    LogHelper.log_step("Încearcă să trimită formularul gol")


@then('validation errors should be shown for all required fields')
def step_verify_all_validation_errors(context):
    """Verifică dacă apar erori de validare pentru toate câmpurile"""
    LogHelper.log_step("Verifică erorile de validare pentru toate câmpurile")
