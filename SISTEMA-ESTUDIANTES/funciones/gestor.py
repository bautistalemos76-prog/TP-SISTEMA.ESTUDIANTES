def crear_estudiante(nombre, legajo, curso):
    estudiante = {
        "nombre": nombre,
        "legajo": legajo,
        "curso": curso,
        "notas": [],
        "materias": []
    }

    print("Estudiante creado correctamente.")
    return estudiante


def listar_estudiantes(lista):
    if len(lista) == 0:
        print("No hay estudiantes cargados.")
        return

    for i in range(len(lista)):
        estudiante = lista[i]
        print("ID:", i)
        print("Nombre:", estudiante["nombre"])
        print("Legajo:", estudiante["legajo"])
        print("Curso:", estudiante["curso"])
        print("Notas:", estudiante["notas"])
        print("Materias:", estudiante["materias"])
        print("--------------------")


def listar_nombres_estudiantes(lista):
    if len(lista) == 0:
        print("No hay estudiantes cargados.")
        return

    for i in range(len(lista)):
        print("ID:", i, "-", lista[i]["nombre"])


def agregar_nota(estudiante, nota):
    estudiante["notas"].append(nota)
    print("Nota agregada correctamente.")


def agregar_materia(estudiante, materia):
    estudiante["materias"].append(materia)
    print("Materia agregada correctamente.")


def crear_docente(nombre, especialidad):
    docente = {
        "nombre": nombre,
        "especialidad": especialidad,
        "cursos": []
    }

    print("Docente creado correctamente.")
    return docente


def listar_docentes(lista):
    if len(lista) == 0:
        print("No hay docentes cargados.")
        return

    for i in range(len(lista)):
        docente = lista[i]
        print("ID:", i)
        print("Nombre:", docente["nombre"])
        print("Especialidad:", docente["especialidad"])
        print("Cursos:", docente["cursos"])
        print("--------------------")


def agregar_curso(docente, curso):
    docente["cursos"].append(curso)
    print("Curso agregado correctamente.")