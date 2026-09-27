contactos = {}

def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número telefónico: ")
    contactos[nombre] = telefono
    print("Contacto agregado correctamente.")
    
def mostrar_contactos():
    print("\n--- Lista de contactos ---")
    
    if len(contactos) == 0:
        print("No hay contactos registrados.")
    else:
        for nombre, telefono in contactos.items():
            print("Nombre:", nombre, "| Teléfono:", telefono)

def buscar_contacto():
    nombre = input("Ingrese el nombre que desea buscar: ")

    if nombre in contactos:
        print("Contacto encontrado:")
        print("Nombre:", nombre)
        print("Teléfono:", contactos[nombre])
    else:
        print("El contacto no existe.")

def eliminar_contacto():
    nombre = input("Ingrese el nombre del contacto que desea eliminar: ")

    if nombre in contactos:
        del contactos[nombre]
        print("Contacto eliminado correctamente.")
    else:
        print("El contacto no existe.")

while True:
    print("\n===== AGENDA DE CONTACTOS =====")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        mostrar_contactos()
    elif opcion == "3":
        buscar_contacto()
    elif opcion == "4":
        eliminar_contacto()
    elif opcion == "5":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida.")