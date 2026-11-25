# ==========================================
# TIPO DE DATO: NONE
# ==========================================
# None representa la ausencia de un valor.
# No significa 0, False o texto vacío.

resultado = None

print("Resultado:", resultado)
print("Tipo:", type(resultado))

# Podemos comprobar si una variable contiene None
if resultado is None:
    print("Todavía no existe un resultado.")
else:
    print("Ya existe un resultado.")

# Después podemos asignarle un valor
resultado = 100

print("Nuevo resultado:", resultado)

# ==========================================
# EJERCICIO
# ==========================================
nombre = None

if nombre is None:
    print("No se ha registrado el nombre.")
else:
    print("Nombre:", nombre)
