from random import randint

"""
Escribe un programa que genere un número aleatorio entre 1 y 100 y
permita al usuario adivinar el número. El programa debe brindar pistas
(ej. el número secreto es mayor) y debe continuar pidiendo al usuario
que adivine hasta que acierte. Al finalizar, debe mostrar el número de
intentos.
"""



secret_number = randint(1, 100)
attempts = 0

while True:
    print("\n--- Adivina el número entre 1 y 100 ---")
    user_input = int(input("Ingrese un número: "))

    attempts += 1

    if user_input > secret_number:
        print("El número secreto es menor.")
    elif user_input < secret_number:
        print("El número secreto es mayor.")
    else:
        print(f"¡Correcto! El número era {secret_number}.")
        print(f"Lo adivinaste en {attempts} intento{'s' if attempts != 1 else ''}.")
        break
