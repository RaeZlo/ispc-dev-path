"""
Escribe un programa que pida al usuario el radio de un círculo y calcule el área.
"""

radius = int(input("Ingresa el radio de un círculo: "))

if radius <= 0:
    print("El radio debe ser un número positivo.")
else:
    area = 3.14 * (radius ** 2)
    print(f"El área es igual a: {area}")
