import pandas as pd
import nltk
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from textblob import TextBlob
from nltk.corpus import stopwords

nltk.download('brown')
nltk.download('punkt')
nltk.download('stopwords')

df = pd.read_excel("C:/Users/valentina/Documents/comentarios8m.xlsx")

#Subjetividad
def calcular_subjetividad (comment):
    blob =TextBlob(comment)
    return blob.sentiment.subjectivity

subjetividad_promedio = df['Comment'].apply(calcular_subjetividad).mean()

#gráfico:
plt.figure(figsize=(8,6))
labels = ['Baja', 'Alta']
explode = (0, 0.1)
plt.pie([subjetividad_promedio, 1 - subjetividad_promedio], labels=labels, explode=explode, autopct='%1.1f%%', startangle=140, colors=['lightcoral', 'lightgreen', 'lightskyble'])
plt.axis('equal')
plt.title('Distrubución de subjetividad')
plt.show()

print (f'Subjetividad promedio: {subjetividad_promedio}')


#Extrajer sustantivos y frases nominales
def extraer_sustantivos (comment):
    blob = TextBlob(comment)
    return blob.noun_phrases

todas_frases_nominales = df ['Comment'].apply(extraer_sustantivos)
frases_nominales_totales = [item for sublist in todas_frases_nominales for item in sublist]
longitud_total = len(frases_nominales_totales)

#gráfico:
plt.figure(figsize=(8,6))
plt.bar(['Frases Nominales'], [longitud_total], color='lightgreen')
plt.title('Número total de sustantivos y frases nominales')
plt.ylabel('Cantidad')
plt.show()

print (f'Número total de sustantivos y frases nominales: {longitud_total}')



#Tokenización de las palabras con NLTK
def tokenize_words(comment):
    return word_tokenize(comment)

df['Tokenized Words'] = df['Comment'].apply(tokenize_words)
df['NumPalabras'] = df['Tokenized Words'].apply(len)

#gráfico:
plt.figure(figsize=(8, 6))
plt.hist(df['NumPalabras'], bins=20, color='orange', edgecolor='black')
plt.title('Distribución del número de palabras')
plt.xlabel('Número de palabras')
plt.ylabel('Número de comentarios')
plt.show()

print(df[['Comment', 'Tokenized Words']])



#Calcular la frecuencia de las palabras
stop_words = set(stopwords.words('spanish'))

def calcular_frecuencia_palabras(texto):
    #tokenizar el texto en palabras
    tokens = nltk.word_tokenize(texto)
    #filtrar las stopwords
    tokens_filtrados = [word.lower() for word in tokens if word.lower() not in stop_words and word.isalpha()]
    #calcular la frecuencia en sí
    frecuencia = nltk.FreqDist(tokens_filtrados)
    return frecuencia

df['Frecuencia de palabras'] = df ['Comment'].apply(calcular_frecuencia_palabras)

#gráfico:
total_frecuencia = nltk.FreqDist([word for sublist in df['Frecuencia de palabras'] for word in sublist])

num_palabras_mostrar = 10
palabras_comunes = total_frecuencia.most_common(num_palabras_mostrar)

palabras=[word[0] for word in palabras_comunes]
frecuencias=[word[1] for word in palabras_comunes]

#crear grafico
plt.figure(figsize=(10, 6))
plt.pie(frecuencias, labels=palabras, autopct='%1.1f%%')
plt.title('Frecuencia de las 10 palabras más comunes')
plt.show()

print(df.head())