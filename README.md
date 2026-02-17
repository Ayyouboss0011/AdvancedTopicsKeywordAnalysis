# 📊 DanielKeywordStatistics - SEO Keyword-Analyse Tool

Ein leistungsstarkes und interaktives Tool zur Analyse von Webseiten-Keywords. Dieses Projekt hilft dabei, SEO-relevante Begriffe direkt von einer URL zu extrahieren, sie zu gewichten und Long-Tail-Phrasen zu identifizieren.

## 🚀 Features

- **Web-Scraping:** Automatisches Auslesen von HTML-Inhalten (Titel, H1-H3, Bilder, Links).
- **Textbereinigung:** Filtert Stoppwörter und Sonderzeichen in Deutsch und Englisch.
- **SEO-Gewichtung:** Keywords werden basierend auf ihrer Position (z.B. im Titel oder in H1) höher bewertet.
- **Long-Tail Analyse:** Nutzung des RAKE-Algorithmus zur Identifizierung komplexer Suchphrasen.
- **Interaktive UI:** Einfache URL-Eingabe und Sprachauswahl über Jupyter Widgets.
- **Visualisierungen:** Anschauliche Diagramme mit Matplotlib und Seaborn.

---

## 🛠 Installation & Einrichtung

Befolgen Sie diese Schritte, um das Projekt lokal auf Ihrem Rechner zum Laufen zu bringen.

### 1. Repository klonen

Zuerst müssen Sie das Projekt von GitHub herunterladen:

```bash
git clone https://github.com/Ayyouboss0011/AdvancedTopicsKeywordAnalysis.git
cd AdvancedTopicsKeywordAnalysis
```

### 2. Virtuelle Umgebung erstellen (empfohlen)

Es wird empfohlen, eine virtuelle Umgebung zu verwenden, um Abhängigkeitskonflikte zu vermeiden:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Abhängigkeiten installieren

Installieren Sie alle benötigten Python-Bibliotheken (einschließlich Jupyter):

```bash
pip install -r requirements.txt
```

*(Hinweis: Falls Jupyter nicht in der requirements.txt enthalten ist, führen Sie zusätzlich `pip install jupyter` aus.)*

---

## 📓 Jupyter Notebook starten

Das Herzstück der Analyse ist das Jupyter Notebook. So starten Sie es:

1. **Jupyter starten:**
   ```bash
   jupyter notebook
   ```
   (Alternativ können Sie die Dateien auch direkt in **VS Code** mit der Jupyter-Erweiterung öffnen.)

2. **Notebook öffnen:**
   Öffnen Sie im Browser die Datei `keyword_analysis.ipynb`.

3. **Kernel auswählen:**
   Stellen Sie sicher, dass oben rechts der richtige Python-Kernel (aus Ihrer virtuellen Umgebung `venv`) ausgewählt ist.

4. **Zellen ausführen:**
   Klicken Sie auf "Run All" oder gehen Sie die Zellen einzeln mit `Shift + Enter` durch.

---

## 📖 Bedienungsanleitung

1. **URL eingeben:** Geben Sie im entsprechenden Textfeld die URL der zu analysierenden Webseite ein.
2. **Sprache wählen:** Wählen Sie zwischen Deutsch und Englisch für die korrekte Stoppwort-Filterung.
3. **Analyse starten:** Führen Sie die nachfolgenden Zellen aus, um:
   - Die Seitenstruktur zu visualisieren.
   - Den Effekt der Textbereinigung zu sehen.
   - Die Top 15 SEO-Keywords als Diagramm zu erhalten.
   - Die besten Long-Tail Phrasen auszulesen.

---

## 🔍 Code-Erklärung (Deep Dive)

Das Tool ist in verschiedene logische Phasen unterteilt, die nacheinander ablaufen:

### 1. Daten-Extraktion (`fetch_data`)
Die Funktion nutzt die `requests`-Bibliothek mit einem benutzerdefinierten User-Agent, um die Webseite abzurufen. `BeautifulSoup` parst anschließend das HTML und ermöglicht den Zugriff auf SEO-relevante Tags wie `<title>`, `<h1>`, `<h2>`, `<h3>`, `<a>` (Links) und `<img>` (Bilder).

### 2. Text-Bereinigung (`get_clean_text`)
Um die Relevanz zu erhöhen, wird der Text transformiert:
- **Bereinigung:** Entfernung von Script- und Style-Tags.
- **Normalisierung:** Umwandlung in Kleinschreibung und Extraktion von Wörtern (Regex `[a-zäöüß]+`).
- **Stopword-Filtering:** Wörter wie "und", "der" oder "the" werden basierend auf der gewählten Sprache (`nltk.corpus.stopwords`) entfernt.

### 3. SEO-Gewichtung & Scoring (`calculate_seo_scores`)
Dies ist das Herzstück der Analyse. Ein Keyword erhält nicht nur Punkte für die Häufigkeit, sondern auch einen **Boost** basierend auf seiner Position:
- **Basis-Score:** Jedes Vorkommen zählt 1.0 Punkt.
- **Titel-Boost (5.0x):** Keywords im HTML-Titel werden mit dem Faktor 5 multipliziert.
- **H1-Boost (3.0x):** Keywords in der Hauptüberschrift erhalten den Faktor 3.
Am Ende werden die Top 15 Keywords nach ihrem finalen Score sortiert.

### 4. Long-Tail Keyword Extraction (RAKE)
Der **RAKE-Algorithmus** (Rapid Automatic Keyword Extraction) analysiert Wort-Kookkurrenzen im Volltext. Er identifiziert Wortgruppen (Phrasen), die häufig zusammen auftreten, und bewertet sie. Das Tool zeigt gezielt Phrasen mit mehr als einem Wort an, um spezifische Suchbegriffe zu finden.

### 5. Visualisierung
- **Struktur-Plot:** Ein Barplot zeigt die Verteilung der HTML-Tags.
- **Bereinigungs-Plot:** Veranschaulicht die Reduktion der Datenmenge durch den Stopword-Filter.
- **Keyword-Plot:** Visualisiert die 15 stärksten Keywords nach ihrem SEO-Score.

---

## 📦 Abhängigkeiten

Die wichtigsten verwendeten Bibliotheken sind:
- `requests` & `BeautifulSoup4` (Scraping)
- `pandas` & `numpy` (Datenverarbeitung)
- `matplotlib` & `seaborn` (Visualisierung)
- `rake-nltk` & `nltk` (NLP / Keyword-Extraktion)
- `scikit-learn` (TF-IDF Analyse)
- `ipywidgets` (Interaktive Elemente)

