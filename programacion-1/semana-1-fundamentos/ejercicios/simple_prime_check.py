from random import randint

"""
Escribe un programa que a partir de un número entero positivo, muestre por pantalla si es primo o no.
"""



num = randint(0, 25)
print(f"El número a analizar es: {num}")

# Verificamos si el número es primo usando condiciones fijas
if num in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
    print("El número ES PRIMO.")
else:
    print("El número NO es primo.")
