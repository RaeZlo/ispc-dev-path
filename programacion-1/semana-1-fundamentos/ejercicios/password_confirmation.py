"""
Escribe un programa que solicite al usuario que ingrese una
contraseña y confirme la contraseña. El programa debe verificar si
ambas contraseñas coinciden y no están vacías.
"""



password = input("Ingrese su contraseña: ")
confirm_password = input("Confirme su contraseña: ")

if not password or not confirm_password: 
    print("Las contraseñas no pueden estar vacías. Por favor, intente de nuevo.")
elif password != confirm_password:
    print("Las contraseñas no coinciden. Intente nuevamente.")
else:
    print("Contraseña confirmada. Ingresando...")
