# ==========================================
# TEMA: MÓDULOS
# ==========================================
# Los módulos permiten utilizar código
# que ya existe en otros archivos o en Python.

import random
import math

# random
numero = random.randint(1, 99)
print("Número aleatorio:", numero)

# math
print("Raíz cuadrada de 25:", math.sqrt(25))
print("Valor de pi:", math.pi)

# Importar una función específica
from random import randint

numero2 = randint(1, 10)
print("Otro número aleatorio:", numero2)

# EJERCICIO
dado = random.randint(1, 6)
print("Resultado del dado:", dado)
