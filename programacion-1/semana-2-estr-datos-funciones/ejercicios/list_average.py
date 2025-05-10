"""
Escribe una función que reciba una lista de números y devuelva el promedio.
"""



def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("La lista no puede estar vacía.")

    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("Todos los elementos deben ser números (int o float).")

    return sum(numbers) / len(numbers)


def main():
    arr = [10, 20, 30, 40]

    try:
        average = calculate_average(arr)
        print(f"El promedio es: {average:.2f}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
