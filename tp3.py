
#1. Crear un programa que almacene en una lista las materias de esta u otra carrera y que las muestre por pantalla. (La lista debe ser predefinida, no debe ser ingresada por el usuario).

#lista = ["Programación I", "Introducción a la informática", "Arquitectura de computadoras"]
#print(lista)

#2. Pedir al usuario que ingrese 5 números para luego almacenarlos en una lista y ordenarlos. Imprimir por pantalla el resultado.

#lista= []
#
#num1= int(input("ingrese un numero: "))
#num2= int(input("ingrese un numero: "))
#num3= int(input("ingrese un numero: "))
#num4= int(input("ingrese un numero: "))
#num5= int(input("ingrese un numero: "))
#
#lista.append(num1)
#lista.append(num2)
#lista.append(num3)
#lista.append(num4)
#lista.append(num5)
#
#lista.sort()
#print(lista)

#2da opcion

#numTotals= 5
#lista= []
#
#for i in range(numTotals):
#  num= int(input("ingrese un numero: "))
#  lista.append(num)
#
#lista.sort()
#print(lista)

#3. Dada la siguiente lista de frutas [“banana”, “manzana”, “pera”], permitir al usuario ingresar 3 frutas más para agregarlas al final de lista. Luego, mostrar por pantalla la lista completa y debajo la misma lista pero sólo con las frutas que añadió el usuario.

#lista= ["banana", "manzana", "pera"]
#
#fruta1= input("ingrese una fruta: ")
#fruta2= input("ingrese una fruta: ")
#fruta3= input("ingrese una fruta: ")
#lista.extend([fruta1, fruta2, fruta3])
#print(lista)
#
#print(lista[-3:])


#4. Dada la siguiente lista: países = [“Argentina,”Brasil”, “Bolivia”,”Paraguay”,”Venezuela”], realizar lo siguiente:

países = ["Argentina","Brasil", "Bolivia","Paraguay","Venezuela"]

#a. Imprimir la cantidad de elementos que tiene la lista.

#print(len(países))

#b. Imprimir el primer y último elemento.

#print(países[0], países[-1])

#c. Imprimir el resto.
#print(países[1:-1])

#d. Permitir que el usuario ingrese un país e imprimir el índice si el país se encuentra en la lista. Si no se encuentra, imprimir un mensaje advirtiendo al usuario.

#paisUsuario = input("ingrese un pais: ")
#
#if paisUsuario in países:
#  print(países.index(paisUsuario))
#else:
#  print("el pais ingresado no se encuentra en la lista")

#e. Permitir al usuario ingresar un número igual o menor a la cantidad de elementos de la lista. Quitar el elemento correspondiente de esa posición.

#numero = int(input("ingresar un número"))
#
#if numero <= len(países):
#  países.remove(países[numero])
#  print(países)
#else:
#  print("ingresar otro numero")
  
#f. Imprimir la lista en orden inverso.

#países.reverse()
#print(países)

#g. Vaciar la lista.
#países.clear()
#print(países)
#
#
##5. Escriba un programa Python que solicite al usuario el ingreso de números enteros. Cuando el usuario ingrese la palabra “fin” el programa deberá concluir con la carga de datos. Cada uno de los números ingresados por el usuario deberá ser almacenado en una lista. A continuación, realice las siguientes tareas:
#
#listaNumeros = []
#
#i=1
#
#while i > 0:
#  numero = input("ingresar un número entero")
#  if numero == "fin":
#    break
#  else:
#   listaNumeros.append(int(numero))
#
#print(listaNumeros)
##a. Determinar el máximo.
#
#listaNumeros.sort()
#print(listaNumeros[-1])
#
##b. Obtener segundo valor máximo. Es decir el que le sigue al máximo.
#
#print(listaNumeros[-2])
#
##c. Determinar el mínimo.
#
#print(listaNumeros[0])
#
##d. Calcular la multiplicación de todos los números de la lista.
#multiplicacion=1
#for i in range(len(listaNumeros)):
#  multiplicacion= multiplicacion *listaNumeros[i]
#  
#print(multiplicacion)
#  
##e. Contar los valores pares e impares.
#pares= 0
#impares= 0
#for i in range(len(listaNumeros)):
#  if listaNumeros[i] % 2 == 0:
#    pares+=1
#  else:
#    impares+=1
#print(f"pares={pares}, impares={impares}")
#
##f. Remover los elementos repetidos.
#sinRerpetidos= []
#for i in range(len(listaNumeros)):
#  if listaNumeros[i] in sinRerpetidos:
#    print("repetido")
#  else:
#    sinRerpetidos.append(listaNumeros[i])
#print(sinRerpetidos)
#


#6. Programe una aplicación de consola Python que brinde al usuario la posibilidad de a partir de una lista vacía:

#listaVacia= []
#
#i= 1
#while i > 0:
#  entrada = input("Elegir una de las siguientes opciones:\n1. Agregar un elemento al final.\n2. Agregar un elemento al principio.\n3. Quitar un elemento al final.\n4. Quitar un elemento al principio.\n0. Salir\n")
#  
#  match entrada :
#    case "1":
#      agregar= input("ingresar un elemento al final de la lista: ")
#      listaVacia.append(agregar)
#    case "2":
#      agregar= input("ingresar un elemento al principio")
#      listaVacia.insert(0, agregar)
#    case "3":
#      listaVacia.pop()
#    case "4":
#      listaVacia.pop(0)
#    case "0":
#      break
#    case _:
#      print("ingreso invalido")
#      break
#  print(listaVacia)
#      
#print(listaVacia)
#  
#a. Agregar un elemento al final.
#b. Agregar un elemento al principio.
#c. Quitar un elemento al final.
#d. Quitar un elemento al principio.

#listaVacia = []
#
#while True:
#    entrada = input(
#        "\nElegí una opción:\n"
#        "1. Agregar un elemento al final\n"
#        "2. Agregar un elemento al principio\n"
#        "3. Quitar un elemento al final\n"
#        "4. Quitar un elemento al principio\n"
#        "0. Salir\n"
#        ">> "
#    )
#
#    match entrada:
#        case "1":
#            agregar = input("Ingresá un elemento al final de la lista: ")
#            listaVacia.append(agregar)
#        case "2":
#            agregar = input("Ingresá un elemento al principio: ")
#            listaVacia.insert(0, agregar)
#        case "3":
#            if listaVacia:
#                listaVacia.pop()
#            else:
#                print("La lista está vacía, no se puede quitar nada.")
#        case "4":
#            if listaVacia:
#                listaVacia.pop(0)
#            else:
#                print("La lista está vacía, no se puede quitar nada.")
#        case "0":
#            print("Saliendo del programa...")
#            break
#        case _:
#            print("Ingreso inválido. Por favor, elegí una opción válida.")
#
#    print("Lista actual:", listaVacia)
#


#7. Escriba un programa Python que cuente con dos listas, la primera de ellas almacenará strings con tareas pendientes y la segunda almacenará strings con tareas terminadas. Permita al usuario:
#a. Agregar nuevas tareas pendientes.
#b. Marcar las tareas pendientes como terminadas. Al hacer esto, la tarea deberá pasar de la lista de pendientes a la de terminadas.
#Nota: posterior a cada operación deberá mostrar por pantalla el estado actual de ambas listas.

tareasPendientes = []
tareasTerminadas = []
stringPend= ""
stringTerm=""

while True:
  tareas = input(
    "\nElegí una opción:\n"
    "1. Agregar tarea pendiente\n"
    "2. Marcar tarea pendiente como terminada\n"
  )
  stringPend= ""
  stringTerm=""
  match tareas:
    case "1":
      agregar = input("Ingresá una tarea pendiente: ")
      tareasPendientes.append(agregar)
    case "2":
      if tareasPendientes:
        stringLista= ""
        for i in range(len(tareasPendientes)):
          stringLista +=f"{i+1} -{tareasPendientes[i]}\n"
        
        agregar = input(f"Ingresar el número de tarea que desea marcar como terminada: \n{stringLista}")
        tareaEliminada = int(agregar) -1
        tareasTerminadas.append(tareasPendientes[tareaEliminada])
        tareasPendientes.pop(tareaEliminada)
      else:
        print("No hay tareas pendientes")
    case "0":
      print("Ingreso inválido. Por favor, elegí una opción válida.")
      break
    case _:
      print("Ingreso inválido. Por favor, elegí una opción válida.")
      break
  for i in range(len(tareasPendientes)):
    stringPend +=f"{i+1}- {tareasPendientes[i]}\n"
  for i in range(len(tareasTerminadas)):
    stringTerm +=f"{i+1}- {tareasTerminadas[i]}\n"
  print(f"\nTareas pendientes: \n{"-Ninguna" if stringPend == "" else stringPend}\nTareas terminadas: \n{"-Ninguna" if stringTerm == "" else stringTerm}\n")