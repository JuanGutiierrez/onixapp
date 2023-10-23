import pandas as pd

from helpers.crearVentasCSV import crearCSV
from data.ventas import ventas

#1 Crear un CSV con los datos de las ventas
crearCSV(ventas, 'ventas.csv')

#2 cargo la fuente de datos y con PANDAS creo un DATAFRAME
ventasDataFrame=pd.read_csv('data/ventas.csv')

#3 explorar los datos
examen1=ventasDataFrame.head()
examen2=ventasDataFrame.tail()
examen3=ventasDataFrame.head(20)
examen4=ventasDataFrame.info()
examen5=ventasDataFrame.describe()
examen6=ventasDataFrame.tail(50)


#4 filtrar y ordenar (limpiar)


#5 modelar o aplicar modelos 


#6 presentar y exportar los datos
print(examen1)
print("\n")
print(examen2)
print("\n")
print(examen3)
print("\n")
print(examen4)
print("\n")
print(examen5)
print("\n")
print(examen6)