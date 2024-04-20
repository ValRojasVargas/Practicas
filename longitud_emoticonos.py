import pandas as pd
import re

df = pd.read_excel("C:/Users/valentina/Documents/comentarios8m.xlsx")


#Función para la longitud
def longitud_mensaje(mensaje):
    return len(mensaje)

longitudes = df['Comment'].apply(longitud_mensaje)
longitud_media = longitudes.mean()

print(f'Longitud media de los comentarios: {longitud_media}')

#Función para comprobar si hay emoticonos en los comentarios
def tiene_emoticonos(comentario):
    patron_emoticonos = r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U00002700-\U000027BF\U00002600-\U000026FF\U0000FE0F]+'
    return bool(re.search(patron_emoticonos, comentario))

df['Tiene Emoticonos'] = df['Comment'].apply(tiene_emoticonos)
total_con_emoticonos = df['Tiene Emoticonos'].sum()

print(f'Número de comentarios con emoticonos: {total_con_emoticonos}')