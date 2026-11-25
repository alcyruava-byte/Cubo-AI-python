# ==========================================
# TIPO DE DATO: BOOLEAN
# ==========================================
# Un booleano solamente puede tener dos valores:
# True  = verdadero
# False = falso

es_mayor_de_edad = True
tiene_hambre = False

print("¿Es mayor de edad?", es_mayor_de_edad)
print("¿Tiene hambre?", tiene_hambre)

# Ver el tipo de dato
print(type(es_mayor_de_edad))

# Los booleanos se utilizan mucho con condiciones
if es_mayor_de_edad:
    print("La persona es mayor de edad.")
else:
    print("La persona es menor de edad.")

# ==========================================
# EJERCICIO
# ==========================================
tiene_dinero = True

if tiene_dinero:
    print("Puede comprar el producto.")
else:
    print("No puede comprar el producto.")
