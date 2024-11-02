import streamlit as st

# Título del proyecto
st.title("Cálculo de pagos mensuales y total después de 20 meses")

# Parámetros iniciales
primer_pago = 10
numero_meses = 20

# Cálculo de pagos mensuales y total
pagos_mensuales = [primer_pago * (2 ** (mes - 1)) for mes in range(1, numero_meses + 1)]
total_pagado = sum(pagos_mensuales)

# Mostrar los pagos de cada mes y el total
st.subheader("Pagos mensuales:")
for mes, pago in enumerate(pagos_mensuales, start=1):
    st.write(f"Mes {mes}: S/{pago}")

st.subheader("Total pagado después de 20 meses:")
st.write(f"S/{total_pagado}")
