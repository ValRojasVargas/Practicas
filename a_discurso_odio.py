import spacy
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("C:/Users/valentina/Documents/comentarios8m.xlsx")
nlp = spacy.load('es_core_news_sm')

#función para analizar
def encontrar_discurso_de_odio(texto):
    doc =nlp(texto)
    return any(token.text.lower() in ['odio', 'abuso', 'miedo', 'violencia', 'justicia', 'sufrimiento', 'grito'] for token in doc)

df['Discurso de odio'] = df['Comment'].apply(encontrar_discurso_de_odio)

#calcular estadísticas 
total_comentarios= len(df)
comentarios_con_odio =df['Discurso de odio'].sum()
porcentaje_odio = (comentarios_con_odio / total_comentarios)*100

comentarios_sin_odio= total_comentarios - comentarios_con_odio

#crear gráfico
datos = [comentarios_con_odio, comentarios_sin_odio]
etiquetas = ['Con discurso de odio', 'Sin discurso de odio']
colores = ['lightblue', 'lightcoral']
plt.pie(datos, labels=etiquetas, colors=colores, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Porcentaje de Comentarios con y sin discurso de odio')
plt.show()

print(f'Total de comentarios: {total_comentarios}')
print(f'Comentarios con discurso de odio:{comentarios_con_odio}')
print(f'Porcentaje de comentarios con discurso de odio:{porcentaje_odio:.2f}%')