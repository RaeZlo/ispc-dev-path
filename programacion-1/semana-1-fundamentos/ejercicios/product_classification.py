from random import randint

"""
Escribe un programa que solicite al usuario el precio y la cantidad
de un producto. Clasifique el producto como "caro" si el precio es
mayor de $100 o si la cantidad es menor que 10 y el precio es
mayor de $50. De lo contrario, clasifíquelo como "barato". Incluye
condiciones para manejar valores falsos (0 o vacío).
"""



price = randint(1, 100)
quantity = randint(1, 100)

if price > 100 or (quantity < 10 and price >= 50):
    print(f"El producto con precio ${price} y cantidad {quantity} es caro.")
else: 
    print(f"El producto con precio ${price} y cantidad {quantity} es barato.")
