"""
Escribe una función que reciba como parámetros un nombre y
devuelva un saludo personalizado.
"""



def personalized_greeting(name: str) -> str:
    if not name.strip():
        return "El nombre no puede estar vacío."
    return f'Buenos días {name.title()}.'


def main():
    name = input("Ingresa tu nombre: ").strip()
    message = personalized_greeting(name)
    print(message)

if __name__ == "__main__":
    main()
