import pandas as pd

#uso basico de PANDAS
#1. Fuente de datos (lista)
ciudades=['Jerusalen','Telabit','kiev','itagui','pitalito']
#2. Procesar y convertir una lista en DataFrame
datafameCiudades= pd.DataFrame({'Ciudad':ciudades})
print(datafameCiudades)

###### data frame es una lista tabulada que me permite convertir los datos
#1. Fuente de datos Una lista de diccionarios(coleccion)
estudiantes = [
    {'id':1,'nombre':'Juan Discotecas','promedio':0.0},
    {'id':2,'nombre':'Santi el Bicho','promedio':0.5},
    {'id':3,'nombre':'santi diomedez','promedio':2.0},
    {'id':4,'nombre':'Susana no volvi','promedio':1.8},
    {'id':5,'nombre':'Juancho Styles','promedio':0.0}
]

#2. Convertir los datos de entrada en un dataFrame
dataFrameEstudiantesRepitentes=pd.DataFrame(estudiantes)
print (dataFrameEstudiantesRepitentes)