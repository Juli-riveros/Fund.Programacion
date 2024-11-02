import streamlit as st

# Título del programa
st.title("Cálculo de la Serie: (1^1) + (2^2) + (3^3) + ... + (N^N)")

# Explicación del ejercicio
st.write("""
Este programa calcula la suma de la serie:
\((1^1) + (2^2) + (3^3) + \dots + (N^N)\) dado un número N.
""")

# Ingreso del valor de N
N = st.number_input("Ingrese un valor entero para N:", min_value=1, step=1)

# Calcular la serie
if N:
    suma = sum(i ** i for i in range(1, N + 1))

    # Mostrar el resultado
    st.subheader("Resultado:")
    st.write(f"La suma de la serie hasta (N^N) con N = {N} es: {suma}")
else:
    st.write("Por favor, ingrese un valor para N.")
