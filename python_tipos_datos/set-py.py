# ==========================================
# TIPO DE DATO: SET
# ==========================================
# Un set guarda varios valores.
# No permite elementos duplicados.
# Se escribe utilizando llaves {}.

numeros = {1, 2, 3, 4, 4, 5}

print("Set:", numeros)
print("Tipo:", type(numeros))

# Agregar un elemento
numeros.add(6)
print("Después de agregar:", numeros)

# Eliminar un elemento
numeros.remove(2)
print("Después de eliminar:", numeros)

# Comprobar si existe un elemento
if 3 in numeros:
    print("El número 3 está en el set.")

# ==========================================
# EJERCICIO
# ==========================================
frutas = {"manzana", "banana", "manzana", "naranja"}

print("Frutas sin duplicados:", frutas)
