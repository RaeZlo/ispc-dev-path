from random import randint

"""
Escribe un programa que determine el mayor de tres números dados.
"""



num1 = randint(0, 100)
num2 = randint(0, 100)
num3 = randint(0, 100)

if num1 >= num2 and num1 >= num3:
    print(f"El número más grande es: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"El número más grande es: {num2}")
else:
    print(f"El número más grande es: {num3}")
