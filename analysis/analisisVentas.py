import pandas as pd

from helpers.crearVentasCSV import crearCSV
from helpers.crearTablasHTML import crearTabla
from data.ventas import ventas
from helpers.crearGraficas import imgGraficar
from helpers.crearArchivosPDF import pdfGraficar

#1 Crear un CSV con los datos de las ventas
crearCSV(ventas, 'ventas.csv')

#2 cargo la fuente de datos y con PANDAS creo un DATAFRAME
ventasDataFrame=pd.read_csv('data/ventas.csv')
pdfGraficar(ventasDataFrame, "assets/img/figuras/ventas.pdf")

# fig, ax = plt.subplots(figsize=(12,4))
# ax.axis('tight')
# ax.axis('off')
# the_table = ax.table(cellText=ventasDataFrame.values,colLabels=ventasDataFrame.columns,loc='center')

# pp= PdfPages("assets/img/figuras/ventasAltas.pdf")
# pp.savefig(fig,bbox_inches='tight')
# pp.close()


#4 filtrar y ordenar (limpiar)
ventasMayores=ventasDataFrame.query('Costo >= 600000')
filtroVentas=ventasMayores[['NumeroOrden','Costo']]


ventasAltas = ventasDataFrame.nlargest(10, "Costo")
ventasBajas = ventasDataFrame.nsmallest(5, "Costo")

#generando html con resultados del filtro
crearTabla(filtroVentas,'ventasAltoCosto')

imgGraficar(ventasAltas, "assets/img/figuras/ventasAltas.png","NumeroOrden","Costo","Numero de orden","Costo","Ventas más altas en el último mes")