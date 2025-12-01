"""
Fixed test runner that works with UTF-8 output and Windows PowerShell
"""

import os
import sys
import subprocess
from pathlib import Path

# Get the current directory
project_root = Path(__file__).parent

def run_behave_with_json(feature_file=None, tags=None, output_file='test_output.json'):
    """Run behave and output to JSON file"""
    
    argv = []
    
    if feature_file:
        argv.append(str(feature_file))
    else:
        argv.append('features')
    
    argv.extend(['--no-capture', '--format', 'json', '--outfile', output_file])
    
    if tags:
        argv.extend(['--tags', tags])
    
    # Change to project root
    original_cwd = os.getcwd()
    os.chdir(project_root)
    
    try:
        # Import and run behave
        from behave.__main__ import main as behave_main
        return behave_main(argv)
    finally:
        os.chdir(original_cwd)


def display_json_results(json_file='test_output.json'):
    """Display test results from JSON file"""
    if not os.path.exists(json_file):
        return
    
    print("\n" + "="*70)
    print("TEST RESULTS:")
    print("="*70)
    
    import json
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            for feature in data:
                print(f"\nFeature: {feature.get('name', 'N/A')}")
                for scenario in feature.get('elements', []):
                    steps = scenario.get('steps', [])
                    if steps:
                        status = 'PASSED' if all(s.get('result', {}).get('status') == 'passed' for s in steps) else 'FAILED'
                    else:
                        status = 'SKIPPED'
                    print(f"  Scenario: {scenario.get('name', 'N/A')} - {status}")
                    for step in steps:
                        result = step.get('result', {})
                        status_str = result.get('status', 'unknown').upper()
                        print(f"    {step.get('keyword', '').strip()} {step.get('name', 'N/A')} - {status_str}")
                        if result.get('error_message'):
                            print(f"      Error: {result['error_message'][:100]}")
    except Exception as e:
        print(f"Error reading JSON output: {e}")
        with open(json_file, 'r', encoding='utf-8') as f:
            print(f.read()[:500])


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == '--mens':
            print("\n" + "="*70)
            print("RUNNING MENS PAGE TESTS (TC1-TC6)")
            print("="*70 + "\n")
            result = run_behave_with_json('features/05_mens_page.feature')
            display_json_results()
            return result
        elif sys.argv[1] == '--passed':
            print("\n" + "="*70)
            print("RUNNING PASSED TESTS (TC1, TC2, TC3, TC5)")
            print("="*70 + "\n")
            result = run_behave_with_json('features/05_mens_page.feature', '~@failed')
            display_json_results()
            return result
        elif sys.argv[1] == '--failed':
            print("\n" + "="*70)
            print("RUNNING FAILED TESTS (TC4, TC6)")
            print("="*70 + "\n")
            result = run_behave_with_json('features/05_mens_page.feature', '@failed')
            display_json_results()
            return result
        else:
            print("Usage:")
            print("  python run_tests_fixed.py --mens     # Run all Mens page tests")
            print("  python run_tests_fixed.py --passed   # Run passed tests only")
            print("  python run_tests_fixed.py --failed   # Run failed tests only")
            return 1
    else:
        print("\n" + "="*70)
        print("RUNNING ALL TESTS")
        print("="*70 + "\n")
        result = run_behave_with_json()
        display_json_results()
        return result


if __name__ == '__main__':
    sys.exit(main())
