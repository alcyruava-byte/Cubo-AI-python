# ==========================================
# TIPO DE DATO: DICTIONARY (dict)
# ==========================================
# Un diccionario guarda información en pares:
# clave: valor

persona = {
    "nombre": "Alcira",
    "edad": 40,
    "pais": "El Salvador"
}

print("Diccionario:", persona)
print("Tipo:", type(persona))

# Obtener valores mediante sus claves
print("Nombre:", persona["nombre"])
print("Edad:", persona["edad"])

# Agregar una nueva clave
persona["profesion"] = "Farmacéutica"

print("Diccionario actualizado:", persona)

# Cambiar un valor
persona["edad"] = 30

print("Nueva edad:", persona["edad"])

# ==========================================
# EJERCICIO
# ==========================================
producto = {
    "nombre": "Pan",
    "precio": 1.50,
    "cantidad": 3
}

total = producto["precio"] * producto["cantidad"]

print("Producto:", producto["nombre"])
print("Total:", total)
