# ==========================================
# TIPO DE DATO: STRING (str)
# ==========================================
# Un string es texto. Se escribe entre comillas.

nombre = "Carlos"
pais = "El Salvador"
mensaje = "Hola, Python"

print(nombre)
print(pais)
print(mensaje)

print("Tipo de nombre:", type(nombre))

# Concatenar strings
nombre_completo = "Ana" + " " + "García"
print(nombre_completo)

# Longitud del texto
print("Cantidad de letras:", len(nombre))

# Convertir texto a mayúsculas y minúsculas
print(nombre.upper())
print(nombre.lower())

# ==========================================
# EJERCICIO
# ==========================================
nombre_usuario = input("Escribe tu nombre: ")

print("Hola", nombre_usuario)
print("Tu nombre tiene", len(nombre_usuario), "caracteres.")
