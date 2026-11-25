# ==========================================
# TIPO DE DATO: LIST
# ==========================================
# Una lista permite guardar varios valores.
# Las listas utilizan corchetes [].

frutas = ["manzana", "banana", "naranja"]

print("Lista:", frutas)
print("Tipo:", type(frutas))

# Acceder a un elemento
print("Primera fruta:", frutas[0])
print("Segunda fruta:", frutas[1])

# Agregar un elemento
frutas.append("mango")
print("Después de agregar:", frutas)

# Eliminar un elemento
frutas.remove("banana")
print("Después de eliminar:", frutas)

# Cantidad de elementos
print("Cantidad de frutas:", len(frutas))

# ==========================================
# EJERCICIO
# ==========================================
animales = ["perro", "gato", "caballo"]

print("Mi animal favorito es:", animales[0])
