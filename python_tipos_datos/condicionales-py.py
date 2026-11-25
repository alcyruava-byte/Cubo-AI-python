# ==========================================
# PYTHON DESDE CERO: CONDICIONALES
# ==========================================
# Basado en el archivo condicionales.py proporcionado.
# Incluye if, else, if anidado, elif y and.

a = 15
b = 5
c = 20

# 1. IF Y ELSE
if a > b:
    print("b es menor que a")
else:
    print("a es mayor o igual que b")

# 2. IF ANIDADO
if a > b:
    if c > a:
        print("c es mayor que a")
    else:
        print("a es menor o igual que c")
else:
    print("b es mayor o igual que a")

# 3. OPERADOR AND
if a > b and a > c:
    print("a es mayor que b y c")
else:
    print("No se cumplen las dos condiciones.")

# 4. IF, ELIF Y ELSE
edad = 20

if edad < 18:
    print("Es menor de edad.")
elif edad == 18:
    print("Tiene exactamente 18 años.")
else:
    print("Es mayor de edad.")

# 5. COMPARACIONES
x = 10
y = 10

print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)

# 6. EJERCICIO
numero = 25

if numero > 50:
    print("El número es mayor que 50.")
elif numero == 50:
    print("El número es 50.")
else:
    print("El número es menor que 50.")
