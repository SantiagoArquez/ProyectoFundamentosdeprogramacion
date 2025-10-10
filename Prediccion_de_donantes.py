import pandas as pd

df=pd.read_csv("donantes.csv",sep=";")

print("Datos cargados correctamente")
print(df.head())

def predecir_donacion(dias_desde,frecuencia_12m):
    if dias_desde<180 and frecuencia_12m>=2:
        print("Probablemente vuelva a donar")
    else:
        print("Probablemente no vuelva a donar")
