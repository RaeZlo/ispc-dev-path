"""
Escribe un programa que solicite al usuario su nombre, edad y
número de teléfono. Verifica que ninguno de estos datos esté vacío
o sea un valor falso (por ejemplo, 0).
"""




name = input("Ingrese un nombre: ")
age = int(input("Ingrese una edad: "))
phone_num = int(input("Ingrese un número de telefono sin guiones o espacios: "))

if name and age and len(str(phone_num)) == 10:
    print("Todo correcto.")
