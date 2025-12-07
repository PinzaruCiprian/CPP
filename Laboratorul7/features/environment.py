"""
Environment file pentru Behave - conține hooks pentru setup și teardown.
Gestionează browser-ul, capturi de ecran și rapoarte HTML.
"""
import os
import sys
from datetime import datetime

# Adaugă directorul rădăcină la Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from utils.driver_factory import DriverFactory, DriverConfig
from utils.helpers import ScreenshotHelpers


def before_all(context):
    """
    Rulează o singură dată înainte de toate testele
    """
    print("\n" + "="*80)
    print("Starting Test Execution - Google Search Automation")
    print("="*80 + "\n")

    # Creează directoare pentru rapoarte și screenshots
    os.makedirs("reports", exist_ok=True)
    screenshots_dir = "reports/screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)

    # Șterge screenshot-urile vechi
    if os.path.exists(screenshots_dir):
        old_screenshots = [f for f in os.listdir(screenshots_dir) if f.endswith('.png')]
        if old_screenshots:
            print(f"[INFO] Cleaning up {len(old_screenshots)} old screenshot(s)...")
            for screenshot in old_screenshots:
                try:
                    os.remove(os.path.join(screenshots_dir, screenshot))
                except Exception as e:
                    print(f"[WARNING] Could not delete {screenshot}: {e}")
            print("[OK] Old screenshots deleted\n")

    # Inițializează liste pentru tracking
    context.screenshots = []
    context.failed_scenarios = []
    context.passed_scenarios = []

    # Configurare
    context.config.setup_logging()


def before_feature(context, feature):
    """
    Rulează înainte de fiecare feature
    """
    print(f"\n{'='*80}")
    print(f"Feature: {feature.name}")
    print(f"{'='*80}\n")


def before_scenario(context, scenario):
    """
    Rulează înainte de fiecare scenario
    Inițializează browser-ul Chrome
    """
    print(f"\n{'-'*80}")
    print(f"Scenario: {scenario.name}")
    print(f"{'-'*80}")

    # Inițializează Chrome WebDriver
    try:
        context.driver = DriverConfig.get_driver()
        print("[OK] Chrome browser initialized successfully")
    except Exception as e:
        print(f"[ERROR] Failed to initialize Chrome browser: {e}")
        raise

    # Salvează informații despre scenario
    context.scenario_name = scenario.name
    context.scenario_start_time = datetime.now()


def after_step(context, step):
    """
    Rulează după fiecare step
    """
    if step.status == "failed":
        print(f"[X] Step FAILED: {step.name}")

        # Ia screenshot la failure
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            # Sanitizează numele scenario-ului pentru nume fișier
            safe_scenario_name = "".join(
                c if c.isalnum() or c in (' ', '_', '-') else '_'
                for c in context.scenario_name
            ).strip()
            screenshot_name = f"FAILED_{safe_scenario_name}_{timestamp}"

            filepath = ScreenshotHelpers.take_screenshot(
                context.driver,
                screenshot_name,
                directory="reports/screenshots"
            )

            if filepath:
                context.screenshots.append(filepath)
                print(f"[OK] Screenshot saved: {filepath}")

                # Atașează screenshot la raport (pentru behave-html-formatter)
                if hasattr(context, 'embed'):
                    with open(filepath, 'rb') as f:
                        context.embed('image/png', f.read(), caption=screenshot_name)
        except Exception as e:
            print(f"[ERROR] Failed to take screenshot: {e}")
    else:
        print(f"[OK] Step PASSED: {step.name}")


def after_scenario(context, scenario):
    """
    Rulează după fiecare scenario
    Închide browser-ul și salvează rezultatele
    """
    # Calculează durata
    if hasattr(context, 'scenario_start_time'):
        duration = datetime.now() - context.scenario_start_time
        duration_str = f"{duration.total_seconds():.2f}s"
    else:
        duration_str = "N/A"

    # Ia screenshot ÎNTOTDEAUNA (indiferent de status)
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_scenario_name = "".join(
            c if c.isalnum() or c in (' ', '_', '-') else '_'
            for c in context.scenario_name
        ).strip()

        # Prefix diferit pentru passed/failed
        if scenario.status == "failed":
            screenshot_name = f"FAILED_{safe_scenario_name}_{timestamp}"
        else:
            screenshot_name = f"PASSED_{safe_scenario_name}_{timestamp}"

        filepath = ScreenshotHelpers.take_screenshot(
            context.driver,
            screenshot_name,
            directory="reports/screenshots"
        )

        if filepath:
            context.screenshots.append(filepath)
            print(f"[OK] Screenshot saved: {filepath}")
    except Exception as e:
        print(f"[ERROR] Failed to take screenshot: {e}")

    # Verifică status și adaugă la lista corespunzătoare
    if scenario.status == "failed":
        print(f"\n[X] Scenario FAILED: {scenario.name} (Duration: {duration_str})")
        context.failed_scenarios.append({
            'name': scenario.name,
            'duration': duration_str,
            'feature': scenario.feature.name
        })
    else:
        print(f"\n[OK] Scenario PASSED: {scenario.name} (Duration: {duration_str})")
        context.passed_scenarios.append({
            'name': scenario.name,
            'duration': duration_str,
            'feature': scenario.feature.name
        })

    # Închide browser-ul
    try:
        if hasattr(context, 'driver') and context.driver:
            DriverFactory.quit_driver(context.driver)
            print("[OK] Chrome browser closed")
    except Exception as e:
        print(f"[ERROR] Error closing browser: {e}")

    print(f"{'-'*80}\n")


def after_feature(context, feature):
    """
    Rulează după fiecare feature
    """
    print(f"\n{'='*80}")
    print(f"Feature Completed: {feature.name}")
    print(f"{'='*80}\n")


def after_all(context):
    """
    Rulează o singură dată după toate testele
    Generează raportul final
    """
    print("\n" + "="*80)
    print("Test Execution Completed")
    print("="*80)

    # Calculează statistici
    total_scenarios = len(context.passed_scenarios) + len(context.failed_scenarios)
    passed_count = len(context.passed_scenarios)
    failed_count = len(context.failed_scenarios)
    success_rate = (passed_count / total_scenarios * 100) if total_scenarios > 0 else 0

    # Afișează rezumatul
    print(f"\n{'='*80}")
    print("TEST EXECUTION SUMMARY")
    print(f"{'='*80}")
    print(f"Total Scenarios:  {total_scenarios}")
    print(f"Passed:           {passed_count}")
    print(f"Failed:           {failed_count}")
    print(f"Success Rate:     {success_rate:.2f}%")
    print(f"Screenshots:      {len(context.screenshots)}")
    print(f"{'='*80}\n")

    # Afișează scenarii failed
    if context.failed_scenarios:
        print("FAILED SCENARIOS:")
        print("-"*80)
        for scenario in context.failed_scenarios:
            print(f"  [X] {scenario['feature']} - {scenario['name']} ({scenario['duration']})")
        print()

    # Generează raport text
    generate_text_report(context, total_scenarios, passed_count, failed_count, success_rate)

    print(f"\n{'='*80}")
    print("Reports generated in 'reports/' directory")
    print(f"{'='*80}\n")


def generate_text_report(context, total, passed, failed, success_rate):
    """
    Generează un raport text cu rezultatele
    """
    try:
        report_path = "reports/test_summary.txt"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("="*80 + "\n")
            f.write("GOOGLE SEARCH AUTOMATION - TEST EXECUTION SUMMARY\n")
            f.write("="*80 + "\n\n")

            f.write(f"Execution Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Browser: Chrome\n")
            f.write(f"Framework: Behave (Cucumber BDD for Python)\n\n")

            f.write("="*80 + "\n")
            f.write("STATISTICS\n")
            f.write("="*80 + "\n")
            f.write(f"Total Scenarios:  {total}\n")
            f.write(f"Passed:           {passed}\n")
            f.write(f"Failed:           {failed}\n")
            f.write(f"Success Rate:     {success_rate:.2f}%\n")
            f.write(f"Screenshots:      {len(context.screenshots)}\n\n")

            # Passed scenarios
            if context.passed_scenarios:
                f.write("="*80 + "\n")
                f.write("PASSED SCENARIOS\n")
                f.write("="*80 + "\n")
                for scenario in context.passed_scenarios:
                    f.write(f"[OK] {scenario['feature']} - {scenario['name']} ({scenario['duration']})\n")
                f.write("\n")

            # Failed scenarios
            if context.failed_scenarios:
                f.write("="*80 + "\n")
                f.write("FAILED SCENARIOS\n")
                f.write("="*80 + "\n")
                for scenario in context.failed_scenarios:
                    f.write(f"[X] {scenario['feature']} - {scenario['name']} ({scenario['duration']})\n")
                f.write("\n")

            # Screenshots
            if context.screenshots:
                f.write("="*80 + "\n")
                f.write("SCREENSHOTS\n")
                f.write("="*80 + "\n")
                for screenshot in context.screenshots:
                    f.write(f"  - {screenshot}\n")
                f.write("\n")

            f.write("="*80 + "\n")
            f.write("END OF REPORT\n")
            f.write("="*80 + "\n")

        print(f"[OK] Text report generated: {report_path}")
    except Exception as e:
        print(f"[ERROR] Failed to generate text report: {e}")
