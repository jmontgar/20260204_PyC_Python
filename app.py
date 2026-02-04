import streamlit as st
import sys
import io
import contextlib
import random
import numpy as np
import matplotlib.pyplot as plt

# --- CONFIGURACIÓN GLOBAL ---
st.set_page_config(page_title="Curso Python 2º Bach", layout="wide", page_icon="🐍")

# --- ESTILOS CSS (Para que el editor de código se vea mejor) ---
st.markdown("""
<style>
    .stTextArea textarea { font-family: 'Consolas', monospace; font-size: 14px; background-color: #f0f2f6; }
</style>
""", unsafe_allow_html=True)

# --- MOTOR DE EJECUCIÓN (SANDBOX HÍBRIDO TEXTO/GRÁFICOS) ---
def ejecutar_codigo(codigo_usuario):
    buffer = io.StringIO()
    # Limpiamos gráficas anteriores
    plt.clf()
    fig = plt.figure()
    
    with contextlib.redirect_stdout(buffer):
        try:
            # Entorno con librerías disponibles
            local_scope = {"random": random, "np": np, "plt": plt}
            exec(codigo_usuario, {}, local_scope)
            
            # Detectamos si se ha generado una gráfica
            if len(plt.gcf().axes) > 0:
                return fig, "plot"
            
            # Si no, devolvemos el texto
            return buffer.getvalue(), "success"
        except Exception as e:
            return f"⚠️ Error de ejecución: {e}", "error"

# --- BARRA LATERAL (MENÚ PRINCIPAL) ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg", width=80)
st.sidebar.title("📚 Temario 2º Bach")

seccion = st.sidebar.radio("Navegación:", 
    ["1. Introducción y Variables", 
     "2. Condicionales (If/Else)", 
     "3. Bucles (While/For)",
     "4. Listas y Colecciones",
     "5. Funciones y Proyectos",
     "6. Laboratorio Matemático (Gráficas)",
     "7. Reto Final Hacker"])

st.sidebar.markdown("---")
st.sidebar.info("💡 **Nota:** `input()` no funciona en web. Usa variables fijas para simular la entrada de datos.")

# ==============================================================================
# SECCIÓN 1: INTRODUCCIÓN
# ==============================================================================
if seccion == "1. Introducción y Variables":
    st.header("1. Variables y Tipos de Datos")
    st.markdown("🔗 **Teoría:** [W3Schools Variables](https://www.w3schools.com/python/python_variables.asp)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        Python detecta el tipo de dato automáticamente:
        * `int` (Enteros): `edad = 18`
        * `float` (Decimales): `media = 9.5`
        * `str` (Texto): `nombre = "Ana"`
        """)
    with col2:
        st.info("📝 **Práctica:** Define base y altura y calcula el área del triángulo.")
        codigo = st.text_area("Editor:", value="base = 10\naltura = 5\n# area = ...\nprint(area)", height=200)
        if st.button("▶️ Ejecutar Intro"):
            res, tipo = ejecutar_codigo(codigo)
            st.code(res) if tipo == "success" else st.error(res)

# ==============================================================================
# SECCIÓN 2: CONDICIONALES (AMPLIADO)
# ==============================================================================
elif seccion == "2. Condicionales (If/Else)":
    st.header("2. Lógica y Decisiones")
    st.markdown("🔗 **Teoría:** [W3Schools If...Else](https://www.w3schools.com/python/python_conditions.asp)")
    
    actividad = st.selectbox("Selecciona ejercicio:", [
        "1. Mayor de edad (Solo IF)",
        "2. Menor de edad (IF / ELSE)",
        "3. Etapas de la vida (ELIF)",
        "4. Condiciones Encadenadas (AND / OR)",
        "5. Pedir edad al usuario (Simulado)",
        "6. IF Anidados (Carnet de conducir)",
        "7. El mayor de 3 números"
    ])
    
    st.markdown("---")
    codigo_init = ""
    
    if "1." in actividad:
        st.write("**Enunciado:** Si `edad >= 18` imprime 'Mayor'.")
        codigo_init = "edad = 19\nif edad >= 18:\n    print('Es mayor')"
    elif "2." in actividad:
        st.write("**Enunciado:** Si `edad < 18` imprime 'Menor', si no 'Mayor'.")
        codigo_init = "edad = 15\nif edad < 18:\n    print('Menor')\nelse:\n    print('Mayor')"
    elif "3." in actividad:
        st.write("**Enunciado:** Clasifica en Niño (<12), Adolescente (<18) o Adulto.")
        codigo_init = "edad = 45\nif edad < 12:\n    print('Niño')\nelif edad < 18:\n    print('Adolescente')\nelse:\n    print('Adulto')"
    elif "4." in actividad:
        st.write("**Enunciado:** Entra si (Mayor 18 Y tiene entrada) O (Conoce al dueño).")
        codigo_init = "edad = 20\ntiene_entrada = False\nconoce_dueno = True\n\nif (edad >= 18 and tiene_entrada) or conoce_dueno:\n    print('Entra')\nelse:\n    print('Fuera')"
    elif "5." in actividad:
        st.write("**Truco:** Cambia la variable `entrada` para simular que escribes.")
        codigo_init = "entrada = '25' # Cambia esto\nedad = int(entrada)\nif edad >= 18:\n    print(f'Tienes {edad} años')"
    elif "6." in actividad:
        st.write("**Enunciado:** Primero comprueba edad. SI es mayor, comprueba carnet.")
        codigo_init = "edad = 19\ncarnet = False\nif edad >= 18:\n    if carnet:\n        print('Conduce')\n    else:\n        print('Te falta carnet')\nelse:\n    print('Muy joven')"
    elif "7." in actividad:
        st.write("**Enunciado:** Compara n1, n2 y n3 y di el mayor.")
        codigo_init = "n1, n2, n3 = 10, 50, 20\nif n1 > n2 and n1 > n3:\n    print(n1)\nelif n2 > n1 and n2 > n3:\n    print(n2)\nelse:\n    print(n3)"

    texto = st.text_area("Código:", value=codigo_init, height=250)
    if st.button("▶️ Ejecutar Condicional"):
        res, tipo = ejecutar_codigo(texto)
        st.code(res)

# ==============================================================================
# SECCIÓN 3: BUCLES (AMPLIADO)
# ==============================================================================
elif seccion == "3. Bucles (While/For)":
    st.header("3. Bucles e Iteraciones")
    st.markdown("🔗 **Teoría:** [While Loops](https://www.w3schools.com/python/python_while_loops.asp) | [For Loops](https://www.w3schools.com/python/python_for_loops.asp)")
    
    tipo_bucle = st.radio("Elige tipo:", ["WHILE (Mientras...)", "FOR (Para cada...)"], horizontal=True)
    
    codigo_init = ""
    
    if "WHILE" in tipo_bucle:
        actividad = st.selectbox("Ejercicios While:", [
            "1. Contar 0 al 10",
            "2. 15 números",
            "3. 15 números pares",
            "4. Menú Calculadora"
        ])
        if "1." in actividad: codigo_init = "i = 0\nwhile i <= 10:\n    print(i)\n    i += 1"
        if "2." in actividad: codigo_init = "c = 1\nwhile c <= 15:\n    print(c)\n    c += 1"
        if "3." in actividad: codigo_init = "c = 0\npares = 0\nwhile pares < 15:\n    if c % 2 == 0:\n        print(c)\n        pares += 1\n    c += 1"
        if "4." in actividad: codigo_init = "opcion = 1\nintentos = 0\nwhile opcion != 0 and intentos < 3:\n    print('1. Sumar | 0. Salir')\n    opcion = 0 # Simulamos salir\n    intentos += 1"
    
    else: # FOR
        actividad = st.selectbox("Ejercicios For:", [
            "1. 10 primeros números",
            "2. Hasta N (Usuario)",
            "3. Desde A hasta B",
            "4. De 2 en 2",
            "5. Buscar y romper (Break)",
            "6. Dos listas a la vez (Zip)"
        ])
        if "1." in actividad: codigo_init = "for i in range(1, 11):\n    print(i)"
        if "2." in actividad: codigo_init = "n = 8\nfor i in range(n):\n    print(i)"
        if "3." in actividad: codigo_init = "ini = 5\nfin = 10\nfor i in range(ini, fin+1):\n    print(i)"
        if "4." in actividad: codigo_init = "for i in range(0, 21, 2):\n    print(i)"
        if "5." in actividad: codigo_init = "lista = [10, 50, 90]\nbuscar = 50\nfor x in lista:\n    if x == buscar:\n        print('Encontrado')\n        break"
        if "6." in actividad: codigo_init = "nombres = ['Ana', 'Luis']\nnotas = [8, 5]\nfor nom, nota in zip(nombres, notas):\n    print(f'{nom}: {nota}')"

    texto = st.text_area("Código:", value=codigo_init, height=250)
    if st.button("▶️ Ejecutar Bucle"):
        res, tipo = ejecutar_codigo(texto)
        st.code(res)

# ==============================================================================
# SECCIÓN 4: LISTAS (VISUAL)
# ==============================================================================
elif seccion == "4. Listas y Colecciones":
    st.header("4. Listas (Arrays)")
    
    col1, col2 = st.columns([1,1])
    with col1:
        st.markdown("**Mapa de Memoria:**")
        st.code("notas = [5, 8, 9, 4]\nIndices: 0  1  2  3")
    with col2:
        st.info("📝 **Ejercicio:** Añade un 10 a la lista y calcula la media.")
    
    codigo = st.text_area("Código:", value="notas = [5, 6, 8]\n# notas.append(10)\n# media = sum(notas) / len(notas)\nprint(notas)", height=200)
    if st.button("▶️ Ejecutar Listas"):
        res, tipo = ejecutar_codigo(codigo)
        st.code(res) if tipo == "success" else st.error(res)

# ==============================================================================
# SECCIÓN 5: FUNCIONES
# ==============================================================================
elif seccion == "5. Funciones y Proyectos":
    st.header("5. Funciones y Modularidad")
    
    actividad = st.selectbox("Actividad:", [
        "1. Suma simple (parámetros)",
        "2. Función Menú",
        "3. PROYECTO: Reserva de Butacas"
    ])
    
    codigo_init = ""
    if "1." in actividad:
        codigo_init = "def sumar(a, b):\n    return a + b\n\nprint(sumar(10, 5))"
    elif "2." in actividad:
        codigo_init = "def menu():\n    print('1. Jugar')\n    print('2. Salir')\n\nmenu()"
    elif "3." in actividad:
        st.warning("Completa la función reservar() para cambiar el 0 por 1.")
        codigo_init = """butacas = [0, 0, 1, 0] # 0 Libre, 1 Ocupada

def ver_sala():
    for i, estado in enumerate(butacas):
        texto = "LIBRE" if estado == 0 else "OCUPADA"
        print(f"Butaca {i}: {texto}")

def reservar(n):
    if butacas[n] == 0:
        butacas[n] = 1
        print("Reservada!")
    else:
        print("Ya estaba ocupada")

ver_sala()
print("--- Reservando la 0 ---")
reservar(0)
ver_sala()"""

    texto = st.text_area("Código:", value=codigo_init, height=300)
    if st.button("▶️ Ejecutar Función"):
        res, tipo = ejecutar_codigo(texto)
        st.code(res)

# ==============================================================================
# SECCIÓN 6: GRÁFICAS MATEMÁTICAS
# ==============================================================================
elif seccion == "6. Laboratorio Matemático (Gráficas)":
    st.header("📈 Laboratorio: NumPy y Matplotlib")
    st.markdown("Genera gráficas de funciones continuas.")
    
    

    st.info("📝 **Reto:** Dibuja Seno (azul) y Coseno (rojo) entre 0 y 4π.")
    
    codigo = """# 1. Crear datos del eje X
x = np.linspace(0, 4*np.pi, 100)

# 2. Calcular eje Y
y_sen = np.sin(x)
y_cos = np.cos(x)

# 3. Dibujar
plt.plot(x, y_sen, color='blue', label='Seno')
# Descomenta la siguiente línea:
# plt.plot(x, y_cos, color='red', label='Coseno')

plt.legend()
plt.grid()
plt.title("Funciones Trigonométricas")
"""
    texto = st.text_area("Editor Gráfico:", value=codigo, height=350)
    
    if st.button("▶️ Generar Gráfica"):
        res, tipo = ejecutar_codigo(texto)
        if tipo == "plot":
            st.pyplot(res)
        elif tipo == "error":
            st.error(res)
        else:
            st.warning("El código corrió, pero no generó gráfica (falta plt.plot)")
            st.code(res)

# ==============================================================================
# SECCIÓN 7: RETO FINAL
# ==============================================================================
elif seccion == "7. Reto Final Hacker":
    st.header("🏆 Generador de Contraseñas")
    st.write("Usa `random.choice()` para crear una password segura de 8 caracteres.")
    
    codigo = """import random
letras = "abcdefghijk123456789!@"
password = ""

for i in range(8):
    # Tu código aquí
    pass

print(password)"""
    
    texto = st.text_area("Editor Hacker:", value=codigo, height=200)
    if st.button("▶️ Generar"):
        res, tipo = ejecutar_codigo(texto)
        st.code(res)
