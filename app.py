import streamlit as st
from backend import calcular_potencia

st.title("Calculadora de Potencia Eléctrica")

voltaje = st.number_input("Voltaje (V)", min_value=0.0, value=220.0)
corriente = st.number_input("Corriente (A)", min_value=0.0, value=5.0)

if st.button("Calcular"):
 potencia = calcular_potencia(voltaje, corriente)
 st.success(f"La potencia es: {potencia} W")