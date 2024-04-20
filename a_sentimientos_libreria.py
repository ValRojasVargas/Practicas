import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize

nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
df = pd.read_excel("C:/Users/valentina/Documents/comentarios8m.xlsx")

#función: polaridad de sentimientos
sid=  SentimentIntensityAnalyzer()

def analizar_sentimiento(comentario):
    #calcular el puntuaje de sentimiento
    scores = sid.polarity_scores(comentario)
    if scores['compound'] >=0.05:
        return 'Positivo'
    elif scores['compound'] <=-0.05:
        return 'Negativo'
    else:
        return 'Neutral'
    

#función: discurso de odio. uso las mismas palabras que en el ejercicio con spacy
palabras_clave_odio = ['odio', 'abuso', 'miedo', 'violencia', 'justicia', 'sufrimiento', 'grito']

def detectar_discurso_odio(comentario):
    tokens= word_tokenize(comentario.lower())
    for palabra in palabras_clave_odio:
        if palabra in tokens:
            return True
        return False
    

#función: discurso dirigido a minorías, usando las mismas palabras claves antiguas
palabras_clave_minorias =['minoria', 'racializadas', 'discriminación', 'inclusión', 'inmigración', 'género', 'excluir', 'diversidad', 'latino', 'latina','hispano', 'blanco', 'negro', 'blanca', 'negra', 'lesbiana', 'transexual', 'país']    

def detectar_discurso_minorias(comentario):
    tokens = word_tokenize(comentario.lower())
    for palabra in palabras_clave_minorias:
        if palabra in tokens:
            return True
        return False

#función para detectaar las entidades nombradas
def detectar_entidades(comentario):
    palabras = nltk.word_tokenize(comentario)
    palabras_etiquetadas = nltk.pos_tag(palabras)
    entidades = nltk.ne_chunk(palabras_etiquetadas)
    return entidades


#aplicar a cada comentario las funciones
df['Sentimiento'] = df ['Comment'].apply(analizar_sentimiento)
df['Discurso de Odio'] = df['Comment'].apply(detectar_discurso_odio)
df['Discurso dirigido a Minorías'] = df ['Comment'].apply(detectar_discurso_minorias)
df['Entidades nombradas'] = df ['Comment'].apply(detectar_entidades)

df.to_excel('resultados_sentimientos_nltk.xlsx', index=False)