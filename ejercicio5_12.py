import streamlit as st

# Título del programa
st.title("Calcular Aprobados, Desaprobados y Promedio de Notas")

# Explicación del ejercicio
st.write("""
Este programa permite ingresar N notas de un estudiante y calcula:
- El número de notas aprobadas y desaprobadas.
- El promedio de todas las notas.
""")

# Ingreso de las notas
num_notas = st.number_input("Ingrese la cantidad de notas (N):", min_value=1, step=1)
notas = []

# Solicitar al usuario ingresar las notas
for i in range(num_notas):
    nota = st.number_input(f"Ingrese la nota {i + 1}:", min_value=0, max_value=20, step=1)
    notas.append(nota)

# Calculo de aprobados, desaprobados y promedio
if notas:
    aprobados = sum(1 for nota in notas if nota >= 11)
    desaprobados = sum(1 for nota in notas if nota < 11)
    promedio = sum(notas) / len(notas)

    # Mostrar los resultados
    st.subheader("Resultados:")
    st.write(f"Total de notas aprobadas: {aprobados}")
    st.write(f"Total de notas desaprobadas: {desaprobados}")
    st.write(f"Promedio de todas las notas: {promedio:.2f}")
else:
    st.write("Por favor, ingrese las notas.")
