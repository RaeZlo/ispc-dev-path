"""
Escribe un programa que cuente el número de vocales en una
cadena de texto proporcionada por el usuario.
"""



user_input = input("Ingrese un texto: ")
vowels_count = 0

for char in user_input:
    if char in "aeiouAEIOU":
        vowels_count += 1

print(f"La sumatoria de las vocales es de: {vowels_count}")

# Alternativa
vowels_count = sum(1 for char in user_input.lower() if char in "aeiou")
