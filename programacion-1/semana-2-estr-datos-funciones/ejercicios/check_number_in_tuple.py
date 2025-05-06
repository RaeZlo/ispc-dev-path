from random import randint

def generate_random_tuple(size: int, min_value: int = 0, max_value: int = 20) -> tuple[int, ...]:
    return tuple(randint(min_value, max_value) for _ in range(size))


def main():
    random_tuple = generate_random_tuple(10)

    try:
        user_input = int(input('Ingresa un número para comprobar su existencia: '))
    except ValueError:
        print('Entrada no válida. Por favor, ingrese un número entero.')
        return

    if user_input in random_tuple:
        print(f'El número {user_input} está presente en la tupla.')
    else:
        print(f'El número {user_input} no está presente en la tupla.')

    print('Tupla aleatoria generada:')
    print(random_tuple)


if __name__ == '__main__':
    main()
