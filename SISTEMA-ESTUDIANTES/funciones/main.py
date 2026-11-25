from funciones.gestor import *


lista_estudiantes = []
lista_docentes = []
opcion_principal = ""

while opcion_principal != "3":
    print("\nMAIN")
    print("1. Estudiante")
    print("2. Docente")
    print("3. Salir")
    opcion_principal = input("Elegí una opción: ")
    if opcion_principal == "1":
        opcion_estudiante = ""
        while opcion_estudiante != "5":
            print("\nMENÚ ESTUDIANTE")
            print("1. Crear")
            print("2. Listar")
            print("3. Ingresar nota")
            print("4. Ingresar materia")
            print("5. Volver")
            opcion_estudiante = input("Elegí una opción: ")
            if opcion_estudiante == "1":
                nombre = input("Ingresá el nombre: ")
                legajo = int(input("Ingresá el legajo: "))
                curso =input("Ingresá el curso: ")
                estudiante = crear_estudiante(nombre, legajo, curso)
                lista_estudiantes.append(estudiante)

            elif opcion_estudiante == "2":
                listar_estudiantes(lista_estudiantes)

            elif opcion_estudiante == "3":
                listar_nombres_estudiantes(lista_estudiantes)

                if len(lista_estudiantes) > 0:
                    id_estudiante = int(input("Ingresá el ID del estudiante: "))
                    if id_estudiante >= 0 and id_estudiante < len(lista_estudiantes):
                        nota = int(input("Ingresá la nota: "))
                        agregar_nota(lista_estudiantes[id_estudiante], nota)
                    else:
                        print("Ese ID no existe.")
            elif opcion_estudiante == "4":
                listar_nombres_estudiantes(lista_estudiantes)
                if len(lista_estudiantes) > 0:
                    id_estudiante = int(input("Ingresá el ID del estudiante: "))
                    if id_estudiante >= 0 and id_estudiante < len(lista_estudiantes):
                        materia = input("Ingresá la materia: ")
                        agregar_materia(lista_estudiantes[id_estudiante], materia)
                    else:
                        print("Ese ID no existe.")
            elif opcion_estudiante != "5":
                print("opcion incorrecta.")
    elif opcion_principal == "2":
        opcion_docente = ""
        while opcion_docente != "4":
            print("\nMENÚ DOCENTE")
            print("1. Crear")
            print("2. Listar")
            print("3. Ingresar curso")
            print("4. Volver")
            opcion_docente = input("Elegí una opción ")
            if opcion_docente == "1":
                nombre = input("Ingresá el nombre: ")
                especialidad = input("Ingresá la especialidad")
                docente = crear_docente(nombre, especialidad)
                lista_docentes.append(docente)
            elif opcion_docente == "2":
                listar_docentes(lista_docentes)
            elif opcion_docente == "3":
                listar_docentes(lista_docentes)
                if len(lista_docentes) > 0:
                    id_docente = int(input("Ingresá el ID del docente: "))
                    if id_docente >= 0 and id_docente < len(lista_docentes):
                        curso = input("Ingresá el curso: ")
                        agregar_curso(lista_docentes[id_docente], curso)
                    else:
                        print("Ese ID no existe.")
            elif opcion_docente != "4":
                print("opcion incorrecta")
    elif opcion_principal != "3":
        print("Opción incorrecta.")
print("programa finalizado")