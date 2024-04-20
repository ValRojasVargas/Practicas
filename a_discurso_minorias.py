import spacy
import pandas as pd
import matplotlib.pyplot as plt 

nlp = spacy.load('es_core_news_sm')
df = pd.read_excel("C:/Users/valentina/Documents/comentarios8m.xlsx")

#función
def encontrar_discurso_minorias(texto):
    doc = nlp(texto)
    terminos_minorias =['minoria', 'racializadas', 'discriminación', 'inclusión', 'inmigración', 'género', 'excluir', 'diversidad', 'latino', 'latina','hispano', 'blanco', 'negro', 'blanca', 'negra', 'lesbiana', 'transexual', 'país']

    return any(token.text.lower() in terminos_minorias for token in doc)

df['Discurso a minorías']= df['Comment'].apply(encontrar_discurso_minorias)

#calcular estadísticas
total_comentarios =len (df)
comentarios_a_minorias =df['Discurso a minorías'].sum()
porcentaje_minorias =(comentarios_a_minorias / total_comentarios) *100

comentarios_sin_minorias = total_comentarios - comentarios_a_minorias

#crear lista con los valores
sizes =[comentarios_a_minorias, comentarios_sin_minorias]
labels=['Con discurso dirigido a minorías', 'Sin discurso dirigido a minorías']

#crear gráfico
plt.figure(figsize=(8,6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Porcentaje de comentarios con y sin discurso dirigido a minorías')
plt.axis('equal')
plt.show()


print(f'Total de comentarios: {total_comentarios}')
print(f'Comentarios con discurso dirigido a minorías: {comentarios_a_minorias}')
print(f'Porcentaje de comentarios con discurso dirigido a minorías: {porcentaje_minorias:.2f}%')
