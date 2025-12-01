#!/usr/bin/env python3
import subprocess
import sys

print("Running quick test for Mens page...")
result = subprocess.run(
    [sys.executable, "run_tests.py", "--mens"],
    cwd="c:\\Users\\ciprian.panzaru\\Desktop\\UTM\\Semestrul VII\\CPP\\CPP\\Laboratorul6",
    capture_output=True,
    text=True,
    timeout=120
)

print("STDOUT:")
print(result.stdout)
print("\nSTDERR:")
print(result.stderr)
print(f"\nReturn code: {result.returncode}")

# Save to file
with open("quick_test_results.txt", "w", encoding="utf-8", errors="replace") as f:
    f.write("STDOUT:\n")
    f.write(result.stdout)
    f.write("\n\nSTDERR:\n")
    f.write(result.stderr)
    f.write(f"\n\nReturn code: {result.returncode}")

print("\nResults saved to quick_test_results.txt")
