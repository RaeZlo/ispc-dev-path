from random import randint

"""
Escribe un programa que a partir de un número entero positivo, muestre por pantalla si es par o impar.
"""



num = randint(0, 1000)

print(f"El número a analizar es: {num}")

if num % 2 == 0:
    print("Es un número PAR.")
else:
    print("Es un número IMPAR.")
