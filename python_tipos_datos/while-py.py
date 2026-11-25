# ==========================================
# TEMA: WHILE
# ==========================================
# while repite código mientras una condición
# sea verdadera.

contador = 1

while contador <= 5:
    print("Contador:", contador)
    contador = contador + 1

# 2. WHILE CON CONDICIONAL
numero = 1

while numero <= 10:
    if numero % 2 == 0:
        print(numero, "es par.")
    else:
        print(numero, "es impar.")
    numero += 1

# 3. WHILE CON INPUT
respuesta = ""

while respuesta != "salir":
    respuesta = input("Escribe 'salir' para terminar: ")

print("Programa terminado.")

# EJERCICIO
contador = 5

while contador > 0:
    print("Faltan", contador)
    contador -= 1

print("¡Terminamos!")
