"""
Escribe un programa que imprima el cuadrado de los números del 1 al 10.
"""



for i in range(1, 11):
    print(i ** 2)

# Alternativa
square = [i ** 2 for i in range(1, 11)]
