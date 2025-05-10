"""
Escribe una función que convierta un número entero a binario y otra que realice el cálculo inverso.
"""



def int_to_binary(number:int) -> str:
    if not isinstance(number, int):
        raise TypeError('El valor debe ser un número entero.')
    
    return bin(number)[2:]


def binary_to_int(binary:str) -> int:
    if not isinstance(binary, str):
        raise TypeError('La entrada debe ser una cadena de texto.')
    
    if not all(char in '01' for char in binary):
        raise ValueError('La cadena debe contener solo 0s y 1s.')


    return int(binary, base=2)


def main():
    for number in [13, 0, 7, 255]:
        binary = int_to_binary(number)
        print(f'Binario de {number} es {binary}')
        original = binary_to_int(binary)
        print(f'Entero de "{binary}" es {original}\n')

if __name__ == "__main__":
    main()
