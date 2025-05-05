from random import randint

"""
Crea una lista de números desordenados y ordénala en orden ascendente y descendente.
"""



def generate_random_list(size:int, min_value:int = 0, max_value:int = 1000) -> list[int]:
    return [randint(min_value, max_value) for _ in range(size)]


def sort_list_ascending(numbers:list[int]) -> list[int]:
    return sorted(numbers)


def sort_list_descending(numbers:list[int]) -> list[int]:
    return sorted(numbers, reverse=True)


def main():
    random_list = generate_random_list(15)
    
    print("Lista original:")
    print(random_list)

    print("\nOrden ascendente:")
    print(sort_list_ascending(random_list))

    print("\nOrden descendente:")
    print(sort_list_descending(random_list))

if __name__ == "__main__":
    main()
