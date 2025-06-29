import json

from datetime import datetime

with open("libros.json", "r", encoding="utf-8") as lib:
  libros = json.load(lib)

with open("libros-vendidos.json", "r", encoding="utf-8") as lib:
  libros_vendidos = json.load(lib)

fecha_actual = datetime.now()

def mostrar_libro(libro):
  print(f"ID: {str(libro['id'])}\n"
  f"Título: {libro['titulo']}\n"
  f"Autor: {libro['autor']}\n"
  f"Editorial: {libro['editorial']}\n"
  f"Año: {str(libro["año"])}\n"
  f"Stock: {str(libro['stock'])}\n"
  f"Precio: ${str(libro['precio'])}\n")

def mostrar_venta(libro_venta):
  print(f"ID Venta: {str(libro_venta['id_venta'])}\n"
  f"ID Libro: {str(libro_venta['id_libro'])}\n"
  f"Título: {libro_venta['titulo']}\n"
  f"Fecha y Hora: {libro_venta['fecha']}\n"
  f"Cantidad: {str(libro_venta['cantidad'])}\n"
  f"Total: ${str(libro_venta['total'])}\n")

def validar_num_int(ingreso):
  try:
    num = int(ingreso)
    return num
  except ValueError:
    otro_ingreso = input("Error, ingresar un número válido: ")
    return validar_num_int(otro_ingreso)
  
def validar_num_float(ingreso):
  try:
    num = float(ingreso)
    return num
  except ValueError:
    otro_ingreso = input("Error, ingresar un número válido: ")
    return validar_num_float(otro_ingreso)
  
def comprobar_stock(stock, cantidad):
  if cantidad == 0:
    print("No es posible realizar la venta")
    return False
  elif(int(stock )- int(cantidad)) < 0:
    print("No hay stock suficiente para realizar la venta")
    cantidad = comprobar_stock(stock,validar_num_int((input("Ingresar otra cantidad a vender: "))))
    return cantidad
  else: return cantidad
  
def guardar_json(libros):
  with open("libros.json", "w", encoding="utf-8") as lib:
    json.dump(libros, lib, indent=4, ensure_ascii=False)

def guardar_json_venta(libros_vendidos):
  with open("libros-vendidos.json", "w", encoding="utf-8") as lib:
    json.dump(libros_vendidos, lib, indent=4, ensure_ascii=False)

def generar_ID(libros):
  if libros:
    return  max(libro["id"] for libro in libros) +1
  else:
    return 1

def generar_ID_venta(libros_vendidos):
  if libros_vendidos:
    return  max(libro_venta["id_venta"] for libro_venta  in libros_vendidos) +1
  else:
    return 1

# OPCIONES
def mostrar_catalogo(libros):
  if libros:
    print(
      "\n#######################"
      "\nCatálogo de libros\n")
    for libro in libros:
      mostrar_libro(libro)
  else:
    print("Aún no hay libros...")

def agregar_libro(libros):
  titulo = input("Ingresar Título: ")
  autor = input("Ingresar Autor: ")
  editorial = input("Ingresar Editorial: ")
  año = validar_num_int(input("Ingresar Año: "))
  stock = validar_num_int(input("Ingresar Stock: "))
  precio = validar_num_float(input("Ingresar Precio: "))
  nuevoLibro= {
    "id": generar_ID(libros),
    "titulo":titulo,
    "autor": autor,
    "editorial": editorial,
    "año": año,
    "stock": stock,
    "precio": precio
  }
  libros.append(nuevoLibro)
  guardar_json(libros)
  print(
    "\n#######################"
    "\nLibro agregado: \n")
  mostrar_libro(nuevoLibro)
  
def editar_libro(libros):
  id = input("Ingresar Id del libro a editar: ")
  encontrado = any(libro["id"] == int(id) for libro in libros)
  if encontrado:
    for libro in libros:
      if libro['id'] == int(id):
        editar = input(
        "\n#######################\n"
        "¿Qué dato del libro querés editar?\n"
        f"1. Título: {libro['titulo']}\n"
        f"2. Autor: {libro['autor']}\n"
        f"3. Editorial: {libro['editorial']}\n"
        f"4. Año: {str(libro["año"])}\n"
        f"5. Stock: {str(libro['stock'])}\n"
        f"6. Precio: {str(libro['precio'])}\n")
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
              libro['año'] = validar_num_int(nuevo)
          case "5":
              nuevo = input("Nuevo Stock: ")
              libro['stock'] = validar_num_int(nuevo)
          case "6":
              nuevo = input("Nuevo Precio: ")
              libro['precio'] = validar_num_float(nuevo)
          case _:
              print("Opción inválida.")
        guardar_json(libros)
        print(
          "\n#######################"
          "\nLibro actualizado: \n")
        mostrar_libro(libro)
        break
  else:
    print("No se encontró un libro con ese ID")
    
def eliminar_libro(libros):
  id = int(input("Ingresar el ID del libro a ELIMINAR: "))
  encontrado = any(libro["id"] == id for libro in libros)
  if encontrado:
    for libro in libros:
      if libro["id"] == id:
          confirmacion = input(f"""Estás seguro que desea ELIMINAR "{libro['titulo']}"? S/N """)
          if(confirmacion.lower() =="s"):
            libros.remove(libro)
            guardar_json(libros)
            print(
            "\n#######################"
            "\nLibro eliminado: \n")
            mostrar_libro(libro)
          else:
            print("NO se eliminó el libro.")
  else:
    print("No se encontró un libro con ese ID.")

def buscar_libro(libros):
  resultados = []
  busqueda = input("Ingresá un dato (Título, Autor, Editorial, Año..) para buscar un libro... ").lower()
  for libro in libros:
    if(busqueda in libro["titulo"].lower() or busqueda in libro["autor"].lower() or busqueda in libro["editorial"].lower() or busqueda == str(libro["año"])):
      resultados.append(libro)
  
  if(len(resultados)):
    print("\n#######################"
          "\nResultado de la busqueda:\n")
    for resultado in resultados:
      mostrar_libro(resultado)
  else:
    print("No hay resultados...")
    
def mostrar_vendidos(libros_vendidos):
  if libros_vendidos:
    print(
    "\n#######################\n"
    "Ventas realizadas:\n")
    for libro_venta in libros_vendidos:
      mostrar_venta(libro_venta)
  else:
    print("Aún no hay ventas...")
    
def ingresar_venta(libros, libros_vendidos):
  id = validar_num_int(input("Ingresá ID del libro a vender: "))
  encontrado = any(libro["id"] == int(id) for libro in libros)
  if not encontrado:
    print("El libro ingresado no existe.")
  else:
    for libro in libros:
      if libro['id'] == int(id):
        if libro["stock"]:
          print(f"""El stock de "{libro['titulo']}" es {libro['stock']}.""")
          cantidad = comprobar_stock(libro['stock'],validar_num_int((input("Ingresar cantidad a vender: "))))
          total= libro['precio'] * float(cantidad)
      
          nuevaVenta= {
            "id_venta": generar_ID_venta(libros_vendidos),
            "id_libro": id,
            "titulo":libro['titulo'],
            "fecha": fecha_actual.strftime("%d/%m/%Y; %H:%M:%S"),
            "cantidad": int(cantidad),
            "total": float(total)
          }
          if cantidad == False:
           break         
          else:
            confirmacion = input(f"El precio por unidad es {libro['precio']}, el total a pagar es ${total}, desea CONFIRMAR la VENTA? S/N ")
            if(confirmacion.lower() =="s"):
              libro["stock"] -= int(cantidad)
              print(f"el stock es {libro["stock"]}")
              libros_vendidos.append(nuevaVenta)
              guardar_json(libros)
              guardar_json_venta(libros_vendidos)
              print(
              "\n#######################"
              "\nINFORMACIÓN DE VENTA:")
              mostrar_venta(nuevaVenta)
            else:
              print("Venta cancelada")
        else:
          print(f"""No hay stock de "{libro['titulo']}" """)

#MENU:    
while True :   
  inicio = input(
    "\nBIENVENIDO AL SISTEMA DE GESTIÓN DE LIBRERIAS\n"
    "\nMenú:\n"
    "1. Mostrar catálogo\n"
    "2. Agregar libro\n"
    "3. Editar libro\n"
    "4. Eliminar libro\n"
    "5. Buscar libro\n"
    "6. Mostrar Ventas\n"
    "7. Ingresar Venta\n"
    "0. Salir\n"
  )
  match inicio:
    case "1":
      mostrar_catalogo(libros)
      break
    case "2":
      agregar_libro(libros)
      break
    case "3":
      editar_libro(libros)
      break
    case "4":
      eliminar_libro(libros)
      break
    case "5":
      buscar_libro(libros)
      break
    case "6":
      mostrar_vendidos(libros_vendidos)
      break
    case "7":
      ingresar_venta(libros, libros_vendidos)
      break
    case "0":
      print("Gracias por utilizar nuestro sistema.")
      break
    case _:
      print("Ingreso inválido. Por favor, elegí una opción válida.")
      continue


