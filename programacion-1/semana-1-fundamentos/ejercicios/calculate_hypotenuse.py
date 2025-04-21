import math

"""
Escribe un programa que pida al usuario los dos catetos de un triángulo rectángulo y calcule la hipotenusa.
"""



leg_a = float(input("Ingresa el valor del cateto A: "))
leg_b = float(input("Ingresa el valor del cateto B: "))

# Calcular la hipotenusa usando potenciación
hypotenuse = (leg_a ** 2 + leg_b ** 2) ** 0.5
print(f"El valor de la hipotenusa es: {hypotenuse:.2f}")

# Versión alternativa usando la función sqrt de la biblioteca math
hypotenuse_alt = math.sqrt(leg_a ** 2 + leg_b ** 2)
print(f"(Alternativa usando math.sqrt) La hipotenusa también es: {hypotenuse_alt:.2f}")
