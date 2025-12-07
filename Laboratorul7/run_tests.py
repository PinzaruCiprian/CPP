"""
Script pentru rularea testelor Behave și generarea raportului HTML.
"""
import os
import sys
import subprocess
from datetime import datetime

# Set UTF-8 encoding for Windows console to handle Romanian characters
if sys.platform == 'win32':
    os.environ['PYTHONIOENCODING'] = 'utf-8'
    # Force UTF-8 encoding for stdout/stderr
    if sys.stdout.encoding != 'utf-8':
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    if sys.stderr.encoding != 'utf-8':
        import codecs
        sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')


def run_behave_tests():
    """
    Rulează testele Behave cu raportare HTML
    """
    print("="*80)
    print("GOOGLE SEARCH AUTOMATION - LABORATORUL 7")
    print("="*80)
    print(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80 + "\n")

    # Creează directoare pentru rapoarte
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

    # Definește calea pentru rapoarte
    json_report = "reports/behave-report.json"

    # Construiește comanda Behave (fără HTML formatter care nu este disponibil)
    behave_cmd = [
        "behave",
        "features/",
        "--format", "json",
        "--outfile", json_report,
        "--format", "pretty",  # Console output
        "--no-capture",  # Don't capture stdout
        "--no-capture-stderr",  # Don't capture stderr
    ]

    print("Running Behave tests...")
    print(f"Command: {' '.join(behave_cmd)}\n")

    try:
        # Setează encoding pentru subprocess
        env = os.environ.copy()
        env['PYTHONIOENCODING'] = 'utf-8'

        # Rulează Behave
        result = subprocess.run(
            behave_cmd,
            cwd=os.getcwd(),
            capture_output=False,
            text=True,
            env=env
        )

        print("\n" + "="*80)
        print("TEST EXECUTION COMPLETED")
        print("="*80)

        # Verifică dacă raportul JSON a fost generat
        if os.path.exists(json_report):
            print(f"\n[OK] JSON Report generated: {json_report}")
        else:
            print(f"\n[X] JSON Report not found at: {json_report}")

        # Verifică dacă raportul text a fost generat
        text_report = "reports/test_summary.txt"
        if os.path.exists(text_report):
            print(f"[OK] Text Summary generated: {text_report}")
        else:
            print(f"[X] Text Summary not found at: {text_report}")

        # Verifică screenshots
        screenshots_dir = "reports/screenshots"
        if os.path.exists(screenshots_dir):
            screenshots = [f for f in os.listdir(screenshots_dir) if f.endswith('.png')]
            print(f"[OK] Screenshots captured: {len(screenshots)} files in {screenshots_dir}/")
        else:
            print(f"[X] Screenshots directory not found: {screenshots_dir}")

        print("\n" + "="*80)
        print(f"End Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*80 + "\n")

        # Return code
        return result.returncode

    except FileNotFoundError:
        print("\n[ERROR] Behave is not installed or not found in PATH")
        print("        Install with: pip install -r requirements.txt")
        return 1
    except Exception as e:
        print(f"\n[ERROR] running tests: {e}")
        return 1


def generate_custom_html_report():
    """
    Generează un raport HTML customizat cu statistici și screenshots
    """
    print("\nGenerating custom HTML report...")

    try:
        # Citește raportul text pentru informații
        text_report_path = "reports/test_summary.txt"
        if not os.path.exists(text_report_path):
            print("[X] Text summary not found, skipping custom HTML report")
            return

        with open(text_report_path, 'r', encoding='utf-8') as f:
            summary_content = f.read()

        # Găsește toate screenshot-urile
        screenshots_dir = "reports/screenshots"
        screenshots = []
        if os.path.exists(screenshots_dir):
            screenshots = sorted([
                f for f in os.listdir(screenshots_dir)
                if f.endswith('.png')
            ])

        # Generează HTML
        html_content = f"""<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Google Search Automation - Test Report</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            line-height: 1.6;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        .header p {{
            font-size: 1.2em;
            opacity: 0.9;
        }}
        .content {{
            padding: 30px;
        }}
        .summary-box {{
            background: #f8f9fa;
            border-left: 5px solid #667eea;
            padding: 20px;
            margin-bottom: 30px;
            border-radius: 5px;
        }}
        .summary-box h2 {{
            color: #667eea;
            margin-bottom: 15px;
        }}
        .summary-box pre {{
            background: white;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            font-size: 0.9em;
            border: 1px solid #dee2e6;
        }}
        .screenshots-section {{
            margin-top: 30px;
        }}
        .screenshots-section h2 {{
            color: #667eea;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #667eea;
        }}
        .screenshots-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }}
        .screenshot-item {{
            background: #f8f9fa;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        .screenshot-item:hover {{
            transform: translateY(-5px);
            box-shadow: 0 5px 20px rgba(0,0,0,0.2);
        }}
        .screenshot-item img {{
            width: 100%;
            height: 200px;
            object-fit: cover;
            cursor: pointer;
        }}
        .screenshot-item .caption {{
            padding: 15px;
            background: white;
            font-size: 0.85em;
            color: #495057;
            word-break: break-all;
        }}
        .footer {{
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            color: #6c757d;
            border-top: 1px solid #dee2e6;
        }}
        .badge {{
            display: inline-block;
            padding: 5px 10px;
            border-radius: 3px;
            font-size: 0.9em;
            font-weight: bold;
        }}
        .badge-success {{
            background: #28a745;
            color: white;
        }}
        .badge-danger {{
            background: #dc3545;
            color: white;
        }}
        .no-screenshots {{
            text-align: center;
            padding: 40px;
            color: #6c757d;
            font-style: italic;
        }}
        /* Modal pentru imagini */
        .modal {{
            display: none;
            position: fixed;
            z-index: 1000;
            padding-top: 50px;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            overflow: auto;
            background-color: rgba(0,0,0,0.9);
        }}
        .modal-content {{
            margin: auto;
            display: block;
            max-width: 90%;
            max-height: 90%;
        }}
        .close {{
            position: absolute;
            top: 15px;
            right: 35px;
            color: #f1f1f1;
            font-size: 40px;
            font-weight: bold;
            cursor: pointer;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔍 Google Search Automation</h1>
            <p>Laboratorul 7 - Test Report</p>
            <p>{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </div>

        <div class="content">
            <div class="summary-box">
                <h2>📊 Test Execution Summary</h2>
                <pre>{summary_content}</pre>
            </div>

            <div class="screenshots-section">
                <h2>📸 Screenshots ({len(screenshots)})</h2>
"""

        if screenshots:
            html_content += '                <div class="screenshots-grid">\n'
            for screenshot in screenshots:
                screenshot_path = f"screenshots/{screenshot}"
                html_content += f"""                    <div class="screenshot-item">
                        <img src="{screenshot_path}" alt="{screenshot}" onclick="openModal(this.src)">
                        <div class="caption">{screenshot}</div>
                    </div>
"""
            html_content += '                </div>\n'
        else:
            html_content += '                <div class="no-screenshots">Nu există screenshots capturate</div>\n'

        html_content += """            </div>
        </div>

        <div class="footer">
            <p>Generated by Behave (Cucumber BDD) | Laboratorul 7 - CPP | UTM</p>
        </div>
    </div>

    <!-- Modal pentru vizualizare imagini -->
    <div id="imageModal" class="modal" onclick="closeModal()">
        <span class="close">&times;</span>
        <img class="modal-content" id="modalImg">
    </div>

    <script>
        function openModal(src) {
            document.getElementById('imageModal').style.display = 'block';
            document.getElementById('modalImg').src = src;
        }

        function closeModal() {
            document.getElementById('imageModal').style.display = 'none';
        }

        // Close modal cu ESC
        document.addEventListener('keydown', function(event) {
            if (event.key === 'Escape') {
                closeModal();
            }
        });
    </script>
</body>
</html>
"""

        # Salvează raportul HTML customizat
        custom_report_path = "reports/test-report-custom.html"
        with open(custom_report_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"[OK] Custom HTML report generated: {custom_report_path}")
        print(f"     Open in browser: file://{os.path.abspath(custom_report_path)}")

    except Exception as e:
        print(f"[ERROR] Error generating custom HTML report: {e}")


def open_html_report_in_browser():
    """
    Deschide automat raportul HTML în browser-ul implicit
    """
    import webbrowser

    custom_report_path = "reports/test-report-custom.html"

    if os.path.exists(custom_report_path):
        abs_path = os.path.abspath(custom_report_path)
        print(f"\n[INFO] Opening HTML report in default browser...")
        print(f"       {abs_path}")

        try:
            # Deschide raportul în browser-ul implicit
            webbrowser.open(f'file://{abs_path}')
            print("[OK] Browser opened successfully!")
        except Exception as e:
            print(f"[WARNING] Could not open browser automatically: {e}")
            print(f"[INFO] Please open manually: {abs_path}")
    else:
        print(f"[WARNING] HTML report not found: {custom_report_path}")


if __name__ == "__main__":
    # Rulează testele
    exit_code = run_behave_tests()

    # Generează raport HTML customizat
    generate_custom_html_report()

    # Deschide automat raportul HTML în browser
    open_html_report_in_browser()

    # Exit cu codul de returnare al Behave
    sys.exit(exit_code)
