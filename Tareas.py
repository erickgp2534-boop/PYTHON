'''
Funcionalidades mínimas obligatorias para este proyecto:
Ver el menú principal de opciones.

Agregar una nueva tarea (con un título y estado pendiente por defecto).

Listar todas las tareas registradas con su estado (Pendiente / Completada).

Marcar una tarea como completada.

Eliminar una tarea.

Guardar y cargar automáticamente las tareas desde un archivo tasks.json.
'''
limpiar = {"hacer": "barrer",
           "terminada" : True,
           "numero": 1}

trastes = {"hacer": "limpiar los trastes",
           "terminada": False,
           "numero": 2}

tareas = [limpiar, trastes]

for tarea in tareas:
    if tarea['terminada']:
        estado = "terminada"
    else:
        estado = "pendiente"
    print(f"{tarea['numero']} Hacer: {tarea['hacer']} | esta terminada: {estado}")

def Menu():
    print("===Menu de listar tareas===")
    print("1. Agregar una tarea.")
    print("2. Listar todas las tareas")
    print("3. Marcar una tarea como completada")
    print("4. Eliminar una tarea")
    print("5. Guardar y cargar los archivos a un json")

def agregar_tarea(tareas):
    listar_tareas = {}
    titulo = input("que tipo de tarea quieres añadir: ").lower()
    estado = input("Tu tarea ya ah sido pendiente o terminada: ").lower()
    numero = 0

    if titulo.lower() in listar_tareas:
        print("Esta tarea ya esta en la lista.")
    else:
        listar_tareas[titulo] = {
            "numero": numero + 1,
            "estado": estado
        }
        print("Su tarea ah sido agregada con exito.")
        tareas.append(listar_tareas)