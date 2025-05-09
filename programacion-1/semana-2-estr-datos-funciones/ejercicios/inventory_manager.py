"""
Escribe un programa que administre el inventario de una tienda.
El programa debe permitir agregar nuevos productos, actualizar
las cantidades de los productos existentes, y mostrar el
inventario actual.
"""



def show_menu():
    print('\n--- Menú de Inventario ---')
    print('1. Agregar producto')
    print('2. Actualizar cantidad')
    print('3. Mostrar inventario')
    print('4. Salir')


def pluralize_unit(quantity):
    return 'unidades' if quantity != 1 else 'unidad'


def add_product(inventory):
    name = input('Nombre del producto:  ').strip()
    if not name:
        print('El nombre del producto no puede estar en blanco.')
        return
    if name in inventory:
        print('El producto ya existe. Usa la opción "Actualizar cantidad".')
        return
    
    try:
        quantity = int(input('Ingresa la cantidad del producto: '))
        if quantity < 0:
            raise ValueError('La cantidad no puede ser negativa.')
        inventory[name] = quantity
        print(f'El producto "{name}" fue añadido con {quantity} {pluralize_unit(quantity)}.')
    except ValueError as e:
        print(f'Error: {e}')


def update_product(inventory):
    name = input('Ingresa el nombre del producto a actualizar: ').strip()
    if name not in inventory:
        print('El producto no está en el inventario.')
        return
    try:
        quantity_change = int(input('Cantidad a agregar o restar (puede ser negativa): '))
        new_quantity = inventory[name] + quantity_change
        if new_quantity < 0:
            print('Error: la cantidad resultante no puede ser negativa.')
            return
        inventory[name] = new_quantity
        print(f'Actualizado. "{name}" ahora tiene {new_quantity} {pluralize_unit(new_quantity)}.')
    except ValueError:
        print('Error: por favor ingresa un número válido.')


def show_inventory(inventory):
    if not inventory:
        print('El inventario está vacío.')
    else:
        print('\n--- Inventario Actual ---')
        for name, quantity in inventory.items():
            print(f'{name}: {quantity} {pluralize_unit(quantity)}')


def main():
    inventory = {}
    while True:
        show_menu()
        option = input('Elige una opción: ')
        if option == '1':
            add_product(inventory)
        elif option == '2':
            update_product(inventory)
        elif option == '3':
            show_inventory(inventory)
        elif option == '4':
            print('Saliendo del programa...')
            break
        else:
            print('Opción inválida. Por favor intenta de nuevo.')


if __name__ == "__main__":
    main()
