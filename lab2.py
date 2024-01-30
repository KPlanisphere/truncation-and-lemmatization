import re
import string
import nltk
nltk.download('wordnet')
import os
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer


nltk.download('punkt')
nltk.download('stopwords')

# Lee el contenido del archivo externo
archivo_path = os.path.join(os.path.dirname(__file__), 'lab1.txt')
with open(archivo_path, 'r', encoding='utf-8') as archivo:
    texto = archivo.read()

# Tokenización usando NLTK
palabras = nltk.word_tokenize(texto)

# separar por espacios
palabras = texto.split()

print("\n///// TEXTO SIN ESPACIOS\n")
print(palabras[:100])

# mostrar signos de puntuacion
print("\n///// SIGNOS DE PUNTUACION\n")
print(string.punctuation)

# Definir expresión regular para eliminar signos de puntuación
simbolos_extra =  '’'
re_punc = re.compile('[%s%s]' % (re.escape(string.punctuation), re.escape(simbolos_extra)))

# Eliminar signos de puntuación de cada palabra
stripped = [re_punc.sub('', w) for w in palabras]

print("\n///// TEXTO SIN SIGNOS DE PUNTUACION\n")
print(stripped[:100])

# Corvertir a minusculas cada palabra de la lista
for i in range(len(stripped)):
    stripped[i] = stripped[i].lower()


print("\n///// TEXTO EN MINUSCULAS\n")
print(stripped[:100])

# Obtener lista de stopwords en inglés
stopwords_english = set(stopwords.words('english'))

# Convertir el conjunto de stopwords a una lista
stopwords_english_list = list(stopwords_english)

# Imprimir las primeras 5 palabras vacías
print("\n///// PRIMERAS 5 PALABRAS VACÍAS\n")
print(stopwords_english_list[:5])
#print(stopwords_english[:5])

# Eliminar palabras vacías
filtered_words = [word for word in stripped if word not in stopwords_english]

# Imprime las primeras 100 palabras en minúsculas sin símbolos ni stopwords
print("\n///// TEXTO SIN PALABRAS VACIAS (BASE PARA TRUNCADAS, SNOWBALL STEMMER Y LEMMATIZER)\n")
print(filtered_words[:100])

stemmer = PorterStemmer()

stemmed_words = [stemmer.stem(word) for word in filtered_words]

# Imprime las primeras 100 palabras truncadas
print("\n///// TEXTO CON PALABRAS TRUNCADAS\n")
print(stemmed_words[:100])

stemmer2 = SnowballStemmer('english')

stemmed_words2 = [stemmer2.stem(word) for word in filtered_words]

# Imprime las primeras 100 palabras SNOWBALL STEMMER
print("\n///// TEXTO SNOWBALL STEMMER\n")
print(stemmed_words2[:100])

lemmatizer = WordNetLemmatizer()

lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

# Imprime las primeras 100 palabras LEMMATIZER 
print("\n///// TEXTO LEMMATIZER\n")
print(lemmatized_words[:100])



#C:\Users\mini_\AppData\Local\Programs\Python\Python312\python.exe "C:\Users\mini_\OneDrive\Documentos\Code Test\TEST 1\lab1.py7"








