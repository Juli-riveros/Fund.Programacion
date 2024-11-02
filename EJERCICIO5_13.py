import streamlit as st

# Título del proyecto
st.title("Cálculo de pagos mensuales y total después de 20 meses")

# Explicación del ejercicio
st.write("""
Una persona adquirió un producto a pagar en 20 meses. 
El primer mes pagó S/10, el segundo S/20, el tercero S/40, y así sucesivamente.
Este programa calculará cuánto debe pagar mensualmente y el total después de 20 meses.
""")

# Variables iniciales
primer_pago = 10
numero_meses = 20

# Lista para almacenar los pagos de cada mes
pagos_mensuales = []

# Calcular los pagos mensuales
pago_actual = primer_pago
for mes in range(1, numero_meses + 1):
    pagos_mensuales.append(pago_actual)
    pago_actual *= 2  # duplicar el pago cada mes

# Calcular el total pagado después de 20 meses
total_pagado = sum(pagos_mensuales)

# Mostrar los resultados
st.subheader("Pagos mensuales:")
for mes, pago in enumerate(pagos_mensuales, start=1):
    st.write(f"Mes {mes}: S/{pago}")

st.subheader("Total pagado después de 20 meses:")
st.write(f"S/{total_pagado}")
