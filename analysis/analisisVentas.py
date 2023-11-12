import pandas as pd
import matplotlib.pyplot as plt

from helpers.crearVentasCSV import crearCSV
from helpers.crearTablaHTML import crearTabla
from data.ventas import ventas

#1 Crear un CSV con los datos de las ventas
crearCSV(ventas, 'ventas.csv')

#2 cargo la fuente de datos y con PANDAS creo un DATAFRAME
ventasDataFrame=pd.read_csv('data/ventas.csv')

#4 filtrar y ordenar (limpiar)
filtroUno=ventasDataFrame.query("(Costo>=290000) and (Costo<=300000)")
totalventas=filtroUno[['NumeroOrden','Costo']]

#generando html con resultados del filtro
crearTabla(totalventas,'ventasBajoCosto')

#Graficando un DATAFRAME co MATLOTLIB
totalventas["NumeroOrden"]=totalventas["NumeroOrden"].astype(str)
colores=['#e36dec', '#f364dc','#ff5ccb','#ff55ba','#ff51a8','#ff4f96','#ff5185','#ff5573']
plt.figure(figsize=(10,10))
plt.bar(totalventas["Costo"],totalventas["NumeroOrden"], color=colores)

#Personalizando la grafica
plt.xlabel("Costo")
plt.ylabel("NumeroOrden")
plt.title("Ventas mas altas en ultimo mes")
plt.xticks(rotation=35)


rutaPDF="assets/img/barrasventas.pdf"
rutaGrafica="assets/img/barrasventas.png"
plt.savefig(rutaGrafica)
plt.savefig(rutaPDF)
