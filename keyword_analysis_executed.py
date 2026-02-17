#!/usr/bin/env python
# coding: utf-8

# # Keyword-Analyse Tool für SEO
# 
# Dieses Notebook analysiert eine Webseite und identifiziert Keywords, die für Google relevant sein könnten. Dabei werden statistische Methoden wie TF-IDF, RAKE und HTML-Gewichtung kombiniert.

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from rake_nltk import Rake
import nltk
from collections import Counter

# NLTK Daten herunterladen
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.corpus import stopwords


# ## 1. Web-Scraping & Datenextraktion
# 
# Zuerst laden wir den Inhalt der Seite herunter und extrahieren Text aus wichtigen SEO-Elementen (Title, H1, H2, Body).

# In[2]:


def scrape_website(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # SEO Relevante Elemente extrahieren
    data = {
        'title': soup.title.string if soup.title else '',
        'h1': [h1.get_text().strip() for h1 in soup.find_all('h1')],
        'h2': [h2.get_text().strip() for h2 in soup.find_all('h2')],
        'meta_description': '',
        'body_text': ''
    }
    
    desc = soup.find('meta', attrs={'name': 'description'})
    if desc:
        data['meta_description'] = desc.get('content', '')
    
    # Script und Style Tags entfernen
    for script in soup(["script", "style"]):
        script.decompose()
        
    data['body_text'] = soup.get_text(separator=' ', strip=True)
    
    return data


# ## 2. Text-Vorverarbeitung
# 
# Reinigung des Textes und Vorbereitung für die statistische Analyse.

# In[3]:


def clean_text(text, lang='german'):
    # Kleinschreibung und Sonderzeichen entfernen
    text = text.lower()
    text = re.sub(r'[^a-zäöüß\s]', '', text)
    
    # Stopwords entfernen
    stop_words = set(stopwords.words(lang))
    words = text.split()
    cleaned_words = [w for w in words if w not in stop_words and len(w) > 2]
    
    return " ".join(cleaned_words)


# ## 3. Statistische Analyse & Gewichtung
# 
# Hier kombinieren wir verschiedene Scores:
# - TF-IDF: Wie wichtig ist das Wort im Text?
# - HTML-Boost: Ist das Wort in einer Überschrift oder im Titel?

# In[4]:


def get_keywords(url, lang='german'):
    raw_data = scrape_website(url)
    full_text = f"{raw_data['title']} {raw_data['meta_description']} {' '.join(raw_data['h1'])} {' '.join(raw_data['h2'])} {raw_data['body_text']}"
    
    cleaned_text = clean_text(full_text, lang)
    
    # TF-IDF Analyse (für Einzelwörter)
    vectorizer = TfidfVectorizer(ngram_range=(1, 1))
    tfidf_matrix = vectorizer.fit_transform([cleaned_text])
    feature_names = vectorizer.get_feature_names_out()
    scores = tfidf_matrix.toarray().flatten()
    
    word_scores = dict(zip(feature_names, scores))
    
    # RAKE für Phrasen
    r = Rake(language=lang)
    r.extract_keywords_from_text(full_text)
    rake_phrases = r.get_ranked_phrases_with_scores()[:20]
    
    # SEO Boost-System
    # Wir geben Wörtern in Title und H1 einen höheren Score
    boosted_scores = word_scores.copy()
    
    important_areas = {
        'title': 5.0,
        'h1': 3.0,
        'h2': 1.5,
        'meta_description': 2.0
    }
    
    for area, boost in important_areas.items():
        content = ""
        if isinstance(raw_data[area], list):
            content = " ".join(raw_data[area])
        else:
            content = raw_data[area]
        
        area_words = clean_text(content, lang).split()
        for word in area_words:
            if word in boosted_scores:
                boosted_scores[word] *= boost
    
    # Ergebnisse aufbereiten
    sorted_keywords = sorted(boosted_scores.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_keywords[:20], rake_phrases


# ## 4. Testlauf
# 
# Geben Sie hier die URL ein, die Sie analysieren möchten.

# In[5]:


URL_TO_ANALYZE = "https://www.google.com" # Beispiel-URL
keywords, phrases = get_keywords(URL_TO_ANALYZE, 'german')

print(f"--- Top Keywords für {URL_TO_ANALYZE} ---")
df_kw = pd.DataFrame(keywords, columns=['Keyword', 'Score'])
print(df_kw.head(10))

print("\n--- Top Phrasen (RAKE) ---")
for score, phrase in phrases[:10]:
    print(f"{phrase} (Score: {score:.2f})")
