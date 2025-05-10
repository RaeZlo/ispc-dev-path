"""
Escribe un programa que permita llevar un registro de las
calificaciones de varios estudiantes. El programa debe permitir
agregar estudiantes con sus calificaciones, actualizar las
calificaciones de un estudiante existente y mostrar el promedio
de calificaciones de un estudiante específico.
"""



def add_student(student_records):
    name = input('Nombre y apellido del alumno: ').strip()
    if not name:
        print('El nombre no puede estar en blanco.')
        return
    if name in student_records:
        print('El alumno ya existe en la base de datos.')
        return
    
    try:
        grades = list(map(float, input('Ingresa las notas del estudiante separadas por espacios: ').split()))
        student_records[name] = grades
        print(f'El alumno "{name}" fue añadido con las siguientes notas: {student_records[name]}.')
    except ValueError:
        print('Error: Asegúrate de ingresar solo números en el apartado de notas.')


def update_grades(student_records):
    name = input('Nombre y apellido del alumno: ').strip()
    if name not in student_records:
        print('El alumno no se encuentra en la base de datos.')
        return

    try:
        grades = list(map(float, input('Ingresa las nuevas notas separadas por espacios: ').split()))
        student_records[name] = grades
        print(f'Notas actualizadas para el alumno "{name}": {student_records[name]}.')
    except ValueError:
        print('Error: Asegúrate de ingresar solo números.')


def show_average(student_records):
    name = input('Nombre y apellido del alumno: ').strip()
    if name not in student_records:
        print('El alumno no se encuentra en la base de datos.')
        return
    
    grades = student_records[name]
    if not grades:
        print(f'El alumno "{name}" no tiene notas registradas.')
        return
    
    average = sum(grades) / len(grades)
    print(f'Promedio de notas para "{name}": {average:.2f}')


def show_menu():
    print("\n--- MENÚ ---")
    print("1. Agregar alumno")
    print("2. Actualizar notas")
    print("3. Mostrar promedio")
    print("4. Salir")


def main():
    student_records = {}

    while True:
        show_menu()
        choice = input("Selecciona una opción: ").strip()

        if choice == "1":
            add_student(student_records)
        elif choice == "2":
            update_grades(student_records)
        elif choice == "3":
            show_average(student_records)
        elif choice == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
