"""
Script simplu pentru a testa dacă Chrome și ChromeDriver funcționează
"""
import sys
print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    print("\n[OK] Selenium imported successfully")
    print(f"Selenium version: {webdriver.__version__}")
except Exception as e:
    print(f"\n[ERROR] Failed to import Selenium: {e}")
    sys.exit(1)

# Test 1: ChromeDriver manual path
print("\n" + "="*60)
print("TEST 1: Manual ChromeDriver path")
print("="*60)

chromedriver_path = "C:/chromedriver/chromedriver-win64/chromedriver.exe"
print(f"Trying: {chromedriver_path}")

try:
    import os
    if os.path.exists(chromedriver_path):
        print(f"[OK] File exists: {chromedriver_path}")
        file_size = os.path.getsize(chromedriver_path)
        print(f"[OK] File size: {file_size:,} bytes")
    else:
        print(f"[ERROR] File not found: {chromedriver_path}")
        sys.exit(1)

    # Create service
    service = Service(chromedriver_path)
    print("[OK] Service created")

    # Create Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    print("[OK] Chrome options configured")

    # Try to create driver
    print("\n[INFO] Attempting to create Chrome driver...")
    print("[INFO] This should open Chrome browser...")

    driver = webdriver.Chrome(service=service, options=options)
    print("[OK] Chrome driver created successfully!")
    print("[OK] Chrome browser should be open now!")

    # Navigate to Google
    print("\n[INFO] Navigating to Google...")
    driver.get("https://www.google.com")
    print(f"[OK] Current URL: {driver.current_url}")
    print(f"[OK] Page title: {driver.title}")

    # Close
    input("\nPress Enter to close the browser...")
    driver.quit()
    print("[OK] Browser closed")
    print("\n" + "="*60)
    print("SUCCESS! Everything works!")
    print("="*60)

except Exception as e:
    print(f"\n[ERROR] Failed: {e}")
    print(f"[ERROR] Error type: {type(e).__name__}")
    import traceback
    print("\nFull traceback:")
    traceback.print_exc()
    sys.exit(1)
