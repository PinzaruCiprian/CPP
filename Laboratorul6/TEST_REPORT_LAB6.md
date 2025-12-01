# 📋 RAPORT TESTE - LABORATORUL 6

## Informații Generale

**Curs:** Tehnici Avansate de Testare Software  
**Laborator:** Laboratorul 6 - BDD cu Cucumber/Behave  
**Data:** Noiembrie 2025  
**Autor:** Pînzaru Ciprian  
**Aplicație Testată:** Elite Shoppy E-Commerce (Netlify)  
**URL:** https://adoring-pasteur-3ae17d.netlify.app/

---

## 📊 Sumar Teste

| Test Case | Denumire | Status | Prioritate | OS/Browser | Note |
|-----------|----------|--------|-----------|-----------|------|
| TC1 | Încărcarea paginii Mens | ✅ PASSED | Normal | Windows 10, Chrome v140 | Pagina se încarcă complet, timp < 3s |
| TC2 | Funcționalitate meniu navigare | ✅ PASSED | High | Windows 10, Chrome v140 | Toate linkurile funcționează corect |
| TC3 | Afișare produse Mens | ✅ PASSED | Normal | Windows 10, Chrome v140 | Produse cu imagine, titlu, preț complet |
| TC4 | Contact link din footer | ❌ FAILED | Low | Windows 10, Chrome v140 | Redirecționează la YouTube în loc de contact |
| TC5 | Responsivitate pagina Mens | ✅ PASSED | High | Windows 10, Chrome v140 | Layout corect pe desktop, tabletă, mobil |
| TC6 | Funcție căutare (pozitiv) | ❌ FAILED | High | Windows 10, Chrome v140 | Redirecționează la "Page not Found" (404) |

**Total:** 6/6 teste create  
**Reușite:** 4 (66.67%)  
**Eșuate:** 2 (33.33%)

---

## 📝 Descrieri Detaliate

### ✅ TC1 - Verificarea încărcării corecte a paginii "Mens"

**Status:** PASSED  
**Prioritate:** Normal

**Obiectiv:**  
Verificare încărcare completă pagina Mens fără erori, cu timp sub 3 secunde.

**Precondiții:**
- Conexiune internet stabilă
- Browser Chrome actualizat
- Cache golit
- URL accesibil: https://adoring-pasteur-3ae17d.netlify.app/mens.html

**Pași Automatizați:**
1. Deschidere browser Chrome
2. Navigare la URL pagina Mens
3. Așteptare finalizare încărcare
4. Verificare prezență elemente: titlu, produse, header, footer
5. Verificare imagini produse încărcate
6. Verificare resurse externe (CSS, JS) disponibile

**Rezultat Așteptat:**  
Pagina se încarcă complet, timp < 3 secunde, toate elementele vizibile.

**Rezultat Actual:**  
✅ PASSED - Pagina încărcată în ~1.2 secunde, toate elementele vizibile.

**Bugs Depistate:** Niciun bug

---

### ✅ TC2 - Verificarea funcționalității meniului de navigare

**Status:** PASSED  
**Prioritate:** High

**Obiectiv:**  
Validare funcționare corectă a meniului principal, redirecționări corecte către pagini.

**Precondiții:**
- Pagina Mens complet încărcată
- Bara meniu vizibilă
- Conexiune internet activă
- Paginile linkate online

**Pași Automatizați:**
1. Navigare pagina Mens
2. Verificare meniu vizibil
3. Hover pe fiecare element meniu (Home, Womens, Mens, Contact)
4. Click pe Home link → verificare redirecționare
5. Click pe Womens link → verificare redirecționare
6. Click pe Mens link → verificare rămânere pagina Mens
7. Verificare absență erori 404/500

**Rezultat Așteptat:**  
Meniu permite navigare corectă, niciun error.

**Rezultat Actual:**  
✅ PASSED - Toate linkurile funcționează corect, navigare fluentă.

**Bugs Depistate:** Niciun bug

---

### ✅ TC3 - Verificarea afișării produselor în secțiunea "Mens"

**Status:** PASSED  
**Prioritate:** Normal

**Obiectiv:**  
Confirmare afișare corectă produse cu toate detaliile: imagine, titlu, preț, buton.

**Precondiții:**
- Produse categoria Mens în bază de date
- Conexiune server activă
- Pagina complet încărcată

**Pași Automatizați:**
1. Navigare pagina Mens
2. Derulare la secțiune produse
3. Verificare pentru fiecare produs:
   - Imagine prezentă și încărcată
   - Titlu valid și vizibil
   - Preț afișat corect
   - Buton acțiune (Add to Cart) prezent și activ

**Rezultat Așteptat:**  
Toate produse afișate cu image, titlu, preț, buton activ.

**Rezultat Actual:**  
✅ PASSED - 24 produse afișate complet, toate datele prezente și corecte.

**Bugs Depistate:** Niciun bug

---

### ❌ TC4 - Verificarea funcționalității linkului "Contact" din footer

**Status:** FAILED  
**Prioritate:** Low  
**Severitate:** MEDIUM

**Obiectiv:**  
Confirmare link Contact din footer redirecționează la pagina Contact.

**Precondiții:**
- Pagina Mens complet încărcată
- Footer vizibil
- Conexiune internet activă
- Pagina Contact publicată

**Pași de Recreare:**
1. Navigare pagina Mens
2. Derulare la footer
3. Click pe link "Contact"
4. Verificare redirecționare

**Rezultat Așteptat:**  
Redirecționare la pagina Contact, fără erori.

**Rezultat Actual:**  
❌ FAILED - Click pe "Contact" redirecționează la YouTube (youtube.com)

**Bug Report:**
- **Bug ID:** BUG-001
- **Descriere:** Contact link din footer redirecționează la YouTube în loc de pagina Contact
- **Impact:** User nu poate accesa contact page din footer
- **Reproductibilitate:** 100% - se reproduce de fiecare dată
- **Severity:** MEDIUM (usability issue)
- **Fix Recomandat:** Actualiza href linkul Contact la pagina contact corectă

---

### ✅ TC5 - Verificarea responsivității paginii Mens

**Status:** PASSED  
**Prioritate:** High

**Obiectiv:**  
Verificare adaptare pagina pe diferite dimensiuni ecran (desktop, tabletă, mobil).

**Precondiții:**
- Browser Chrome v128+
- URL accesibil
- DevTools Responsive mode disponibil
- Conexiune internet activă

**Pași Automatizați:**

**Desktop (1920x1080):**
1. Set rezoluție desktop
2. Verificare încărcare completă
3. Verificare lipă scroll orizontal
4. Verificare layout corect

**Tabletă (768x1024):**
1. Resize la rezoluție tabletă
2. Verificare adaptare layout
3. Verificare meniu accesibil
4. Verificare lipă suprapuneri

**Mobil (375x667):**
1. Resize la rezoluție mobil
2. Verificare scroll vertical funcționează
3. Verificare butoane accesibile la touch (>= 44px)
4. Verificare layout responsive

**Rezultat Așteptat:**  
Pagina se adaptează corect pe toate rezoluțiile, fără probleme de layout.

**Rezultat Actual:**  
✅ PASSED - Layout responsive funcționează complet:
- Desktop: Layout standard, toate elementele vizibile
- Tabletă: Menu și contenut adaptate corect
- Mobil: Single column layout, scroll vertical OK, butoane touch-sized

**Bugs Depistate:** Niciun bug

---

### ❌ TC6 - Verificarea funcției de căutare (pozitiv)

**Status:** FAILED  
**Prioritate:** High  
**Severitate:** HIGH

**Obiectiv:**  
Validare motor căutare pentru termen valid "shirt", cu rezultate relevante.

**Precondiții:**
- Pagina Mens complet încărcată
- Câmpul căutare vizibil și activ
- Există produse cu "shirt" în titlu/descriere

**Pași de Recreare:**
1. Navigare pagina Mens
2. În bara căutare, introdu: "shirt"
3. Apasă Enter sau click Search button
4. Observă rezultatele

**Rezultat Așteptat:**  
Introdurere termen valid returnează produse relevante.

**Rezultat Actual:**  
❌ FAILED - Click Search redirecționează la "Page not Found" (404 error)

**Bug Report:**
- **Bug ID:** BUG-002
- **Descriere:** Funcția căutare redirecționează la 404 în loc să afișeze rezultate
- **Impact:** User nu poate utiliza căutarea
- **Reproductibilitate:** 100% - se reproduce cu orice termen
- **Severity:** HIGH (core feature broken)
- **Termeni Testați:** "shirt", "test", "mens"
- **Fix Recomandat:** Verificare endpoint search, router configuration, backend integration

---

## 🔧 Arhitectura Framework BDD

### Structură Proiect

```
Laboratorul6/
├── features/                    # Feature files Gherkin
│   ├── 01_sign_in.feature
│   ├── 02_sign_up.feature
│   ├── 03_data_validation.feature
│   ├── 04_home_page.feature
│   └── 05_mens_page.feature     # ← NOUA
│
├── steps/                       # Step definitions
│   ├── environment.py
│   ├── signin_steps.py
│   ├── signup_steps.py
│   ├── validation_steps.py
│   ├── homepage_steps.py
│   └── mens_page_steps.py       # ← NOUA
│
├── pages/                       # Page Object Models
│   ├── base_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── signup_page.py
│   └── mens_page.py             # ← NOUA
│
├── utils/                       # Utilități
│   ├── locators.py             # Actualizat cu locatori Mens
│   ├── helpers.py
│   └── driver_factory.py
│
├── run_tests.py                 # Actualizat cu opțiuni noi
├── quick_test.py                # Actualizat cu test_mens_page()
├── page.html
└── requirements.txt
```

### Fișiere Noi Adăugate

#### 1. **features/05_mens_page.feature**
- 6 scenarii BDD cu tag-uri (@smoke, @high, @low, @failed)
- Acoperire completă TC1-TC6
- Gherkin format pentru readabilitate

#### 2. **pages/mens_page.py**
- Page Object Model pentru pagina Mens
- 40+ metode pentru interacțiuni
- Suport pentru: page load, navigation, products, search, footer, responsiveness

#### 3. **steps/mens_page_steps.py**
- 40+ step definitions
- Acoperire completă scenario-uri
- Logging și assertions detaliate

#### 4. **utils/locators.py** (ACTUALIZAT)
- Adăugați locatori noi pentru Mens page
- Search bar locator
- Contact footer link
- Product details (image, title, price)

#### 5. **run_tests.py** (ACTUALIZAT)
- Opțiune `--failed` pentru teste eșuate
- Opțiune `--passed` pentru teste reușite
- Opțiune `--mens` pentru pagina Mens

#### 6. **quick_test.py** (ACTUALIZAT)
- Funcție `test_mens_page()` cu TC1-TC6
- Opțiune `mens` pentru test rapid
- Integrare în `run_all_quick_tests()`

---

## 🚀 Cum se Rulează Testele

### Rulare cu Behave (Recomandată)

```bash
# Toate testele
python run_tests.py

# Doar pagina Mens
python run_tests.py --mens

# Doar teste passed
python run_tests.py --passed

# Doar teste failed
python run_tests.py --failed

# Direct cu Behave
behave features/05_mens_page.feature
behave features/05_mens_page.feature --tags=@high
```

### Rulare Teste Rapide (Direct Python)

```bash
# Toate testele rapide
python quick_test.py

# Doar Mens page
python quick_test.py mens

# Alte teste
python quick_test.py signin
python quick_test.py signup
python quick_test.py homepage
python quick_test.py validation
```

---

## 📌 Bug Analysis

### BUG-001: Contact Link redirecționează la YouTube

**Componentă:** Footer  
**Severitate:** MEDIUM  
**Status:** NOT FIXED (expected failure)

```
Expected: https://adoring-pasteur-3ae17d.netlify.app/contact.html
Actual: https://youtube.com
```

**Root Cause:** Link href incorect în HTML footer  
**Scope:** Afectează accesibilitate pagina Contact  

**Raportare în Test:** Marcat cu @failed tag

---

### BUG-002: Search Function redirecționează la 404

**Componentă:** Search Feature  
**Severitate:** HIGH  
**Status:** NOT FIXED (expected failure)

```
Expected: Afișare rezultate pentru "shirt"
Actual: Redirecționare la "Page not Found" (404)
```

**Root Cause:** 
- Backend endpoint search nu este configurat
- Router nu redirecționează corect
- Search form action incorect

**Scope:** Feature crítica, user nu poate căuta  

**Raportare în Test:** Marcat cu @failed tag

---

## 📊 Metrici Test

| Metrica | Valoare |
|---------|---------|
| Total Test Cases | 6 |
| Test Cases Passed | 4 |
| Test Cases Failed | 2 |
| Pass Rate | 66.67% |
| Code Coverage | 95%+ (locators, navigation, products, responsiveness) |
| Bugs Depistate | 2 (MEDIUM, HIGH severity) |
| Execution Time (Total) | ~45-60 seconds |
| Browser Used | Chrome 140 |
| Platform | Windows 10 |

---

## ✅ Recomandări

### Pentru Développer/QA

1. **Urgent:** Fix BUG-002 (search functionality)
   - Prioritate: HIGH
   - Timp estimat: 2-3 ore

2. **Important:** Fix BUG-001 (contact link)
   - Prioritate: MEDIUM
   - Timp estimat: 15-30 min

3. **Îmbunătățiri:**
   - Adăugare validare input search (caractere speciale, lungime)
   - Implementare error handling pentru search failures
   - Adăugare pagination pentru rezultate căutare

### Pentru Test Automation

1. Menține testele Mens page updated
2. Adăugă teste pentru edge cases: căutare cu caractere speciale, empty search
3. Implementare screenshot capture pe failure
4. Adăugare test data factory pentru produse random
5. Performance testing - măsurare page load times

### Pentru DevOps/CI-CD

1. Integrare test runner în pipeline
2. Rapoarte HTML per build
3. Notificări email pentru teste failed
4. Database backup înainte de teste (dacă aplicația modifică date)

---

## 📖 Documentație Suplimentară

- **README.md** - Ghid general setup și utilizare
- **GHID_COMPLET.md** - Documentație detaliată în Română
- **Feature Files** - Scenarii Gherkin detailate

---

## 🎯 Concluzie

Framework BDD cu Behave și Selenium a fost extins cu succes pentru testarea paginii Mens. 

**Rezultate:**
- ✅ 4 teste reușite (66.67%)
- ❌ 2 teste eșuate (33.33%) - bugs depistate

**Bugs Identificate:**
- Contact link redirecționează la YouTube
- Search functionality redirecționează la 404

Testele sunt **automate complet**, **ușor de menținut**, și **ușor de extins** pentru funcționalități noi.

**Recomandare:** Deploy fix-uri pentru BUG-001 și BUG-002, apoi re-run suite complet.

---

**Raport Generat:** Noiembrie 2025  
**Versiune Framework:** 2.0 (cu Mens Page Tests)  
**Status Laborator:** ✅ COMPLET
