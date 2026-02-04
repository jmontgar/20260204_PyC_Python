import streamlit as st
import sys
import io
import contextlib
import random
import numpy as np
import matplotlib.pyplot as plt

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Curso Python 2º Bach", layout="wide", page_icon="🐍")

# --- MOTOR DE EJECUCIÓN ---
def ejecutar_codigo(codigo_usuario):
    buffer = io.StringIO()
    plt.clf()
    fig = plt.figure()
    
    with contextlib.redirect_stdout(buffer):
        try:
            local_scope = {"random": random, "np": np, "plt": plt}
            exec(codigo_usuario, {}, local_scope)
            if len(plt.gcf().axes) > 0: return fig, "plot"
            return buffer.getvalue(), "success"
        except Exception as e:
            return f"⚠️ Error: {e}", "error"

# --- BARRA LATERAL ---
st.sidebar.title("📚 Temario 2º Bach")
seccion = st.sidebar.radio("Navegación:", 
    ["1. Introducción y Variables", 
     "2. Condicionales (If/Else)", 
     "3. Bucles (While/For)",
     "4. Listas y Colecciones",
     "5. Funciones y Proyectos",
     "6. Laboratorio Gráfico",
     "7. Reto Final Hacker"])

st.sidebar.markdown("---")
st.sidebar.info("💡 Escribe tu código en el editor y pulsa 'Ejecutar'.")

# ==============================================================================
# SECCIÓN 1: INTRODUCCIÓN
# ==============================================================================
if seccion == "1. Introducción y Variables":
    st.header("1. Variables y Operaciones")
    st.markdown("🔗 **Teoría:** [Variables](https://www.w3schools.com/python/python_variables.asp)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("📝 **Ejercicio:** Tienes la base y la altura. Calcula el área del triángulo e imprímela.")
        # PLANTILLA VACÍA
        codigo_plantilla = "base = 10\naltura = 5\n\n# 1. Crea una variable llamada 'area' y calcula (base*altura)/2\n\n# 2. Imprime el resultado\n"
        # SOLUCIÓN OCULTA
        solucion = "base = 10\naltura = 5\narea = (base * altura) / 2\nprint(area)"
    
    with col2:
        texto = st.text_area("Editor de Código:", value=codigo_plantilla, height=200)
        if st.button("▶️ Ejecutar"):
            res, tipo = ejecutar_codigo(texto)
            st.code(res) if tipo == "success" else st.error(res)
        
        with st.expander("👀 Ver Solución (¡Inténtalo antes!)"):
            st.code(solucion)

# ==============================================================================
# SECCIÓN 2: CONDICIONALES
# ==============================================================================
elif seccion == "2. Condicionales (If/Else)":
    st.header("2. Lógica y Decisiones")
    actividad = st.selectbox("Selecciona ejercicio:", [
        "1. Mayor de edad (If)",
        "2. Menor/Mayor (If/Else)",
        "3. Etapas vida (Elif)",
        "4. Discoteca VIP (And/Or)",
        "5. If Anidados (Carnet)"
    ])
    
    codigo_plantilla = ""
    solucion = ""
    
    if "1." in actividad:
        st.write("**Misión:** Si edad >= 18, imprime 'Es mayor'.")
        codigo_plantilla = "edad = 19\n\n# Escribe tu IF aquí abajo:\n"
        solucion = "edad = 19\nif edad >= 18:\n    print('Es mayor')"
        
    elif "2." in actividad:
        st.write("**Misión:** Si edad < 18 imprime 'Menor', si no 'Mayor'.")
        codigo_plantilla = "edad = 15\n\nif edad < 18:\n    pass # Borra esto y escribe tu print\nelse:\n    # Tu código aquí\n    pass"
        solucion = "edad = 15\nif edad < 18:\n    print('Menor')\nelse:\n    print('Mayor')"
        
    elif "3." in actividad:
        st.write("**Misión:** <12 Niño, <18 Adolescente, resto Adulto.")
        codigo_plantilla = "edad = 45\n\nif edad < 12:\n    print('Niño')\n# Añade aquí el elif y el else:\n"
        solucion = "edad = 45\nif edad < 12:\n    print('Niño')\nelif edad < 18:\n    print('Adolescente')\nelse:\n    print('Adulto')"
        
    elif "4." in actividad:
        st.write("**Misión:** Entra si (Mayor 18 Y entrada) O (Conoce dueño).")
        codigo_plantilla = "edad = 20\ntiene_entrada = False\nconoce_dueno = True\n\n# Completa la condición:\nif (__________) or _________:\n    print('Adentro')\nelse:\n    print('Fuera')"
        solucion = "if (edad >= 18 and tiene_entrada) or conoce_dueno:\n    print('Adentro')\nelse:\n    print('Fuera')"
        
    elif "5." in actividad:
        st.write("**Misión:** Comprueba edad. SI es mayor, comprueba carnet.")
        codigo_plantilla = "edad = 19\ncarnet = False\n\nif edad >= 18:\n    # Aquí dentro, pon OTRO if para el carnet\n    pass\nelse:\n    print('Muy joven')"
        solucion = "if edad >= 18:\n    if carnet:\n        print('Conduce')\n    else:\n        print('Sin carnet')\nelse:\n    print('Muy joven')"

    texto = st.text_area("Editor:", value=codigo_plantilla, height=250)
    if st.button("▶️ Ejecutar"):
        res, tipo = ejecutar_codigo(texto)
        st.code(res)
    
    with st.expander("👀 Ver Solución"):
        st.code(solucion)

# ==============================================================================
# SECCIÓN 3: BUCLES
# ==============================================================================
elif seccion == "3. Bucles (While/For)":
    st.header("3. Bucles")
    tipo = st.radio("Tipo:", ["WHILE", "FOR"], horizontal=True)
    
    codigo_plantilla = ""
    solucion = ""
    
    if "WHILE" in tipo:
        actividad = st.selectbox("Ejercicio:", ["1. Contar 0-10", "2. Pares hasta 15"])
        if "1." in actividad:
            codigo_plantilla = "i = 0\n# Escribe el while para que pare al llegar a 10\nwhile ______:\n    print(i)\n    # ¡No olvides incrementar i!"
            solucion = "i = 0\nwhile i <= 10:\n    print(i)\n    i += 1"
        else:
            codigo_plantilla = "c = 0\npares = 0\n# Debes encontrar 15 pares\nwhile pares < 15:\n    # Si c es par (c % 2 == 0)...\n    pass\n    c += 1"
            solucion = "c = 0\npares = 0\nwhile pares < 15:\n    if c % 2 == 0:\n        print(c)\n        pares += 1\n    c += 1"
    else:
        actividad = st.selectbox("Ejercicio:", ["1. Del 1 al 10", "2. Sumar lista"])
        if "1." in actividad:
            codigo_plantilla = "# Usa range(inicio, fin)\nfor i in ______:\n    print(i)"
            solucion = "for i in range(1, 11):\n    print(i)"
        else:
            codigo_plantilla = "precios = [10, 20, 30]\nsuma = 0\n\n# Recorre la lista y suma cada precio\nfor p in precios:\n    # Tu código\n    pass\nprint(suma)"
            solucion = "precios = [10, 20, 30]\nsuma = 0\nfor p in precios:\n    suma += p\nprint(suma)"

    texto = st.text_area("Editor:", value=codigo_plantilla, height=250)
    if st.button("▶️ Ejecutar"):
        res, tipo = ejecutar_codigo(texto)
        st.code(res)
    with st.expander("👀 Ver Solución"):
        st.code(solucion)

# ==============================================================================
# SECCIÓN 4: LISTAS
# ==============================================================================
elif seccion == "4. Listas y Colecciones":
    st.header("4. Listas")
    st.info("📝 **Ejercicio:** Añade el nº 10 a la lista y calcula la media.")
    
    codigo_plantilla = "notas = [5, 6, 8]\n\n# 1. Usa .append() para añadir un 10\n\n# 2. Calcula la media (suma / longitud)\n# Pista: usa sum(notas) y len(notas)\n"
    solucion = "notas = [5, 6, 8]\nnotas.append(10)\nmedia = sum(notas) / len(notas)\nprint(media)"
    
    texto = st.text_area("Editor:", value=codigo_plantilla, height=200)
    if st.button("▶️ Ejecutar"):
        res, tipo = ejecutar_codigo(texto)
        st.code(res) if tipo == "success" else st.error(res)
    with st.expander("👀 Ver Solución"):
        st.code(solucion)

# ==============================================================================
# SECCIÓN 5: FUNCIONES
# ==============================================================================
elif seccion == "5. Funciones y Proyectos":
    st.header("5. Funciones")
    actividad = st.selectbox("Reto:", ["1. Crear función Suma", "2. PROYECTO CINE"])
    
    if "1." in actividad:
        codigo_plantilla = "# Define una función llamada 'sumar' que reciba a y b\ndef _______(a, b):\n    # devuelve la suma\n    pass\n\n# Prueba tu función\nprint(sumar(5, 5))"
        solucion = "def sumar(a, b):\n    return a + b\nprint(sumar(5, 5))"
    else:
        st.warning("Completa la lógica para reservar (cambiar 0 por 1).")
        codigo_plantilla = """butacas = [0, 0, 1, 0] # 0=Libre, 1=Ocupada

def reservar(n):
    # Si la butaca butacas[n] es 0...
    if _________ == 0:
        # Cámbiala a 1
        print("Reservada")
    else:
        print("Ocupada")

reservar(0) # Debería funcionar
reservar(2) # Debería fallar"""
        solucion = "def reservar(n):\n    if butacas[n] == 0:\n        butacas[n] = 1\n        print('Reservada')\n    else:\n        print('Ocupada')"

    texto = st.text_area("Editor:", value=codigo_plantilla, height=300)
    if st.button("▶️ Ejecutar"):
        res, tipo = ejecutar_codigo(texto)
        st.code(res)
    with st.expander("👀 Ver Solución"):
        st.code(solucion)

# ==============================================================================
# SECCIÓN 6: GRÁFICAS
# ==============================================================================
elif seccion == "6. Laboratorio Gráfico":
    st.header("📈 Gráficas Matemáticas")
    st.markdown("Dibuja un seno y un coseno.")
    
    codigo_plantilla = """import numpy as np
import matplotlib.pyplot as plt

# 1. Datos del Eje X (de 0 a 4pi)
x = np.linspace(0, 4*np.pi, 100)

# 2. Datos Eje Y
y_seno = np.sin(x)
# y_coseno = ... (calcúlalo tú)

# 3. Dibujar
plt.plot(x, y_seno, label="Seno")
# plt.plot( ... ) # Dibuja el coseno aquí

plt.legend()
plt.grid()"""
    
    solucion = "y_coseno = np.cos(x)\nplt.plot(x, y_seno)\nplt.plot(x, y_coseno)"

    texto = st.text_area("Editor Gráfico:", value=codigo_plantilla, height=350)
    if st.button("▶️ Generar Gráfica"):
        res, tipo = ejecutar_codigo(texto)
        if tipo == "plot": st.pyplot(res)
        else: st.code(res)
    with st.expander("👀 Ver Solución (partes clave)"):
        st.code(solucion)

# ==============================================================================
# SECCIÓN 7: RETO HACKER
# ==============================================================================
elif seccion == "7. Reto Final Hacker":
    st.header("🏆 Generador de Passwords")
    
    codigo_plantilla = """import random
letras = "abcdef12345"
password = ""

# Crea un bucle que se repita 8 veces
for i in range(8):
    # Elige una letra al azar: random.choice(letras)
    # Añado la letra a password
    pass

print(password)"""
    
    solucion = "for i in range(8):\n    password += random.choice(letras)\nprint(password)"
    
    texto = st.text_area("Editor:", value=codigo_plantilla, height=250)
    if st.button("▶️ Generar"):
        res, tipo = ejecutar_codigo(texto)
        st.code(res)
    with st.expander("👀 Ver Solución"):
        st.code(solucion)
