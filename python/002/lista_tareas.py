tareas = []
repetir = True

while repetir:
    print("\nMenú de Tareas:")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        tarea = input("Ingresa la nueva tarea: ")
        tareas.append(tarea)
        print(f"Tarea '{tarea}' agregada con éxito.")
    elif opcion == "2":
        if len(tareas) == 0:
            print("No hay tareas en la lista.")
        else:
            print("Tareas actuales:")
            for i, tarea in enumerate(tareas):
                print(f"{i+1}. {tarea}")
    elif opcion == "3":
        if len(tareas) == 0:
            print("No hay tareas para eliminar.")
        else:
            print("Tareas disponibles:")
            for i, tarea in enumerate(tareas):
                print(f"{i+1}. {tarea}")
            num = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
            if 0 <= num < len(tareas):
                eliminada = tareas.pop(num)
                print(f"Tarea '{eliminada}' eliminada.")
            else:
                print("Número inválido.")
    elif opcion == "4":
        print("Saliendo del programa...")
        repetir = False
    else:
        print("Opción no válida, intenta de nuevo.")
