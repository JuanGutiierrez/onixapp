import pandas as pd

from helpers.crearVentasCSV import crearCSV
from helpers.crearTablaHTML import crearTabla

import matplotlib.pyplot as plt

from data.ventas import ventas

#1 Crear un CSV con los datos de las ventas
crearCSV(ventas, 'ventas.csv')

#2 cargo la fuente de datos y con PANDAS creo un DATAFRAME
ventasDataFrame=pd.read_csv('data/ventas.csv')
crearTabla(ventasDataFrame,'tablaventas')

#3 explorar los datos
'''examen1=ventasDataFrame.head()
examen2=ventasDataFrame.tail()
examen3=ventasDataFrame.head(20)
examen4=ventasDataFrame.info()
examen5=ventasDataFrame.describe()
examen6=ventasDataFrame.tail(50)'''


#4 filtrar y ordenar (limpiar)
filtroUno=ventasDataFrame.query("(Costo>=290000) and (Costo<=300000)")
totalventas=filtroUno[['Costo','Cliente']]

#generando html con resultados del filtro
crearTabla(filtroUno,'ventasBajoCosto')


#6 presentar y exportar los datos
ventasAltas=ventasDataFrame.nlargest(5,"Costo")
ventasBajas=ventasDataFrame.nsmallest(5,"Costo")
print(ventasAltas)

#Graficando un DATAFRAME co MATLOTLIB
ventasAltas["NumeroOrden"]
colores=['#e36dec', '#f364dc','#ff5ccb','#ff55ba','#ff51a8','#ff4f96','#ff5185','#ff5573']
plt.figure(figsize=(10,10))
plt.bar(ventasAltas["Cliente"],ventasAltas["Costo"], color=colores)

#Personalizando la grafica
plt.xlabel("Cliente")
plt.ylabel("Costo")
plt.title("Ventas mas altas en ultimo mes")

plt.show()