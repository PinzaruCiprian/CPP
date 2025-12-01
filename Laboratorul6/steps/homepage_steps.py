"""
Step definitions pentru Home Page functionality
Separat per funcționalitate pentru ușor de găsit și menținut
"""

from behave import then
from utils.helpers import LogHelper


@then('the home page should be loaded successfully')
def step_verify_home_page_loaded(context):
    """Verifică dacă pagina principală s-a încărcat"""
    assert context.home_page.is_home_page_loaded(), "Pagina principală nu s-a încărcat corect"
    LogHelper.log_step("Verifică că pagina principală este încărcată")


@then('Sign In button should be visible')
def step_verify_sign_in_button_visible(context):
    """Verifică dacă butonul Sign In este vizibil"""
    assert context.home_page.is_displayed('a[data-toggle="modal"][data-target="#myModal"]'), \
        "Butonul Sign In nu este vizibil"
    LogHelper.log_step("Verifică că butonul Sign In este vizibil")


@then('Sign Up button should be visible')
def step_verify_sign_up_button_visible(context):
    """Verifică dacă butonul Sign Up este vizibil"""
    assert context.home_page.is_displayed('a[data-toggle="modal"][data-target="#myModal2"]'), \
        "Butonul Sign Up nu este vizibil"
    LogHelper.log_step("Verifică că butonul Sign Up este vizibil")


@then('Cart button should be visible')
def step_verify_cart_button_visible(context):
    """Verifică dacă butonul Coș este vizibil"""
    assert context.home_page.is_cart_button_visible(), "Butonul Coș nu este vizibil"
    LogHelper.log_step("Verifică că butonul Coș este vizibil")


@then('the page should display products')
def step_verify_products_displayed(context):
    """Verifică dacă pagina afișează produse"""
    products = context.home_page.get_products()
    assert len(products) > 0, "Nu sunt afișate produse"
    LogHelper.log_step(f"Verifică că {len(products)} produse sunt afișate")


@then('at least one product should be visible')
def step_verify_at_least_one_product(context):
    """Verifică dacă cel puțin un produs este vizibil"""
    products = context.home_page.get_products()
    assert len(products) >= 1, "Nu este nici un produs vizibil"
    LogHelper.log_step(f"Verifică că cel puțin un produs este vizibil")


@when('I click on a product Quick View button')
def step_click_product_quick_view(context):
    """Face click pe butonul Quick View al unui produs"""
    context.home_page.click_product_quick_view(0)
    LogHelper.log_step("Face click pe butonul Quick View")


@then('the product details should be displayed')
def step_verify_product_details_displayed(context):
    """Verifică dacă detaliile produsului sunt afișate"""
    LogHelper.log_step("Verifică că detaliile produsului sunt afișate")


@when('I select a poll option')
def step_select_poll_option(context):
    """Selectează o opțiune din sondaj"""
    context.home_page.select_poll_option(0)
    LogHelper.log_step("Selectează o opțiune din sondaj")


@when('I submit the poll')
def step_submit_poll(context):
    """Trimite sondajul"""
    context.home_page.submit_poll()
    LogHelper.log_step("Trimite sondajul")


@then('the poll should be submitted successfully')
def step_verify_poll_submitted(context):
    """Verifică dacă sondajul s-a trimis cu succes"""
    LogHelper.log_step("Verifică că sondajul s-a trimis cu succes")


@when('I sort products by "{sort_option}"')
def step_sort_products(context, sort_option):
    """Sortează produsele după o opțiune"""
    context.home_page.sort_products(sort_option)
    LogHelper.log_step(f"Sortează produsele după: {sort_option}")


@then('products should be sorted correctly')
def step_verify_products_sorted(context):
    """Verifică dacă produsele sunt sortate corect"""
    LogHelper.log_step("Verifică că produsele sunt sortate corect")
