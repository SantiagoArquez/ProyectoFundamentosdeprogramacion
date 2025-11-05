import pandas as pd
import streamlit as st

st.title("Sistema de Predicción de Donantes")

archivo = st.file_uploader("Sube el archivo donantes.csv", type=["csv"])

if archivo is not None:
    df = pd.read_csv(archivo, sep=";")
    
    st.subheader("Datos cargados")
    st.dataframe(df)

    df["prediccion"] = df.apply(
        lambda fila: "Probablemente volvera a donar"
        if fila["dias_desde"] < 180 and fila["frecuencia_12m"] >= 2
        else "Probablemente no volvera a donar",
        axis=1
    )

    st.subheader("Resultados de Predicción")
    st.dataframe(df[["nombre", "dias_desde", "frecuencia_12m", "volumen_total_ml", "prediccion"]])

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Descargar resultados", csv, "resultado_predicciones.csv")
