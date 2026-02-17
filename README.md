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

Installieren Sie alle benötigten Python-Bibliotheken:

```bash
pip install -r requirements.txt
```

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

## 📦 Abhängigkeiten

Die wichtigsten verwendeten Bibliotheken sind:
- `requests` & `BeautifulSoup4` (Scraping)
- `pandas` & `numpy` (Datenverarbeitung)
- `matplotlib` & `seaborn` (Visualisierung)
- `rake-nltk` & `nltk` (NLP / Keyword-Extraktion)
- `scikit-learn` (TF-IDF Analyse)
- `ipywidgets` (Interaktive Elemente)

---



