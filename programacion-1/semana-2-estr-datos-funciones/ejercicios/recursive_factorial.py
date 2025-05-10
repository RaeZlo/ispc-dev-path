"""
Escribe una función que permita calcular el factorial de un número.
"""


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("El número debe ser no negativo.")
    if n == 0:
        return 1
    return n * factorial(n - 1)


def main():
    try:
        number = int(input("Ingresa un número entero no negativo: "))
        result = factorial(number)
        print(f"El factorial de {number} es: {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
