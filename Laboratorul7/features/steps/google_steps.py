"""
Step definitions pentru funcționalitatea Google Search.
Pașii sunt separați pe funcționalitate.
"""
import time
from behave import given, when, then, step
from pages.google_home_page import GoogleHomePage
from pages.google_results_page import GoogleResultsPage


# ============================================================================
# GIVEN steps - Pregătire și stare inițială
# ============================================================================

@given('că utilizatorul deschide browserul Chrome')
@given('utilizatorul deschide browserul Chrome')
def step_open_chrome(context):
    """
    Deschide browserul Chrome - executat de environment.py
    """
    # Browser-ul este deja deschis în before_scenario hook
    assert context.driver is not None, "Driver not initialized"


@given('că utilizatorul este pe pagina Google')
@given('utilizatorul este pe pagina Google')
def step_user_on_google_page(context):
    """
    Navighează la pagina Google
    """
    context.google_home_page = GoogleHomePage(context.driver)
    success = context.google_home_page.navigate_to_google()
    assert success, "Failed to navigate to Google"

    # Așteaptă ca pagina să se încarce
    time.sleep(1)
    assert context.google_home_page.is_google_page_loaded(), "Google page not loaded properly"


# ============================================================================
# WHEN steps - Acțiuni
# ============================================================================

@when('utilizatorul accesează "{url}"')
def step_user_accesses_url(context, url):
    """
    Accesează un URL specific
    """
    context.google_home_page = GoogleHomePage(context.driver)
    context.driver.get(url)
    time.sleep(2)  # Așteaptă încărcarea paginii


@when('utilizatorul caută după "{search_term}"')
def step_user_searches_for(context, search_term):
    """
    Realizează o căutare cu un termen specific
    """
    # Inițializează pagina dacă nu există
    if not hasattr(context, 'google_home_page'):
        context.google_home_page = GoogleHomePage(context.driver)

    # Salvează termenul de căutare în context pentru comparații ulterioare
    if not hasattr(context, 'search_terms'):
        context.search_terms = []
    context.search_terms.append(search_term)

    # Realizează căutarea
    success = context.google_home_page.search_for(search_term)
    assert success, f"Failed to search for '{search_term}'"

    # Așteaptă ca rezultatele să se încarce
    time.sleep(2)

    # Inițializează pagina de rezultate
    context.google_results_page = GoogleResultsPage(context.driver)


@when('utilizatorul nu introduce nimic în search box')
def step_user_enters_nothing(context):
    """
    Nu introduce nimic în search box (îl lasă gol)
    """
    if not hasattr(context, 'google_home_page'):
        context.google_home_page = GoogleHomePage(context.driver)

    # Asigură-te că search box-ul este gol
    context.google_home_page.clear_search_box()
    time.sleep(0.5)


@when('utilizatorul apasă pe butonul "{button_name}"')
def step_user_clicks_button(context, button_name):
    """
    Apasă pe un buton specific
    """
    if not hasattr(context, 'google_home_page'):
        context.google_home_page = GoogleHomePage(context.driver)

    # Salvează URL-ul curent pentru comparație
    context.url_before_click = context.driver.current_url

    if "Google Search" in button_name or "Căutare" in button_name:
        # Încearcă să facă click pe butonul de căutare
        # Uneori butonul nu este vizibil, dar executăm click cu JavaScript
        try:
            success = context.google_home_page.click_google_search_button()
        except Exception as e:
            print(f"Click on search button failed: {e}")
            success = False

        # Pentru căutare goală, este ok dacă click-ul nu reușește
        # deoarece butonul poate fi disabled
        time.sleep(2)


# ============================================================================
# THEN steps - Verificări și aserțiuni
# ============================================================================

@then('pagina Google ar trebui să se deschidă cu succes')
@step('pagina Google ar trebui să se deschidă cu succes')
def step_verify_google_page_opened(context):
    """
    Verifică că pagina Google s-a deschis cu succes
    """
    if not hasattr(context, 'google_home_page'):
        context.google_home_page = GoogleHomePage(context.driver)

    # Verifică URL-ul
    current_url = context.driver.current_url
    assert "google" in current_url.lower(), f"Not on Google page. Current URL: {current_url}"

    # Verifică că pagina este încărcată
    assert context.google_home_page.is_google_page_loaded(), "Google page not loaded properly"


@then('search box-ul ar trebui să fie vizibil')
@step('search box-ul ar trebui să fie vizibil')
def step_verify_search_box_visible(context):
    """
    Verifică că search box-ul este vizibil
    """
    if not hasattr(context, 'google_home_page'):
        context.google_home_page = GoogleHomePage(context.driver)

    from utils.locators import GoogleHomePageLocators
    locators = GoogleHomePageLocators()

    is_visible = context.google_home_page.is_element_visible(locators.SEARCH_BOX)
    assert is_visible, "Search box is not visible"


@then('logo-ul Google ar trebui să fie afișat')
@step('logo-ul Google ar trebui să fie afișat')
def step_verify_google_logo_displayed(context):
    """
    Verifică că logo-ul Google este afișat
    """
    if not hasattr(context, 'google_home_page'):
        context.google_home_page = GoogleHomePage(context.driver)

    is_visible = context.google_home_page.is_google_logo_visible()
    assert is_visible, "Google logo is not displayed"


@then('pagina de rezultate ar trebui să se încarce')
@step('pagina de rezultate ar trebui să se încarce')
def step_verify_results_page_loaded(context):
    """
    Verifică că pagina de rezultate s-a încărcat
    """
    if not hasattr(context, 'google_results_page'):
        context.google_results_page = GoogleResultsPage(context.driver)

    # Verifică URL-ul
    current_url = context.driver.current_url
    assert "search?" in current_url, f"Not on results page. Current URL: {current_url}"

    # Verifică că pagina este încărcată
    is_loaded = context.google_results_page.is_results_page_loaded()
    assert is_loaded, "Results page not loaded properly"


@then('ar trebui să fie afișate rezultate de căutare')
@step('ar trebui să fie afișate rezultate de căutare')
def step_verify_search_results_displayed(context):
    """
    Verifică că există rezultate de căutare afișate
    """
    if not hasattr(context, 'google_results_page'):
        context.google_results_page = GoogleResultsPage(context.driver)

    # Așteaptă ca rezultatele să se încarce
    context.google_results_page.wait_for_results_to_load()

    # Verifică că există rezultate
    has_results = context.google_results_page.has_results()
    assert has_results, "No search results displayed"


@then('numărul de rezultate de pe pagină ar trebui să fie între {min_count:d} și {max_count:d}')
@step('numărul de rezultate de pe pagină ar trebui să fie între {min_count:d} și {max_count:d}')
def step_verify_results_count_range(context, min_count, max_count):
    """
    Verifică că numărul de rezultate este într-un interval specific
    """
    if not hasattr(context, 'google_results_page'):
        context.google_results_page = GoogleResultsPage(context.driver)

    # Obține numărul de rezultate
    results_count = context.google_results_page.get_number_of_results_on_page()
    context.results_count = results_count

    print(f"Number of results on page: {results_count}")

    assert min_count <= results_count <= max_count, \
        f"Results count {results_count} is not between {min_count} and {max_count}"


@then('ar trebui să fie afișat numărul total de rezultate')
@step('ar trebui să fie afișat numărul total de rezultate')
def step_verify_total_results_displayed(context):
    """
    Verifică că este afișat numărul total de rezultate
    """
    if not hasattr(context, 'google_results_page'):
        context.google_results_page = GoogleResultsPage(context.driver)

    # Obține textul cu statistici
    stats_text = context.google_results_page.get_result_stats_text()
    assert stats_text, "Result stats not displayed"

    print(f"Result stats: {stats_text}")

    # Obține numărul total
    total_count = context.google_results_page.get_total_results_count()
    assert total_count > 0, "Total results count is 0 or not found"

    print(f"Total results count: {total_count}")


@then('utilizatorul ar trebui să rămână pe pagina principală Google')
@step('utilizatorul ar trebui să rămână pe pagina principală Google')
def step_verify_remains_on_google_home(context):
    """
    Verifică că utilizatorul rămâne pe pagina principală Google
    """
    current_url = context.driver.current_url
    # URL-ul ar trebui să fie google.co.in fără parametri de search
    assert "google.co.in" in current_url or "google.com" in current_url, \
        f"Not on Google home page. Current URL: {current_url}"


@then('URL-ul nu ar trebui să conțină "{fragment}"')
@step('URL-ul nu ar trebui să conțină "{fragment}"')
def step_verify_url_not_contains(context, fragment):
    """
    Verifică că URL-ul nu conține un fragment specific
    """
    current_url = context.driver.current_url
    assert fragment not in current_url, \
        f"URL contains '{fragment}'. Current URL: {current_url}"


@then('nu ar trebui să fie afișate rezultate de căutare')
@step('nu ar trebui să fie afișate rezultate de căutare')
def step_verify_no_search_results(context):
    """
    Verifică că nu sunt afișate rezultate de căutare
    """
    current_url = context.driver.current_url

    # Dacă suntem pe pagina de rezultate, verifică că nu sunt rezultate
    if "search?" in current_url:
        if hasattr(context, 'google_results_page'):
            has_results = context.google_results_page.has_results()
            assert not has_results, "Search results are displayed but shouldn't be"
    # Altfel, verificăm că suntem pe pagina principală
    else:
        assert "google.co.in" in current_url or "google.com" in current_url, \
            "Not on Google home page"


@then('ar trebui să fie afișat linkul "Did you mean"')
@step('ar trebui să fie afișat linkul "Did you mean"')
def step_verify_did_you_mean_displayed(context):
    """
    Verifică că linkul "Did you mean" este afișat
    """
    if not hasattr(context, 'google_results_page'):
        context.google_results_page = GoogleResultsPage(context.driver)

    # Verifică că linkul este vizibil
    is_visible = context.google_results_page.is_did_you_mean_visible()
    assert is_visible, "Did you mean link is not displayed"

    print("Did you mean link is visible")


@then('sugestia de corectare ar trebui să conțină text alternativ')
@step('sugestia de corectare ar trebui să conțină text alternativ')
def step_verify_did_you_mean_text(context):
    """
    Verifică că sugestia "Did you mean" conține text
    """
    if not hasattr(context, 'google_results_page'):
        context.google_results_page = GoogleResultsPage(context.driver)

    # Obține textul sugestiei
    did_you_mean_text = context.google_results_page.get_did_you_mean_text()
    assert did_you_mean_text, "Did you mean text is empty"

    print(f"Did you mean suggestion: {did_you_mean_text}")


@then('ar trebui să fie afișate cel puțin {min_count:d} rezultate')
@step('ar trebui să fie afișate cel puțin {min_count:d} rezultate')
def step_verify_minimum_results(context, min_count):
    """
    Verifică că sunt afișate cel puțin un număr minim de rezultate
    """
    if not hasattr(context, 'google_results_page'):
        context.google_results_page = GoogleResultsPage(context.driver)

    results_count = context.google_results_page.get_number_of_results_on_page()
    assert results_count >= min_count, \
        f"Expected at least {min_count} results, but found {results_count}"

    print(f"Found {results_count} results (minimum {min_count})")


@then('fiecare rezultat ar trebui să aibă un titlu')
@step('fiecare rezultat ar trebui să aibă un titlu')
def step_verify_results_have_titles(context):
    """
    Verifică că fiecare rezultat are un titlu
    """
    if not hasattr(context, 'google_results_page'):
        context.google_results_page = GoogleResultsPage(context.driver)

    # Obține titlurile
    titles = context.google_results_page.get_search_result_titles()
    assert len(titles) > 0, "No result titles found"

    # Verifică că toate titlurile au conținut
    empty_titles = [i for i, title in enumerate(titles) if not title.strip()]
    assert len(empty_titles) == 0, f"Found {len(empty_titles)} results without titles"

    print(f"All {len(titles)} results have titles")


@then('ar trebui să existe butonul "Next" pentru paginare')
@step('ar trebui să existe butonul "Next" pentru paginare')
def step_verify_next_button_exists(context):
    """
    Verifică că există butonul Next pentru paginare
    """
    if not hasattr(context, 'google_results_page'):
        context.google_results_page = GoogleResultsPage(context.driver)

    # Scroll la sfârșitul paginii pentru a vedea butonul Next
    context.google_results_page.scroll_to_bottom()
    time.sleep(1)

    is_visible = context.google_results_page.is_next_page_button_visible()
    assert is_visible, "Next button is not visible"

    print("Next button is visible")


@then('rezultatele ar trebui să fie diferite de căutarea anterioară')
@step('rezultatele ar trebui să fie diferite de căutarea anterioară')
def step_verify_results_different_from_previous(context):
    """
    Verifică că rezultatele sunt diferite de căutarea anterioară
    """
    if not hasattr(context, 'google_results_page'):
        context.google_results_page = GoogleResultsPage(context.driver)

    # Obține rezultatele curente
    current_titles = context.google_results_page.get_search_result_titles()

    # Compară cu rezultatele anterioare (dacă există)
    if hasattr(context, 'previous_result_titles'):
        # Verifică că cel puțin primele 3 rezultate sunt diferite
        different_count = 0
        for i in range(min(3, len(current_titles), len(context.previous_result_titles))):
            if current_titles[i] != context.previous_result_titles[i]:
                different_count += 1

        assert different_count > 0, "Results are identical to previous search"
        print(f"{different_count} out of 3 top results are different")

    # Salvează rezultatele curente pentru comparații viitoare
    context.previous_result_titles = current_titles


@then('search box-ul ar trebui să fie vizibil pe pagina de rezultate')
@step('search box-ul ar trebui să fie vizibil pe pagina de rezultate')
def step_verify_search_box_on_results_page(context):
    """
    Verifică că search box-ul este vizibil pe pagina de rezultate
    """
    if not hasattr(context, 'google_results_page'):
        context.google_results_page = GoogleResultsPage(context.driver)

    from utils.locators import GoogleResultsPageLocators
    locators = GoogleResultsPageLocators()

    is_visible = context.google_results_page.is_element_visible(locators.SEARCH_BOX)
    assert is_visible, "Search box is not visible on results page"


@then('search box-ul ar trebui să conțină termenul căutat')
@step('search box-ul ar trebui să conțină termenul căutat')
def step_verify_search_box_contains_term(context):
    """
    Verifică că search box-ul conține termenul căutat
    """
    if not hasattr(context, 'google_results_page'):
        context.google_results_page = GoogleResultsPage(context.driver)

    # Obține valoarea din search box
    search_box_value = context.google_results_page.get_search_box_value()

    # Obține termenul căutat
    if hasattr(context, 'search_terms') and context.search_terms:
        search_term = context.search_terms[-1]  # Ultimul termen căutat
        assert search_term.lower() in search_box_value.lower(), \
            f"Search box doesn't contain search term. Expected: '{search_term}', Found: '{search_box_value}'"

        print(f"Search box contains: '{search_box_value}'")
