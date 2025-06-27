# Proyecto: Sistema de Gestión para una Librería

# TAREAS/FUNCIONALIDADES BÁSICAS POR REALIZAR:

# 1. Mostrar Catálogo
#    - Listar todos los libros del catálogo con sus datos completos.

# 2. Agregar Libro
#    - Ingresar un nuevo libro al catálogo.
#    - Validar que no se repita el título o ID.

# 3. Editar Libro
#    - Modificar los datos de un libro existente (título, autor, año, editorial, stock, precio).
#    - Buscar el libro por ID o título.

# 4. Eliminar Libro
#    - Eliminar un libro del catálogo.
#    - Confirmar antes de borrar.
#    - Buscar por ID o título.

# 5. Buscar Libro
#    - Buscar libros por título, autor, editorial o año.
#    - Mostrar coincidencias.

## SI NOS DA EL TIEMPO TAMBIEN PODEMOS HACER ESTA FUNCIONALIDAD

# 6. Agregar Venta
#    - Registrar una venta de un libro.
#    - Verificar que haya stock suficiente.
#    - Descontar el stock del libro vendido.
#    - Agregar el registro a la lista de ventas con fecha, cantidad y total.

# 7. Mostrar Ventas
#    - Ver lista de libros vendidos con sus datos.
#    - Posiblemente mostrar ventas por fecha o por libro.

# 8. Guardar y Cargar Datos (opcional)
#    - Guardar el catálogo y las ventas en archivos (JSON, CSV o TXT).
#    - Cargar los datos al iniciar el sistema.

# NOTA:
# - Usar estructuras de datos simples como listas y diccionarios.
# - Opcional: convertir en un menú interactivo por consola.

libros = [
    {
        "id": 1,
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "editorial": "Sudamericana",
        "año": 1967,
        "stock": 10,
        "precio": 3500.00
    },
    {
        "id": 2,
        "titulo": "1984",
        "autor": "George Orwell",
        "editorial": "Debolsillo",
        "año": 1949,
        "stock": 5,
        "precio": 2800.00
    },
    {
        "id": 3,
        "titulo": "El Principito",
        "autor": "Antoine de Saint-Exupéry",
        "editorial": "Salamandra",
        "año": 1943,
        "stock": 8,
        "precio": 2200.00
    },
    {
        "id": 4,
        "titulo": "Rayuela",
        "autor": "Julio Cortázar",
        "editorial": "Sudamericana",
        "año": 1963,
        "stock": 6,
        "precio": 3900.00
    },
    {
        "id": 5,
        "titulo": "Fahrenheit 451",
        "autor": "Ray Bradbury",
        "editorial": "Minotauro",
        "año": 1953,
        "stock": 4,
        "precio": 3100.00
    }
]

libros_vendidos = [
    {
        "id_venta": 1,
        "id_libro": 2,
        "titulo": "1984",
        "fecha": "2025-06-10",
        "cantidad": 2,
        "total": 5600.00
    },
    {
        "id_venta": 2,
        "id_libro": 1,
        "titulo": "Cien años de soledad",
        "fecha": "2025-06-11",
        "cantidad": 1,
        "total": 3500.00
    },
    {
        "id_venta": 3,
        "id_libro": 3,
        "titulo": "El Principito",
        "fecha": "2025-06-12",
        "cantidad": 3,
        "total": 6600.00
    }
]

def mostrar_catalogo(libros):
    print("Catalogo de libros")
    for libro in libros:
        print(f"Id: {libro["id"]}, Titulo: {libro["titulo"]}, Editorial: {libro["editorial"]}, Año: {libro["año"]}, Stock: {libro["stock"]}, Precio: {libro["precio"]}")

def agregar_libro(libros):
    id_libro = 1
    titulo = input("Ingresar Titulo: ")
    autor = input("Ingresar Autor: ")
    editorial = input("Ingresar Editorial: ")
    año = int(input("Ingresar Año: "))
    stock = int(input("Ingresar Stock: "))
    precio = float(input("Ingresar Precio: "))
    libros.append({"id": id_libro, "titulo": titulo, "autor": autor, "editorial": editorial, "año": año, "stock": stock, "precio": precio})
    print("Libro agregado")
    
def editar_libro(libros):
    id= int(input("Ingresar Id del libro a editar: "))
    for libro in libros:
      if libro["id"] == id:
        libro["titulo"] = input("Nuevo Título: ") 
        libro["autor"] = input("Nuevo Autor: ") 
        libro["editorial"] = input("Nueva Editorial: ") 
        libro["año"] = int(input("Nuevo Año: "))
        libro["stock"] = int(input("Nuevo Stock: ") )
        libro["precio"] = float(input("Nuevo Precio: ") )
        print("Libro actualizado")

def eliminar_libro(libros):
    id = int(input("Ingresar Id del libro a eliminar"))
    for libro in libros:
        if libro["id"] == id:
            libros.remove(libro)
            print("Libro eliminado")

def buscar_libro(libros):
    titulo = input("Ingresar titulo del libro")
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            print("Libro encontrado")

while True:
        print("Menu:")
        print("1. Mostrar catálogo")
        print("2. Agregar libro")
        print("3. Editar libro")
        print("4. Eliminar libro")
        print("5. Buscar libro")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            mostrar_catalogo(libros)
        elif opcion == "2":
            agregar_libro(libros)
        elif opcion == "3":
            editar_libro(libros)
        elif opcion == "4":
            eliminar_libro(libros)
        elif opcion == "5":
            buscar_libro(libros)
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")                                                  