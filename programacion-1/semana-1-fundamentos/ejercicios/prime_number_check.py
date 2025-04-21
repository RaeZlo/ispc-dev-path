from random import randint

"""
Escribe un programa que a partir de un número entero positivo, muestre por pantalla si es primo o no.
"""



num = randint(2, 100)
print(f"El número a analizar es: {num}")

is_prime = True

# Verificamos los posibles divisores
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        is_prime = False  # Si encontramos un divisor, no es primo
        break

if is_prime:
    print("ES PRIMO.")
else:
    print("NO es PRIMO.")
