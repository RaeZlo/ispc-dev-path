from random import randint

"""
Escribe un programa que solicite tres lados de un triángulo e indique si es equilátero, isósceles o escaleno.
"""



side1 = randint(1, 11)
side2 = randint(1, 11)
side3 = randint(1, 11)

# Mostrar los lados generados para referencia
print(f"Lados generados: {side1}, {side2}, {side3}")

# Verificar el tipo de triángulo
if side1 == side2 == side3:
    print("El triángulo es equilátero.")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")
