import pandas as pd
from pysentimiento import create_analyzer
import matplotlib.pyplot as plt

df = pd.read_excel("C:/Users/valentina/Documents/comentarios8m.xlsx")

#Función para analizar sentimientos
analyzer_sentimientos = create_analyzer(task='sentiment', lang='es')

def analizar_sentimiento(comentario):
    resultado = analyzer_sentimientos.predict(comentario)
    return resultado.output

df['Sentimiento'] = df['Comment'].apply(analizar_sentimiento)


#Función para discurso de odio
analyzer_odio = create_analyzer(task='hate_speech', lang="es")

def detectar_discurso_odio(comentario):
    resultado = analyzer_odio.predict(comentario)
    return resultado.output

df ['Discurso de Odio'] = df['Comment'].apply(detectar_discurso_odio)


#Función para dirigimiento a minorías
analyzer_minorias = create_analyzer(task='hate_speech', lang='es')

def detectar_dirigimiento_minorias(comentario):
    resultado = analyzer_minorias.predict(comentario)
    return resultado.output

df['Dirigimiento a Minorías'] = df['Comment'].apply(detectar_dirigimiento_minorias)

#Visualizar los resultados de manera gráfica
df['Sentimiento'].value_counts().plot(kind='pie',autopct='%1.1f%%' ,title='Recuento de sentimientos')
plt.axis('equal')
plt.show()