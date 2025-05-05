"""
amigos = ['Ana', 'Monica', 'José', 'Camila', 'Raquel', 'Matías']

1. Devuelve la posición (el index, un número) del amigo “Matías”.
2. Devuelve la misma lista pero añadiendo los amigos de la
infancia “Ivana” y “Andrés” como otra lista.
3. Agrega un nuevo amigo “María” y devuelve el nro de amigos.
4. Elimina el último elemento amigo y devuelve el nombre del
amigo eliminado.
5. Devuelve un arreglo ordenado alfabéticamente.
"""



def show_list(friends:list[str]):
    print(f'Lista actual de amigos: {friends}')


def get_friend_position(friends:list[str], name:str):
    try:
        position = friends.index(name)
        print(f'La posición de {name} es: {position}')
    except ValueError:
        print(f'"{name}" no está en la lista.')


def add_childhood_friends(friends:list[str], new_friends:list[str]):
    friends.extend(new_friends)
    print(f'Se agregaron los amigos de la infancia: {new_friends}')
    return friends


def add_friend(friends:list[str], new_friend:str):
    friends.append(new_friend)
    print(f'Se agregó en la lista: {new_friend}. Ahora hay {len(friends)} amigos')
    return friends


def remove_last_friend(friends:list[str]):
    if friends:
        removed = friends.pop()
        print(f'Se eliminó al último amigo: {removed}')
    else:
        print('La lista está vacía. No se puede eliminar.')
        return None


def get_sorted_list(friends:list[str]):
    sorted_list = sorted(friends)
    print(f'Lista ordenada alfabéticamente: {sorted_list}')
    return sorted_list


# Main program
def main():
    friends = ['Ana', 'Monica', 'José', 'Camila', 'Raquel', 'Matías']
    show_list(friends)

    get_friend_position(friends, 'Matías')

    friends = add_childhood_friends(friends, ['Ivana', 'Andrés'])
    show_list(friends)

    friends = add_friend(friends, 'María')

    remove_last_friend(friends)

    get_sorted_list(friends)

# Entry point
if __name__ == "__main__":
    main()
