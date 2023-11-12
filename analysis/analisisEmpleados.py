import pandas as pd

from helpers.crearCSVEmpleados import crearCSV
from data.empleados import empleados


print(empleados)

crearCSV(empleados, 'empleados.csv')

empleadosDataFrame=pd.read_csv('data/empleados.csv')
print(empleadosDataFrame)
