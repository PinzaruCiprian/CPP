# language: ro
Funcționalitate: Testare Google Search
  Ca utilizator al Google
  Vreau să pot căuta informații
  Pentru a găsi rezultate relevante

  Context:
    Dat fiind că utilizatorul deschide browserul Chrome

  @smoke @google_page
  Scenariu: Verificare deschidere pagină Google
    Când utilizatorul accesează "https://www.google.co.in"
    Atunci pagina Google ar trebui să se deschidă cu succes
    Și search box-ul ar trebui să fie vizibil
    Și logo-ul Google ar trebui să fie afișat

  @search @results_count
  Scenariu: Verificare număr rezultate afișate pe o singură pagină
    Dat fiind că utilizatorul este pe pagina Google
    Când utilizatorul caută după "automation testing"
    Atunci pagina de rezultate ar trebui să se încarce
    Și ar trebui să fie afișate rezultate de căutare
    Și numărul de rezultate de pe pagină ar trebui să fie între 8 și 15

  @search @empty_search
  Scenariu: Verificare comportament la căutare goală
    Dat fiind că utilizatorul este pe pagina Google
    Când utilizatorul nu introduce nimic în search box
    Și utilizatorul apasă pe butonul "Google Search"
    Atunci utilizatorul ar trebui să rămână pe pagina principală Google
    Și URL-ul nu ar trebui să conțină "search?"

  @search @did_you_mean
  Scenariu: Verificare afișare "Did you mean" pentru căutări irelevante
    Dat fiind că utilizatorul este pe pagina Google
    Când utilizatorul caută după "speling mistke"
    Atunci pagina de rezultate ar trebui să se încarce
    Și ar trebui să fie afișat linkul "Did you mean"
