from datetime import date

"""
Escribe un programa que pida al usuario su año de nacimiento,
calcule su edad y genere un mensaje de saludo personalizado
que incluya su nombre y la edad calculada.
"""


name = input("Ingrese su nombre: ")
year_of_birth = int(input("Ingrese su año de nacimiento: "))

current_year = date.today().year
age = current_year - year_of_birth

print(f"¡Hola {name}! Tienes {age} años.")
