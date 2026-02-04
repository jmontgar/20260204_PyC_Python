import streamlit as st
import sys
import io
import contextlib
import random
import numpy as np
import matplotlib.pyplot as plt

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Python 2º Bach - Prácticas", layout="wide", page_icon="🐍")

# --- ESTILOS CSS ---
st.markdown("""
<style>
    .stTextArea textarea { font-family: 'Consolas', monospace; font-size: 14px; }
</style>
""", unsafe_allow_html=True)

# --- FUNCIÓN SANDBOX ---
def ejecutar_codigo(codigo_usuario):
    buffer = io.StringIO()
    plt.clf()
    fig = plt.figure()
    
    with contextlib.redirect_stdout(buffer):
        try:
            local_scope = {"random": random, "np": np, "plt": plt}
            exec(codigo_usuario, {}, local_scope)
            
            if len(plt.gcf().axes) > 0:
                return fig, "plot"
            return buffer.getvalue(), "success"
        except Exception as e:
            return f"⚠️ Error: {e}", "error"

# --- BARRA LATERAL ---
st.sidebar.title("📚 Temario")
tema = st.sidebar.radio("Ir a:", 
    ["1. Condicionales (If/Else)", 
     "2. Bucles (While/For)", 
     "3. Funciones y Modularidad"])

st.sidebar.info("💡 **Nota sobre `input()`:** En este simulador web no podemos detener el programa para pedir datos. En su lugar, **declara variables** al inicio del código para simular la entrada del usuario.")

# ==========================================
# TEMA 1: CONDICIONALES
# ==========================================
if tema == "1. Condicionales (If/Else)":
    st.header("1. Estructuras de Control Condicionales")
    
    # Selector de ejercicios
    ejercicio = st.selectbox("Selecciona la actividad:", [
        "1. Mayor de edad (Solo IF)",
        "2. Menor de edad (IF / ELSE)",
        "3. Etapas de la vida (ELIF)",
        "4. Condiciones Encadenadas (AND / OR)",
        "5. Pedir edad al usuario (Simulado)",
        "6. IF Anidados (Carnet de conducir)",
        "7. El mayor de 3 números"
    ])

    st.markdown("---")

    codigo_inicial = ""
    enunciado = ""

    if ejercicio == "1. Mayor de edad (Solo IF)":
        enunciado = "Comprueba si la variable `edad` es mayor o igual a 18. Si lo es, imprime 'Es mayor de edad'. (No hagas nada si es menor)."
        codigo_inicial = "edad = 19\n\nif edad >= 18:\n    # Tu código aquí\n    pass"

    elif ejercicio == "2. Menor de edad (IF / ELSE)":
        enunciado = "Si es menor de 18 imprime 'Es menor', si no, imprime 'Es mayor'."
        codigo_inicial = "edad = 15\n\nif edad < 18:\n    print(\"Es menor\")\nelse:\n    # Tu código aquí\n    pass"

    elif ejercicio == "3. Etapas de la vida (ELIF)":
        enunciado = "Clasifica: <12 'Niño', <18 'Adolescente', <65 'Adulto', resto 'Jubilado'."
        codigo_inicial = "edad = 45\n\nif edad < 12:\n    print(\"Niño\")\nelif edad < 18:\n    print(\"Adolescente\")\n# Completa el resto..."

    elif ejercicio == "4. Condiciones Encadenadas (AND / OR)":
        enunciado = "Para entrar VIP se necesita: ser mayor de 18 **Y** tener entrada VIP. O bien, conocer al dueño (variable `conoce_dueno`)."
        codigo_inicial = "edad = 20\ntiene_vip = False\nconoce_dueno = True\n\n# Usa and / or\nif (edad >= 18 and tiene_vip) or conoce_dueno:\n    print(\"Entra al VIP\")\nelse:\n    print(\"Fuera\")"

    elif ejercicio == "5. Pedir edad al usuario (Simulado)":
        enunciado = "**IMPORTANTE:** En web no funciona `input()`. Simulamos que el usuario escribe cambiando la variable `entrada_usuario`."
        codigo_inicial = "# Simulamos: edad = int(input('Dime tu edad'))\nentrada_usuario = \"25\" # Cambia este valor para probar\n\nedad = int(entrada_usuario)\n\nif edad >= 18:\n    print(f\"Tienes {edad} años, eres mayor.\")"

    elif ejercicio == "6. IF Anidados (Carnet de conducir)":
        enunciado = "Primero mira si tiene 18 años. SI LOS TIENE, mira si tiene carnet. Si no tiene 18, di que es muy joven."
        codigo_inicial = "edad = 19\ntiene_carnet = False\n\nif edad >= 18:\n    print(\"Tienes edad...\")\n    # IF ANIDADO AQUÍ\n    if tiene_carnet:\n        print(\"Puedes conducir\")\n    else:\n        print(\"Te falta el carnet\")\nelse:\n    print(\"Eres muy joven\")"

    elif ejercicio == "7. El mayor de 3 números":
        enunciado = "Dadas tres variables n1, n2, n3, imprime cuál es el número más grande."
        codigo_inicial = "n1 = 10\nn2 = 50\nn3 = 20\n\nif n1 > n2 and n1 > n3:\n    print(f\"El mayor es {n1}\")\nelif n2 > n1 and n2 > n3:\n    print(f\"El mayor es {n2}\")\nelse:\n    print(f\"El mayor es {n3}\")"

    st.info(f"📝 **Tarea:** {enunciado}")
    texto_codigo = st.text_area("Editor:", value=codigo_inicial, height=250)
    
    if st.button("▶️ Ejecutar"):
        res, tipo = ejecutar_codigo(texto_codigo)
        st.code(res) if tipo == "success" else st.error(res)


# ==========================================
# TEMA 2: BUCLES
# ==========================================
elif tema == "2. Bucles (While/For)":
    st.header("2. Bucles e Iteraciones")
    
    tipo_bucle = st.radio("Tipo de bucle:", ["Bucle WHILE", "Bucle FOR"], horizontal=True)
    
    if tipo_bucle == "Bucle WHILE":
        ejercicio = st.selectbox("Ejercicios While:", [
            "1. Números del 0 al 10",
            "2. Imprimir 15 números",
            "3. Imprimir 15 números pares",
            "4. Menú de calculadora (Salir con 0)"
        ])
        
        codigo_inicial = ""
        if ejercicio == "1. Números del 0 al 10":
            codigo_inicial = "i = 0\nwhile i <= 10:\n    print(i)\n    i = i + 1"
        elif ejercicio == "2. Imprimir 15 números":
            codigo_inicial = "contador = 1\nwhile contador <= 15:\n    print(f\"Número: {contador}\")\n    contador += 1"
        elif ejercicio == "3. Imprimir 15 números pares":
            codigo_inicial = "contador = 0\npares_encontrados = 0\n\nwhile pares_encontrados < 15:\n    if contador % 2 == 0:\n        print(contador)\n        pares_encontrados += 1\n    contador += 1"
        elif ejercicio == "4. Menú de calculadora (Salir con 0)":
            codigo_inicial = "# Simulamos un menú que se repite 3 veces para no colgar la web\nintentos = 0\nopcion = 1\n\nwhile opcion != 0 and intentos < 5:\n    print(\"--- MENÚ ---\")\n    print(\"1. Sumar\")\n    print(\"0. Salir\")\n    \n    # Simulamos que el usuario elige 1, luego 1, luego 0\n    if intentos < 2: \n        opcion = 1\n        print(\"Usuario elige: 1\")\n    else: \n        opcion = 0\n        print(\"Usuario elige: 0\")\n        \n    if opcion == 1:\n        print(\"Sumando...\")\n    elif opcion == 0:\n        print(\"Adiós\")\n    \n    intentos += 1"

    else: # Bucle FOR
        ejercicio = st.selectbox("Ejercicios For:", [
            "1. Los 10 primeros números",
            "2. Hasta número dado por usuario",
            "3. Desde... Hasta... (Usuario)",
            "4. Saltando de 2 en 2",
            "5. Buscar valor en lista (Break)",
            "6. Recorrer dos listas a la vez"
        ])
        
        codigo_inicial = ""
        if ejercicio == "1. Los 10 primeros números":
            codigo_inicial = "for i in range(1, 11):\n    print(i)"
        elif ejercicio == "2. Hasta número dado por usuario":
            codigo_inicial = "limite = 8 # Simula input\nfor i in range(limite):\n    print(i)"
        elif ejercicio == "3. Desde... Hasta... (Usuario)":
            codigo_inicial = "inicio = 5\nfin = 12\nfor i in range(inicio, fin + 1):\n    print(i)"
        elif ejercicio == "4. Saltando de 2 en 2":
            codigo_inicial = "# range(inicio, fin, salto)\nfor i in range(0, 21, 2):\n    print(i)"
        elif ejercicio == "5. Buscar valor en lista (Break)":
            codigo_inicial = "lista = [10, 50, 33, 90, 20]\nbuscado = 33\n\nfor numero in lista:\n    print(f\"Mirando el {numero}...\")\n    if numero == buscado:\n        print(\"¡ENCONTRADO!\")\n        break # Termina el bucle al encontrarlo"
        elif ejercicio == "6. Recorrer dos listas a la vez":
            codigo_inicial = "alumnos = [\"Ana\", \"Luis\", \"Eva\"]\nnotas = [8, 5, 9]\n\n# zip une las dos listas\nfor alumno, nota in zip(alumnos, notas):\n    print(f\"{alumno} ha sacado un {nota}\")"

    st.write("---")
    texto_codigo = st.text_area("Editor:", value=codigo_inicial, height=250)
    if st.button("▶️ Ejecutar Bucle"):
        res, tipo = ejecutar_codigo(texto_codigo)
        st.code(res)


# ==========================================
# TEMA 3: FUNCIONES
# ==========================================
elif tema == "3. Funciones y Modularidad":
    st.header("3. Funciones y Proyecto Cine")
    
    ejercicio = st.selectbox("Actividad:", [
        "1. Función Suma (parámetros)",
        "2. Función Menú (print)",
        "3. PROYECTO: Gestión de Butacas"
    ])

    codigo_inicial = ""
    
    if ejercicio == "1. Función Suma (parámetros)":
        codigo_inicial = "def sumar(a, b):\n    resultado = a + b\n    return resultado\n\n# Llamada a la función\nn1 = 10\nn2 = 35\ntotal = sumar(n1, n2)\nprint(f\"La suma es {total}\")"
        
    elif ejercicio == "2. Función Menú (print)":
        codigo_inicial = "def mostrar_menu():\n    print(\"1. Calcular\")\n    print(\"2. Ver resultados\")\n    print(\"3. Configuración\")\n    print(\"4. Salir\")\n\nprint(\"Bienvenido...\")\nmostrar_menu() # Llamada simple"
        
    elif ejercicio == "3. PROYECTO: Gestión de Butacas":
        st.info("ℹ️ **Reto:** Completa las funciones para mostrar qué butacas están libres (0) y reservarlas (1).")
        codigo_inicial = """# 0 = Libre, 1 = Ocupada
butacas = [0, 0, 1, 0, 0] 

def mostrar_butacas():
    print("Estado de la sala:")
    for i in range(len(butacas)):
        if butacas[i] == 0:
            estado = "LIBRE"
        else:
            estado = "OCUPADA"
        print(f"Butaca {i}: {estado}")

def reservar(numero_butaca):
    # Comprueba si está libre (0)
    if butacas[numero_butaca] == 0:
        butacas[numero_butaca] = 1
        print(f"✅ Butaca {numero_butaca} reservada con éxito.")
    else:
        print(f"❌ La butaca {numero_butaca} ya está ocupada.")

# --- PRUEBAS ---
mostrar_butacas()
print("\\n--- Intentando reservar la 1 ---")
reservar(1)
print("\\n--- Intentando reservar la 2 (ya ocupada) ---")
reservar(2)
print("\\n")
mostrar_butacas()"""

    texto_codigo = st.text_area("Editor:", value=codigo_inicial, height=350)
    if st.button("▶️ Ejecutar Función"):
        res, tipo = ejecutar_codigo(texto_codigo)
        st.code(res) if tipo == "success" else st.error(res)
