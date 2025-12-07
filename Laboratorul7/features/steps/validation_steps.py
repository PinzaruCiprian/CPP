"""
Step definitions generice pentru validarea datelor.
Acești pași pot fi reutilizați în diferite scenarii și funcționalități.
"""
import time
from behave import given, when, then
from selenium.webdriver.common.by import By


# ============================================================================
# Generic URL validation steps
# ============================================================================

@then('URL-ul curent ar trebui să conțină "{url_fragment}"')
def step_verify_url_contains(context, url_fragment):
    """
    Verifică că URL-ul curent conține un fragment specific
    """
    current_url = context.driver.current_url
    assert url_fragment in current_url, \
        f"URL doesn't contain '{url_fragment}'. Current URL: {current_url}"
    print(f"URL contains '{url_fragment}'")


@then('URL-ul curent ar trebui să fie "{expected_url}"')
def step_verify_exact_url(context, expected_url):
    """
    Verifică că URL-ul curent este exact cel așteptat
    """
    current_url = context.driver.current_url
    assert current_url == expected_url, \
        f"URL mismatch. Expected: '{expected_url}', Actual: '{current_url}'"
    print(f"URL is: {current_url}")


# ============================================================================
# Generic element visibility validation steps
# ============================================================================

@then('elementul cu id "{element_id}" ar trebui să fie vizibil')
def step_verify_element_by_id_visible(context, element_id):
    """
    Verifică că un element cu ID specific este vizibil
    """
    from utils.helpers import ElementHelpers
    locator = (By.ID, element_id)
    is_visible = ElementHelpers.is_element_visible(context.driver, locator)
    assert is_visible, f"Element with id '{element_id}' is not visible"
    print(f"Element with id '{element_id}' is visible")


@then('elementul cu clasa "{class_name}" ar trebui să fie vizibil')
def step_verify_element_by_class_visible(context, class_name):
    """
    Verifică că un element cu clasă specifică este vizibil
    """
    from utils.helpers import ElementHelpers
    locator = (By.CLASS_NAME, class_name)
    is_visible = ElementHelpers.is_element_visible(context.driver, locator)
    assert is_visible, f"Element with class '{class_name}' is not visible"
    print(f"Element with class '{class_name}' is visible")


@then('elementul cu xpath "{xpath}" ar trebui să fie vizibil')
def step_verify_element_by_xpath_visible(context, xpath):
    """
    Verifică că un element cu XPath specific este vizibil
    """
    from utils.helpers import ElementHelpers
    locator = (By.XPATH, xpath)
    is_visible = ElementHelpers.is_element_visible(context.driver, locator)
    assert is_visible, f"Element with xpath '{xpath}' is not visible"
    print(f"Element with xpath '{xpath}' is visible")


# ============================================================================
# Generic element presence validation steps
# ============================================================================

@then('elementul cu id "{element_id}" ar trebui să fie prezent')
def step_verify_element_by_id_present(context, element_id):
    """
    Verifică că un element cu ID specific este prezent în DOM
    """
    from utils.helpers import ElementHelpers
    locator = (By.ID, element_id)
    is_present = ElementHelpers.is_element_present(context.driver, locator)
    assert is_present, f"Element with id '{element_id}' is not present"
    print(f"Element with id '{element_id}' is present")


@then('elementul cu clasa "{class_name}" ar trebui să fie prezent')
def step_verify_element_by_class_present(context, class_name):
    """
    Verifică că un element cu clasă specifică este prezent în DOM
    """
    from utils.helpers import ElementHelpers
    locator = (By.CLASS_NAME, class_name)
    is_present = ElementHelpers.is_element_present(context.driver, locator)
    assert is_present, f"Element with class '{class_name}' is not present"
    print(f"Element with class '{class_name}' is present")


# ============================================================================
# Generic text validation steps
# ============================================================================

@then('pagina ar trebui să conțină textul "{expected_text}"')
def step_verify_page_contains_text(context, expected_text):
    """
    Verifică că pagina conține un text specific
    """
    page_source = context.driver.page_source
    assert expected_text in page_source, \
        f"Page doesn't contain text '{expected_text}'"
    print(f"Page contains text '{expected_text}'")


@then('elementul cu id "{element_id}" ar trebui să conțină textul "{expected_text}"')
def step_verify_element_contains_text(context, element_id, expected_text):
    """
    Verifică că un element conține un text specific
    """
    from utils.helpers import ElementHelpers
    locator = (By.ID, element_id)
    element_text = ElementHelpers.get_element_text(context.driver, locator)
    assert expected_text in element_text, \
        f"Element text '{element_text}' doesn't contain '{expected_text}'"
    print(f"Element contains text '{expected_text}'")


@then('titlul paginii ar trebui să fie "{expected_title}"')
def step_verify_page_title(context, expected_title):
    """
    Verifică titlul paginii
    """
    actual_title = context.driver.title
    assert expected_title in actual_title, \
        f"Page title mismatch. Expected: '{expected_title}', Actual: '{actual_title}'"
    print(f"Page title: {actual_title}")


@then('titlul paginii ar trebui să conțină "{title_fragment}"')
def step_verify_page_title_contains(context, title_fragment):
    """
    Verifică că titlul paginii conține un fragment specific
    """
    actual_title = context.driver.title
    assert title_fragment in actual_title, \
        f"Page title doesn't contain '{title_fragment}'. Actual title: '{actual_title}'"
    print(f"Page title contains '{title_fragment}'")


# ============================================================================
# Generic count validation steps
# ============================================================================

@then('ar trebui să existe exact {expected_count:d} elemente cu clasa "{class_name}"')
def step_verify_element_count_exact(context, expected_count, class_name):
    """
    Verifică numărul exact de elemente cu o clasă specifică
    """
    elements = context.driver.find_elements(By.CLASS_NAME, class_name)
    actual_count = len(elements)
    assert actual_count == expected_count, \
        f"Expected {expected_count} elements, but found {actual_count}"
    print(f"Found exactly {actual_count} elements with class '{class_name}'")


@then('ar trebui să existe cel puțin {min_count:d} elemente cu clasa "{class_name}"')
def step_verify_element_count_minimum(context, min_count, class_name):
    """
    Verifică numărul minim de elemente cu o clasă specifică
    """
    elements = context.driver.find_elements(By.CLASS_NAME, class_name)
    actual_count = len(elements)
    assert actual_count >= min_count, \
        f"Expected at least {min_count} elements, but found {actual_count}"
    print(f"Found {actual_count} elements with class '{class_name}' (minimum {min_count})")


@then('ar trebui să existe cel mult {max_count:d} elemente cu clasa "{class_name}"')
def step_verify_element_count_maximum(context, max_count, class_name):
    """
    Verifică numărul maxim de elemente cu o clasă specifică
    """
    elements = context.driver.find_elements(By.CLASS_NAME, class_name)
    actual_count = len(elements)
    assert actual_count <= max_count, \
        f"Expected at most {max_count} elements, but found {actual_count}"
    print(f"Found {actual_count} elements with class '{class_name}' (maximum {max_count})")


# ============================================================================
# Generic attribute validation steps
# ============================================================================

@then('elementul cu id "{element_id}" ar trebui să aibă atributul "{attribute_name}" cu valoarea "{expected_value}"')
def step_verify_element_attribute_value(context, element_id, attribute_name, expected_value):
    """
    Verifică valoarea unui atribut al unui element
    """
    element = context.driver.find_element(By.ID, element_id)
    actual_value = element.get_attribute(attribute_name)
    assert actual_value == expected_value, \
        f"Attribute '{attribute_name}' has value '{actual_value}', expected '{expected_value}'"
    print(f"Element attribute '{attribute_name}' has value '{actual_value}'")


@then('elementul cu id "{element_id}" ar trebui să fie enabled')
def step_verify_element_enabled(context, element_id):
    """
    Verifică că un element este enabled
    """
    element = context.driver.find_element(By.ID, element_id)
    assert element.is_enabled(), f"Element with id '{element_id}' is not enabled"
    print(f"Element with id '{element_id}' is enabled")


@then('elementul cu id "{element_id}" ar trebui să fie disabled')
def step_verify_element_disabled(context, element_id):
    """
    Verifică că un element este disabled
    """
    element = context.driver.find_element(By.ID, element_id)
    assert not element.is_enabled(), f"Element with id '{element_id}' is not disabled"
    print(f"Element with id '{element_id}' is disabled")


# ============================================================================
# Generic wait validation steps
# ============================================================================

@then('ar trebui să aștept {seconds:d} secunde')
def step_wait_seconds(context, seconds):
    """
    Așteaptă un număr specific de secunde
    """
    time.sleep(seconds)
    print(f"Waited {seconds} seconds")


@then('elementul cu id "{element_id}" ar trebui să dispară în {timeout:d} secunde')
def step_verify_element_disappears(context, element_id, timeout):
    """
    Verifică că un element dispare în timpul specificat
    """
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    locator = (By.ID, element_id)
    try:
        WebDriverWait(context.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )
        print(f"Element with id '{element_id}' disappeared")
    except Exception as e:
        raise AssertionError(f"Element with id '{element_id}' did not disappear in {timeout} seconds")


# ============================================================================
# Generic screenshot steps
# ============================================================================

@then('iau un screenshot cu numele "{screenshot_name}"')
def step_take_screenshot(context, screenshot_name):
    """
    Ia un screenshot cu un nume specific
    """
    from utils.helpers import ScreenshotHelpers
    filepath = ScreenshotHelpers.take_screenshot(context.driver, screenshot_name)
    if filepath:
        print(f"Screenshot saved: {filepath}")
        # Atașează screenshot-ul la raport (dacă este suportat)
        if hasattr(context, 'screenshots'):
            context.screenshots.append(filepath)
    else:
        print("Failed to take screenshot")


# ============================================================================
# Generic input validation steps
# ============================================================================

@when('introduc textul "{text}" în elementul cu id "{element_id}"')
def step_enter_text_in_element(context, text, element_id):
    """
    Introduce text într-un element cu ID specific
    """
    from utils.helpers import ElementHelpers
    locator = (By.ID, element_id)
    success = ElementHelpers.safe_send_keys(context.driver, locator, text)
    assert success, f"Failed to enter text in element with id '{element_id}'"
    print(f"Entered text '{text}' in element with id '{element_id}'")


@when('fac click pe elementul cu id "{element_id}"')
def step_click_element_by_id(context, element_id):
    """
    Face click pe un element cu ID specific
    """
    from utils.helpers import ElementHelpers
    locator = (By.ID, element_id)
    success = ElementHelpers.safe_click(context.driver, locator)
    assert success, f"Failed to click element with id '{element_id}'"
    print(f"Clicked element with id '{element_id}'")


@when('fac click pe elementul cu clasa "{class_name}"')
def step_click_element_by_class(context, class_name):
    """
    Face click pe un element cu clasă specifică
    """
    from utils.helpers import ElementHelpers
    locator = (By.CLASS_NAME, class_name)
    success = ElementHelpers.safe_click(context.driver, locator)
    assert success, f"Failed to click element with class '{class_name}'"
    print(f"Clicked element with class '{class_name}'")


# ============================================================================
# Generic scroll validation steps
# ============================================================================

@when('scroll la sfârșitul paginii')
def step_scroll_to_bottom(context):
    """
    Scroll la sfârșitul paginii
    """
    from utils.helpers import ScrollHelpers
    ScrollHelpers.scroll_to_bottom(context.driver)
    print("Scrolled to bottom of page")


@when('scroll la începutul paginii')
def step_scroll_to_top(context):
    """
    Scroll la începutul paginii
    """
    from utils.helpers import ScrollHelpers
    ScrollHelpers.scroll_to_top(context.driver)
    print("Scrolled to top of page")


@when('scroll la elementul cu id "{element_id}"')
def step_scroll_to_element(context, element_id):
    """
    Scroll la un element specific
    """
    from utils.helpers import ScrollHelpers
    locator = (By.ID, element_id)
    ScrollHelpers.scroll_to_element(context.driver, locator)
    print(f"Scrolled to element with id '{element_id}'")
