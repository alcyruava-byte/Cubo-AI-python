# ==========================================
# TEMA: LOOP / BUCLES
# ==========================================
# Un loop permite repetir instrucciones.
# Uno de los principales es for.

# 1. FOR CON RANGE
for numero in range(1, 6):
    print(numero)

# 2. RECORRER UNA LISTA
frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print("Fruta:", fruta)

# 3. FOR CON CONDICIONAL
for numero in range(1, 11):
    if numero % 2 == 0:
        print(numero, "es par.")
    else:
        print(numero, "es impar.")

# EJERCICIO
for numero in range(1, 6):
    print("Estoy aprendiendo Python:", numero)
