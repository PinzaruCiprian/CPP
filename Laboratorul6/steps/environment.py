"""
Environment file pentru Behave - setup și teardown
"""

from utils.driver_factory import WebDriverFactory


def before_all(context):
    """Se execută înainte de toate testele"""
    print("\n" + "="*60)
    print("INÍCIO - Testare BDD cu Behave și Selenium")
    print("="*60 + "\n")


def before_scenario(context, scenario):
    """Se execută înainte de fiecare scenariu"""
    print(f"\n▶ Scenariul: {scenario.name}")
    print("-" * 60)


def after_scenario(context, scenario):
    """Se execută după fiecare scenariu"""
    if scenario.status == "passed":
        print("✓ Scenariul a trecut cu succes")
    elif scenario.status == "failed":
        print("✗ Scenariul a eșuat")
    else:
        print(f"? Status: {scenario.status}")


def after_all(context):
    """Se execută după toate testele"""
    WebDriverFactory.close_driver()
    print("\n" + "="*60)
    print("FINAL - Testare completată")
    print("="*60 + "\n")
