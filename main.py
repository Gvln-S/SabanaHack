import pandas as pd

datos = pd.read_excel("./sources/data.xlsx", header = None)
print(datos.head())
