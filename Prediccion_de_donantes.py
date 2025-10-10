import pandas as pd

df=pd.read_csv("donantes.csv",sep=";")

print("Datos cargados correctamente")
print(df.head())

def predecir_donacion(frecuencia_dias,frecuencia_12m):
    if frecuencia_dias<180 and frecuencia_12m>=2:
        print("Probablemente vuelva a donar")
    else:
        print("Probablemente no vuelva a donar")
