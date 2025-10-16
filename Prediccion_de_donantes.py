import pandas
pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('display.max_colwidth', None)
pandas.set_option('display.width', None) 

df=pandas.read_csv("donantes.csv",sep=";")

print("Datos cargados correctamente")
print(df.to_string())

df["prediccion"] = df.apply(
    lambda fila: "Probablemente volvera a donar"
    if fila["dias_desde"]<180 and fila["frecuencia_12m"]>=2
    else "Probablemente no volvera a donar",
    axis=1
)


print("-------------RESULTADOS DE PREDICCION--------------")
print(df[["nombre", "dias_desde", "frecuencia_12m", "volumen_total_ml", "prediccion"]])

