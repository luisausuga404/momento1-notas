
estudiantes = {}


def registrar_estudiante():
    nombre = input("  Nombre del estudiante: ")
    if nombre in estudiantes:
        print("  Ya existe ese estudiante.")
    else:
        estudiantes[nombre] = []
        print("  Estudiante registrado.")


def registrar_nota():
    if not estudiantes:
        print("  No hay estudiantes registrados.")
        return
    nombre = input("  Nombre del estudiante: ")
    if nombre not in estudiantes:
        print("  Ese estudiante no existe.")
        return
    nota = float(input("  Nota (0.0 - 5.0): "))
    estudiantes[nombre].append(nota)
    print("  Nota registrada exitosamente.")


def ver_promedio():
    if not estudiantes:
        print("  No hay estudiantes registrados.")
        return
    nombre = input("Nombre del estudiante: ")
    if nombre not in estudiantes:
        print("  Ese estudiante no existe.")
        return
    notas = estudiantes[nombre]
    if not notas:
        print("  Ese estudiante no tiene notas.")
        return
    promedio = sum(notas) / len(notas)
    if promedio >= 3.0:
        estado = "APRUEBA"
    else:
        estado = "REPRUEBA"
    print("  Promedio:", promedio)
    print("  Estado:", estado)


def ver_todos():
    if not estudiantes:
        print("  No hay estudiantes registrados.")
        return
    for nombre, notas in estudiantes.items():
        print(" ", nombre, ":", notas)


def menu():
    print("SISTEMA DE NOTAS")
    print("  1. Registrar Estudiante")
    print("  2. Registrar Nota")
    print("  3. Ver Promedio")
    print("  4. Ver Todos")
    print("  5. Salir")



if __name__ == "__main__":
    print("Bienvenido al Sistema de Notas")

    while True:
        menu()
        opcion = input("  Elige una opción: ")

        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            registrar_nota()
        elif opcion == "3":
            ver_promedio()
        elif opcion == "4":
            ver_todos()
        elif opcion == "5":
            print("  Hasta luego!")
            break
        else:
            print("  Opción inválida.")