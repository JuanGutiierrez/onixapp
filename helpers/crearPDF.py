import pandas as pd
import matplotlib.pyplot as plt

from data.ventas import ventas

ventasDataFrame=pd.read_csv('data/ventas.csv')

filtroUno=ventasDataFrame.query("(Costo>=290000) and (Costo<=300000)")
totalventas=filtroUno[['NumeroOrden','Costo']]

#Graficando un DATAFRAME co MATLOTLIB
totalventas["NumeroOrden"]=totalventas["NumeroOrden"].astype(str)
colores=['#e36dec', '#f364dc','#ff5ccb','#ff55ba','#ff51a8','#ff4f96','#ff5185','#ff5573']
plt.figure(figsize=(10,10))
plt.bar(totalventas["NumeroOrden"],totalventas["Costo"], color=colores)

#Personalizando la grafica
plt.xlabel("NumeroOrden")
plt.ylabel("Costo")
plt.title("Ventas mas altas en ultimo mes")
plt.xticks(rotation=35)

rutaGrafica="assets/img/barrasventas.pdf"
plt.savefig(rutaGrafica)