"""
Script pentru verificarea step-urilor definite vs. cele necesare
"""
import os
import sys

# Set UTF-8 encoding
if sys.platform == 'win32':
    os.environ['PYTHONIOENCODING'] = 'utf-8'
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Citește feature file și extrage step-urile
feature_file = 'features/google_search.feature'
steps_needed = set()

with open(feature_file, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        # Verifică liniile care încep cu Dat fiind, Când, Atunci, Și
        if line.startswith(('Dat fiind ', 'Când ', 'Atunci ', 'Și ')):
            # Elimină tag-ul de step
            for prefix in ['Dat fiind ', 'Când ', 'Atunci ', 'Și ']:
                if line.startswith(prefix):
                    step_text = line[len(prefix):]
                    steps_needed.add(step_text)
                    print(f"Step necesar: {step_text}")

print(f"\nTotal step-uri unice necesare: {len(steps_needed)}")
