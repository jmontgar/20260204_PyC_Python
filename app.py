import streamlit as st
import sys
import io
import contextlib
import random
# --- NUEVOS IMPORTS PARA GRÁFICAS ---
import numpy as np
import matplotlib.pyplot as plt

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Curso Python 2º Bach", layout="wide", page_icon="🐍")

# --- FUNCIÓN SANDBOX MEJORADA (Soporta texto y gráficas) ---
def ejecutar_codigo(codigo_usuario):
    buffer = io.StringIO()
    # Creamos una nueva figura limpia para evitar que se superpongan gráficas anteriores
    plt.clf()
    fig = plt.figure()
    
    with contextlib.redirect_stdout(buffer):
        try:
            # --- MODIFICACIÓN CLAVE: Pasamos las librerías al entorno del alumno ---
            local_scope = {
                "random": random,
                "np": np,   # El alumno podrá usar 'np.'
                "plt": plt  # El alumno podrá usar 'plt.'
            }
            exec(codigo_usuario, {}, local_scope)
            
            # --- DETECCIÓN DE RESULTADO ---
            # Verificamos si se ha dibujado algo en los ejes de la figura actual
            if len(plt.gcf().axes) > 0:
                return fig, "plot" # Devolvemos la imagen
            else:
                # Si no hay gráfica, devolvemos el texto estándar
                resultado = buffer.getvalue()
                return resultado, "success"
                
        except Exception as e:
            return f"⚠️ Error: {e}", "error"

# --- BARRA LATERAL ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg", width=100)
st.sidebar.title("📚 Temario 2º Bach")
opcion = st.sidebar.radio("Navegación:", 
    ["1. Variables y Datos", 
     "2. Condicionales (If/Else)", 
     "3. Bucles (For Loops)",
     "4. Listas y Colecciones",
     "5. Funciones",
     "6. Gráficas Matemáticas (NUEVO)",
     "7. Reto Final"])

st.sidebar.markdown("---")
st.sidebar.info("💡 **Consejo:** Usa la documentación de W3Schools si te atascas.")

# --- CONTENIDO PRINCIPAL ---
st.title("🐍 Entorno de Programación Python")

# === TEMA 1: VARIABLES ===
if opcion == "1. Variables y Datos":
    st.header("1. Variables y Tipos de Datos")
    st.markdown("🔗 **Doc:** [W3Schools - Variables](https://www.w3schools.com/python/python_variables.asp)")
    col1, col2 = st.columns(2)
    with col1:
        st.code('nombre = "Ana" # str\nedad = 17     # int\nnota = 8.5    # float')
    with col2:
        st.info("📝 **Ejercicio:** Calcula el área de un triángulo (base 10, altura 5).")
        codigo = st.text_area("Código:", value="base = 10\naltura = 5\n# area = ...\nprint(area)")
        if st.button("▶️ Ejecutar"):
            res, estado = ejecutar_codigo(codigo)
            st.code(res) if estado == "success" else st.error(res)

# === TEMA 2: CONDICIONALES ===
elif opcion == "2. Condicionales (If/Else)":
    st.header("2. Lógica Booleana")
    st.markdown("🔗 **Doc:** [W3Schools - If...Else](https://www.w3schools.com/python/python_conditions.asp)")
    st.info("📝 **Ejercicio:** Imprime 'Aprobado' si la nota es >= 5, si no 'Suspenso'.")
    codigo = st.text_area("Código:", value="nota = 4.9\nif nota >= 5:\n    print('Aprobado')\nelse:\n    # ...")
    if st.button("▶️ Ejecutar"):
        res, estado = ejecutar_codigo(codigo)
        st.code(res) if estado == "success" else st.error(res)

# === TEMA 3: BUCLES ===
elif opcion == "3. Bucles (For Loops)":
    st.header("3. Bucles For")
    st.markdown("🔗 **Doc:** [W3Schools - For Loops](https://www.w3schools.com/python/python_for_loops.asp)")
    st.info("📝 **Ejercicio:** Suma los números del 1 al 100 usando un bucle.")
    codigo = st.text_area("Código:", value="suma = 0\nfor i in range(1, 101):\n    suma = suma + i\nprint(suma)")
    if st.button("▶️ Ejecutar"):
        res, estado = ejecutar_codigo(codigo)
        st.code(res)

# === TEMA 4: LISTAS ===
elif opcion == "4. Listas y Colecciones":
    st.header("4. Listas (Arrays)")
    st.markdown("🔗 **Doc:** [W3Schools - Lists](https://www.w3schools.com/python/python_lists.asp)")
    st.info("📝 **Ejercicio:** Dada la lista, añade el 10 y calcula la media.")
    codigo = st.text_area("Código:", value="notas = [5, 8, 4]\n# notas.append(10)\n# media = sum(notas) / len(notas)\nprint(media)")
    if st.button("▶️ Ejecutar"):
        res, estado = ejecutar_codigo(codigo)
        st.code(res) if estado == "success" else st.error(res)

# === TEMA 5: FUNCIONES ===
elif opcion == "5. Funciones":
    st.header("5. Funciones (def)")
    st.markdown("🔗 **Doc:** [W3Schools - Functions](https://www.w3schools.com/python/python_functions.asp)")
    st.info("📝 **Ejercicio:** Crea una función que reciba un precio sin IVA y devuelva el precio final (IVA 21%).")
    codigo = st.text_area("Código:", value="def calcular_iva(precio):\n    return precio * 1.21\n\nprint(calcular_iva(100))")
    if st.button("▶️ Ejecutar"):
        res, estado = ejecutar_codigo(codigo)
        st.code(res)

# === TEMA 6: GRÁFICAS MATEMÁTICAS (NUEVO) ===
elif opcion == "6. Gráficas Matemáticas (NUEVO)":
    st.header("📈 6. Visualización Matemática con Matplotlib")
    
    st.markdown("""
    En Bachillerato trabajáis con funciones continuas ($y = \sin(x)$). Los ordenadores no entienden "continuo", entienden puntos discretos.
    
    Para graficar, necesitamos dos herramientas profesionales:
    1.  **NumPy (`np`):** Para crear miles de puntos en el eje X.
    2.  **Matplotlib (`plt`):** Para unir esos puntos con líneas.
    """)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("##### Concepto Clave: `np.linspace`")
        st.code("""
import numpy as np
# Crea 100 puntos entre 0 y 10
x = np.linspace(0, 10, 100)
        """)
        st.caption("Esto genera una lista gigante de números: `[0.0, 0.1, 0.2 ... 10.0]`")

    with col2:
        st.markdown("##### Concepto Clave: `plt.plot`")
        st.code("""
import matplotlib.pyplot as plt
y = x**2  # Calcula Y para cada X
plt.plot(x, y) # Dibuja la línea
plt.show()
        """)

    st.markdown("---")
    st.info("📝 **Ejercicio: Ondas Trigonométricas**")
    st.write("""
    **Objetivo:** Dibuja en la misma gráfica la función **Seno (en azul)** y la función **Coseno (en rojo)**.
    * El eje X debe ir desde $0$ hasta $4\pi$ (dos vueltas completas).
    * Usa `np.sin(x)` y `np.cos(x)`.
    * Usa `plt.plot(x, y, color='blue')` para elegir colores.
    """)
    
    # Código boilerplate para ayudarles a empezar
    codigo_inicial = """# Importamos las librerías necesarias (ya están disponibles)
# import numpy as np
# import matplotlib.pyplot as plt

# 1. DEFINIR EL EJE X
# Generamos 200 puntos entre 0 y 4*pi
x = np.linspace(0, 4 * np.pi, 200)

# 2. CALCULAR LOS EJES Y
y_seno = np.sin(x)
# y_coseno = ... (complétalo tú)

# 3. DIBUJAR
plt.figure(figsize=(10,4)) # Hacemos la gráfica más ancha
plt.plot(x, y_seno, label='Seno', color='blue')
# plt.plot(...) # Dibuja aquí el coseno en rojo

# Añadimos detalles
plt.title("Funciones Trigonométricas")
plt.legend() # Muestra las etiquetas
plt.grid(True) # Añade cuadrícula
"""
    codigo = st.text_area("Editor de Gráficas:", height=400, value=codigo_inicial)
    
    if st.button("▶️ Generar Gráfica"):
        # --- LÓGICA DIFERENTE PARA GRÁFICAS ---
        res, estado = ejecutar_codigo(codigo)
        if estado == "plot":
            st.success("¡Gráfica generada con éxito!")
            st.pyplot(res) # Aquí es donde Streamlit dibuja la imagen
        elif estado == "success":
             st.warning("El código se ejecutó, pero no has usado plt.plot() para dibujar nada.")
             st.code(res)
        else:
            st.error(res)


# === RETO FINAL ===
elif opcion == "7. Reto Final":
    st.header("🏆 Reto Final")
    st.info("Generador de contraseñas aleatorias (Usa el módulo `random`).")
    codigo = st.text_area("Código:", value="import random\nletras = 'abcdef123456'\n# Usa random.choice(letras) en un bucle")
    if st.button("▶️ Ejecutar"):
        res, estado = ejecutar_codigo(codigo)
        st.code(res) if estado == "success" else st.error(res)
