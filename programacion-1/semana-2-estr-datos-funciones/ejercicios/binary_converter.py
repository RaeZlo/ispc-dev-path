"""
Escribe una función que convierta un número entero a binario y otra que realice el cálculo inverso.
"""



def int_to_binary(number:int) -> str:
    if not isinstance(number, int):
        raise TypeError('El valor debe ser un número entero.')
    
    binary = bin(abs(number))[2:]  
    return f"-{binary}" if number < 0 else binary


def binary_to_int(binary:str) -> int:
    if not isinstance(binary, str):
        raise TypeError('La entrada debe ser una cadena de texto.')

    is_negative = binary.startswith('-')
    digits = binary[1:] if is_negative else binary

    if not all(char in '01' for char in digits):
        raise ValueError('La cadena debe contener solo 0s y 1s.')
    
    value = int(digits, base=2)
    return -value if is_negative else value


def main():
    for number in [13, 0, 7, 255, -10]:
        binary = int_to_binary(number)
        print(f'Binario de {number} es {binary}')
        original = binary_to_int(binary)
        print(f'Entero de "{binary}" es {original}\n')

if __name__ == "__main__":
    main()
