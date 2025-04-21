from random import randint

"""
Escribe un programa que permita realizar la división de dos números siempre y cuando el denominador no sea 0.
"""



numerator = randint(0, 100)
denominator = randint(0, 10)

print(f"Dividendo: {numerator}")
print(f"Divisor: {denominator}")

# Verificar si el divisor es distinto de cero
if denominator != 0:
    result  = numerator / denominator
    print(f"El resultado de la división es: {result:.2f}")
else:
    print("Error: No se puede dividir entre cero.")
