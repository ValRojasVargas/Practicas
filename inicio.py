import pandas as pd
from textblob import TextBlob
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

#cargar comentearios
df = pd.read_excel("C:/Users/valentina/Documents/comentarios8m.xlsx")

#prueba de análisis de sentimiento.
def analyze_sentiment(comment):
    analysis = TextBlob(comment)
    return analysis.sentiment.polarity

df['Sentiment'] = df['Comment'].apply(analyze_sentiment)

df.to_excel('ruta/al/archivo_con_sentimiento.xlsx', index=False)
