"""
Escribe un programa que sume todos los números de una lista y
luego responde ¿Qué tipo de variable utilizamos para resolver?
"""



numbers = [21, 43, 5, 32, 7, 88, 54, 32, 1, 3]

if not numbers:
    print("La lista está vacía.")
else:
    accumulator = 0
    for num in numbers:
        accumulator += num

print(f"La suma de todos los números es: {accumulator}")

# Alternativa
accumulator = sum(numbers)
print(f"La suma de todos los números es: {accumulator}")
