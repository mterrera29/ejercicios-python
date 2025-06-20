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

import json

""" libros = [
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
 """
""" libros_vendidos = [
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
 """

with open("libros.json", "r", encoding="utf-8") as lib:
  libros = json.load(lib)

with open("libros-vendidos.json", "r", encoding="utf-8") as lib:
  libros_vendidos = json.load(lib)

from datetime import datetime
fecha_actual = datetime.now()
  

def mostrarVenta(libro_venta):
  print(f"\nID Venta: {str(libro_venta['id_venta'])}\n"
  f"ID Libro: {str(libro_venta['id_libro'])}\n"
  f"Título: {libro_venta['titulo']}\n"
  f"Fecha: {libro_venta['fecha']}\n"
  f"Cantidad: {str(libro_venta['cantidad'])}\n"
  f"Total: {str(libro_venta['total'])}\n")

def mostrarLibro(libro):
  print(f"\nID: {str(libro['id'])}\n"
  f"Título: {libro['titulo']}\n"
  f"Autor: {libro['autor']}\n"
  f"Editorial: {libro['editorial']}\n"
  f"Año: {str(libro["año"])}\n"
  f"Stock: {str(libro['stock'])}\n"
  f"Precio: {str(libro['precio'])}\n")

def guardarJson():
  with open("libros.json", "w", encoding="utf-8") as lib:
    json.dump(libros, lib, indent=4, ensure_ascii=False)

def guardarJsonVenta():
  with open("libros-vendidos.json", "w", encoding="utf-8") as lib:
    json.dump(libros_vendidos, lib, indent=4, ensure_ascii=False)

def generarID():
  if libros:
    return  max(libro["id"] for libro in libros) +1
  else:
    return 1

def generarIDVenta():
  if libros_vendidos:
    return  max(libro_venta["id_venta"] for libro_venta  in libros_vendidos) +1
  else:
    return 1

# FUNCIONES DE LAS OPCIONES
def mostrarCatalogo():
  for libro in libros:
    print(
    "\n#######################")
    mostrarLibro(libro)

def agregarLibro():
  titulo = input("Ingresá Título: ")
  autor = input("Ingresá Autor: ")
  editorial = input("Ingresá Editorial: ")
  año = input("Ingresá Año: ")
  stock = input("Ingresá Stock: ")
  precio = input("Ingresá Precio: ")
  nuevoLibro= {
    "id": generarID(),
    "titulo":titulo,
    "autor": autor,
    "editorial": editorial,
    "año": int(año),
    "stock": int(stock),
    "precio": float(precio)
}
  libros.append(nuevoLibro)
  guardarJson()
  print(
    "\n#######################"
    "\nLIBRO AGREGADO:")
  mostrarLibro(nuevoLibro)
  
def editarLibro():
  id = input("Ingresá el ID del libro a editar: ")
  encontrado = any(libro["id"] == int(id) for libro in libros)
  if encontrado:
    for libro in libros:
      if libro['id'] == int(id):
        editar = input(
        "\n#######################\n"
        "¿Qué dato del libro querés editar?"
        f"\nID: {str(libro['id'])}\n"
        f"1 -Título: {libro['titulo']}\n"
        f"2 -Autor: {libro['autor']}\n"
        f"3 -Editorial: {libro['editorial']}\n"
        f"4 -Año: {str(libro["año"])}\n"
        f"5 -Stock: {str(libro['stock'])}\n"
        f"6 -Precio: {str(libro['precio'])}\n")
        match editar:
          case "1":
              nuevo = input("Nuevo Título: ")
              libro['titulo'] = nuevo
          case "2":
              nuevo = input("Nuevo Autor: ")
              libro['autor'] = nuevo
          case "3":
              nuevo = input("Nueva Editorial: ")
              libro['editorial'] = nuevo
          case "4":
              nuevo = input("Nuevo Año: ")
              libro['año'] = int(nuevo)
          case "5":
              nuevo = input("Nuevo Stock: ")
              libro['stock'] = int(nuevo)
          case "6":
              nuevo = input("Nuevo Precio: ")
              libro['precio'] = float(nuevo)
          case _:
              print("Opción inválida.")
        guardarJson()
        print(
          "\n#######################"
          "\nLIBRO EDITADO:")
        mostrarLibro(libro)
        break
  else:
    print("No se encontró un libro con ese ID")
    
def eliminarLibro():
  id = input("Ingresá el ID del libro a ELIMINAR: ")
  encontrado = any(libro["id"] == int(id) for libro in libros)
  if encontrado:
    for i, libro in enumerate(libros):
      if libro['id'] == int(id):
        confirmacion = input(f"Estas seguro que desea ELIMINAR {libro['titulo']}? S/N ")
        if(confirmacion.lower() =="s"):
          del libros[i]
          guardarJson()
          print(
          "\n#######################"
          "\nLIBRO ELIMINADO:")
          mostrarLibro(libro)
        else:
          print("NO se eliminó el libro")
  else:
    print("No se encontró un libro con ese ID")

def buscarLibro():
  resultados = []
  busqueda = input("Ingresá un dato (Título, Autor, Editorial, Año..) para buscar un libro... ").lower()
  for libro in libros:
    if(busqueda in libro["titulo"].lower() or busqueda in libro["autor"].lower() or busqueda in libro["editorial"].lower() or busqueda == str(libro["año"])):
      resultados.append(libro)
  
  if(len(resultados)):
    print("\n#######################"
          "\nRESULTADOS")
    for resultado in resultados:
      print(
      "\n#######################")
      mostrarLibro(resultado)
  else:
    print("No hay resultados...")
    
def mostrarVendidos():
  for libro_venta in libros_vendidos:
    print(
    "\n#######################")
    mostrarVenta(libro_venta)
    
def ingresarVenta():
  id = input("Ingresá ID del libro a vender: ")
  encontrado = any(libro["id"] == int(id) for libro in libros)
  titulo=""
  precio= 0
  stock = False
  if not encontrado:
    print("El libro ingresado no existe")
  else:
    for i, libro in enumerate(libros):
      if libro['id'] == int(id):
        if libro["stock"] == 0:
          stock=False
          break
        stock=True
        titulo= libro['titulo']
        precio= libro['precio']
      
  if not stock:
    print("No hay stock del libro a vender.")
  else:
    cantidad = input("Ingresá Cantidad: ")
    total= precio * float(cantidad)

    nuevaVenta= {
      "id_venta": generarIDVenta(),
      "id_libro": id,
      "titulo":titulo,
      "fecha": fecha_actual.strftime("%d/%m/%Y"),
      "cantidad": int(cantidad),
      "total": float(total)
    }
    
    confirmacion = input(f"El total a pagar es {total}, desea CONFIRMAR la VENTA? S/N ")
    
    if(confirmacion.lower() =="s"):
      for libro in libros:
        if libro['id'] == int(id):
          if(int(libro["stock"] )- int(cantidad)) < 0:
            print("No hay stock suficiente para realizar la venta")
            break         
          else:
            libro["stock"] -= int(cantidad)
            print(f"el stock es {libro["stock"]}")
            libros_vendidos.append(nuevaVenta)
            guardarJson()
            guardarJsonVenta()
            print(
            "\n#######################"
            "\n INFORMACIÓN DE VENTA:")
            mostrarVenta(nuevaVenta)
    else:
      print("Venta cancelada")
    
while True :   
  inicio = input(
    "\nBIENVENIDO AL SISTEMA DE GESTIÓN DE LIBRERIAS\n"
    "\nElegí una opción:\n"
    "1. Mostrar Catálogo de Libros\n"
    "2. Agregar un libro\n"
    "3. Editar Libro\n"
    "4. Eliminar Libro\n"
    "5. Buscar Libro\n"
    "6. Mostrar Ventas\n"
    "7. Ingresar Venta\n"
    "0. Salir\n"
  )
  match inicio:
    case "1":
      mostrarCatalogo()
      break
    case "2":
      agregarLibro()
      break
    case "3":
      editarLibro()
      break
    case "4":
      eliminarLibro()
      break
    case "5":
      buscarLibro()
      break
    case "6":
      mostrarVendidos()
      continue
    case "7":
      ingresarVenta()
      break
    case "0":
      print("Gracias por utilizar nuestro sistema.")
      break
    case _:
      print("Ingreso inválido. Por favor, elegí una opción válida.")
      continue


