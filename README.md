# Truncation and Lemmatization

## Description
This project focuses on text processing using Python and the Natural Language Toolkit (nltk) library. The primary goal is to prepare textual data for information retrieval tasks by performing various preprocessing steps, including tokenization, punctuation removal, conversion to lowercase, removal of stopwords, stemming, and lemmatization. The project includes practical implementations and a comparative analysis of different stemming and lemmatization techniques.

### Files Included
- **lab2.py**: A Python script that performs various text processing tasks.
- **prueba.txt**: A text file containing a sample story titled "The Robber Bridegroom".
- **Laboratorio 2 Truncado y Lematización.pdf**: Official documentation detailing the objectives, methodology, and results of the project.

### Notable Code Snippets

#### 1. Reading and Tokenizing Text
This snippet reads the content of `prueba.txt` and tokenizes the text using the `nltk` library.

```python
import os
import nltk
nltk.download('punkt')

# Read the content of the external file
archivo_path = os.path.join(os.path.dirname(__file__), 'prueba.txt')
with open(archivo_path, 'r', encoding='utf-8') as archivo:
    texto = archivo.read()

# Tokenization using NLTK
palabras = nltk.word_tokenize(texto)
```
#### 2. Removing Punctuation

This snippet defines a regular expression to remove punctuation from the tokenized text.

```python
import re
import string

# Define regular expression to remove punctuation
simbolos_extra = '’'
re_punc = re.compile('[%s%s]' % (re.escape(string.punctuation), re.escape(simbolos_extra)))

# Remove punctuation from each word
stripped = [re_punc.sub('', w) for w in palabras]
```

#### 3. Stemming and Lemmatization

This snippet demonstrates the use of PorterStemmer, SnowballStemmer, and WordNetLemmatizer to stem and lemmatize the cleaned text.

```python
from nltk.stem.porter import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer

# Stemming with PorterStemmer
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_words]

# Stemming with SnowballStemmer
stemmer2 = SnowballStemmer('english')
stemmed_words2 = [stemmer2.stem(word) for word in filtered_words]

# Lemmatization with WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
```

### Official Documentation Summary

The official documentation provided in "Laboratorio 2 Truncado y Lematización.pdf" outlines the following key points:

#### Objectives

-   To prepare texts for information retrieval by performing tokenization, punctuation removal, converting text to lowercase, removing stopwords, and truncating words using different stemming methods.
-   To compare the results of different stemming methods (Porter, Snowball) and lemmatization.

#### Methodology

1.  **Tokenization**: Splitting text into individual tokens (words).
2.  **Punctuation Removal**: Using regular expressions to strip punctuation from tokens.
3.  **Lowercase Conversion**: Converting all tokens to lowercase.
4.  **Stopwords Removal**: Eliminating common stopwords using the `nltk` library.
5.  **Stemming and Lemmatization**: Applying PorterStemmer, SnowballStemmer, and WordNetLemmatizer to reduce words to their base or root form.

#### Results and Discussion

-   The results show the effectiveness of each method in reducing words to their base form, with PorterStemmer providing the most aggressive stemming, followed by SnowballStemmer, and WordNetLemmatizer offering a more moderate approach.
-   The comparative analysis highlights the strengths and weaknesses of each method in terms of accuracy and preservation of semantic meaning.

### Installation and Usage

1.  Clone the repository to your local machine.
2.  Ensure you have Python and `nltk` installed.
3.  Run the `lab2.py` script to process the text in `prueba.txt`.

```bash
git clone https://github.com/KPlanisphere/truncation-and-lemmatization.git
cd truncation-and-lemmatization
python lab2.py
```

### Dependencies

-   Python
-   NLTK library