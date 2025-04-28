"""
Escribe un programa que cuente los caracteres de una cadena
de texto proporcionada por el usuario utilizando el for.
"""



user_input = input("Ingrese un texto: ")
char_count = 0

if user_input:
    for char in user_input:
        if not char.isspace():
            char_count += 1
    print(f"Total de caracteres: {char_count}")
else:
    print("No se ingreso correctamente la información.")

# Alternativa
print(len(user_input))
