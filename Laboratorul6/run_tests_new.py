"""
Main test runner - executa testele BDD cu Behave
Utilizeaza Chrome WebDriver pentru testare
Handles UTF-8 encoding for Windows PowerShell
"""

import os
import sys
import json
from pathlib import Path

# Set UTF-8 encoding for Windows PowerShell compatibility
os.environ['PYTHONIOENCODING'] = 'utf-8'
if sys.stdout.encoding is None or sys.stdout.encoding.lower() != 'utf-8':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Adauga directoarele proiectului la path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / 'pages'))
sys.path.insert(0, str(project_root / 'utils'))
sys.path.insert(0, str(project_root / 'steps'))

from behave.__main__ import main as behave_main


def run_behave_with_json(feature_file=None, tags=None, output_file='test_output.json'):
    """Run behave and output to JSON file"""
    
    argv = []
    
    if feature_file:
        argv.append(str(feature_file))
    else:
        argv.append('features')
    
    # Use JSON formatter with no other formatters
    argv.extend(['--no-capture', '--format', 'json', '--outfile', output_file])
    
    # Suppress stdout to avoid encoding issues
    argv.append('--quiet')
    
    if tags:
        argv.extend(['--tags', tags])
    
    return behave_main(argv)


def display_json_results(json_file='test_output.json'):
    """Display test results from JSON file"""
    if not os.path.exists(json_file):
        return
    
    print("\n" + "="*70)
    print("TEST RESULTS:")
    print("="*70)
    
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            # If data is a list, it's a newer Behave format
            if isinstance(data, list):
                features = data
            else:
                features = [data] if isinstance(data, dict) else []
            
            total_scenarios = 0
            passed_scenarios = 0
            
            for feature in features:
                feature_name = feature.get('name', 'N/A')
                if feature_name:
                    print(f"\nFeature: {feature_name}")
                
                for scenario in feature.get('elements', []):
                    # Skip background scenarios (type='background')
                    if scenario.get('type') == 'background':
                        continue
                    
                    total_scenarios += 1
                    scenario_name = scenario.get('name', 'N/A')
                    steps = scenario.get('steps', [])
                    
                    if steps:
                        failed_steps = [s for s in steps if s.get('result', {}).get('status') != 'passed']
                        status = 'FAILED' if failed_steps else 'PASSED'
                        if status == 'PASSED':
                            passed_scenarios += 1
                    else:
                        status = 'SKIPPED'
                    
                    print(f"  Scenario: {scenario_name} - {status}")
                    for step in steps:
                        result = step.get('result', {})
                        status_str = result.get('status', 'unknown').upper()
                        print(f"    {step.get('keyword', '').strip()} {step.get('name', 'N/A')} - {status_str}")
                        if result.get('error_message'):
                            error_msg = str(result['error_message'])
                            if isinstance(error_msg, list):
                                error_msg = ' '.join(error_msg)
                            error_msg = error_msg.replace('\n', ' ')[:80]
                            print(f"      Error: {error_msg}")
            
            if total_scenarios > 0:
                print(f"\n{'='*70}")
                print(f"SUMMARY: {passed_scenarios}/{total_scenarios} scenarios passed")
                print(f"{'='*70}")
    except Exception as e:
        import traceback
        print(f"Error reading JSON output: {e}")
        traceback.print_exc()
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                content = f.read()[:500]
                print(f"File content preview: {content}")
        except:
            pass


def run_all_tests():
    """Executa toate testele BDD"""
    print("\n" + "="*70)
    print("ELITE SHOPPY - TESTE AUTOMATIZARE BDD CU CUCUMBER (Behave)")
    print("="*70 + "\n")
    
    result = run_behave_with_json()
    display_json_results()
    return result


def run_specific_feature(feature_name):
    """Executa un anumit feature"""
    print("\n" + "="*70)
    print(f"EXECUTA FEATURE: {feature_name}")
    print("="*70 + "\n")
    
    result = run_behave_with_json(f'features/{feature_name}.feature')
    display_json_results()
    return result


def run_tests_with_tags(tags):
    """Executa teste cu anumite tag-uri"""
    print("\n" + "="*70)
    print(f"EXECUTA TESTE CU TAG-URILE: {tags}")
    print("="*70 + "\n")
    
    result = run_behave_with_json(tags=tags)
    display_json_results()
    return result


def run_failed_tests():
    """Executa doar testele marcate ca failed (TC4, TC6)"""
    print("\n" + "="*70)
    print("EXECUTA TESTELE ESUITE (TC4, TC6)")
    print("="*70 + "\n")
    
    result = run_behave_with_json('features/05_mens_page.feature', '@failed')
    display_json_results()
    return result


def run_passed_tests():
    """Executa doar testele marcate ca passed (TC1, TC2, TC3, TC5)"""
    print("\n" + "="*70)
    print("EXECUTA TESTELE REUSUITE (TC1, TC2, TC3, TC5)")
    print("="*70 + "\n")
    
    result = run_behave_with_json('features/05_mens_page.feature', '~@failed')
    display_json_results()
    return result


def run_mens_page_tests():
    """Executa toate testele paginii Mens (TC1-TC6)"""
    print("\n" + "="*70)
    print("EXECUTA TESTELE PAGINII MENS (TC1-TC6)")
    print("="*70 + "\n")
    
    result = run_specific_feature("05_mens_page")
    return result


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '--feature' and len(sys.argv) > 2:
            result = run_specific_feature(sys.argv[2])
        elif sys.argv[1] == '--tags' and len(sys.argv) > 2:
            result = run_tests_with_tags(sys.argv[2])
        elif sys.argv[1] == '--failed':
            result = run_failed_tests()
        elif sys.argv[1] == '--passed':
            result = run_passed_tests()
        elif sys.argv[1] == '--mens':
            result = run_mens_page_tests()
        else:
            result = run_all_tests()
    else:
        result = run_all_tests()
    
    sys.exit(result)
