# ==========================================
# TEMA: FUNCIONES
# ==========================================
# Una función es código reutilizable.

# 1. FUNCIÓN SENCILLA
def saludar():
    print("Hola, bienvenido a Python.")

saludar()

# 2. FUNCIÓN CON PARÁMETRO
def saludar_persona(nombre):
    print("Hola", nombre)

saludar_persona("Ana")
saludar_persona("Carlos")

# 3. FUNCIÓN CON RETURN
def sumar(a, b):
    return a + b

resultado = sumar(10, 5)
print("Resultado:", resultado)

# 4. FUNCIÓN CON CONDICIONAL
def verificar_edad(edad):
    if edad >= 18:
        return "Es mayor de edad."
    else:
        return "Es menor de edad."

print(verificar_edad(20))
print(verificar_edad(15))

# EJERCICIO
def multiplicar(numero1, numero2):
    return numero1 * numero2

print(multiplicar(4, 5))
