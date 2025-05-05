from random import randint

"""
Crea una lista de números que cuente el número de veces que aparece el número ingresado por el usuario.
"""



def generate_random_list(size:int, min_value:int = 0, max_value:int = 20) -> list[int]:
    return [randint(min_value, max_value) for _ in range(size)]


def main():
    random_list = generate_random_list(10)

    try:
        user_input = int(input('Ingresa un número para buscar: '))
    except ValueError:
        print('Entrada no válida. Por favor, ingrese un número entero.')
        return
    
    occurrences = random_list.count(user_input)
    print(f'El número {user_input} aparece {occurrences} veces en la lista.')

    print('Lista aleatoria generada: ')
    print(random_list)

if __name__ == '__main__':
    main()
