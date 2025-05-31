
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

lista= [“banana”, “manzana”, “pera”]


#4. Dada la siguiente lista: países = [“Argentina,”Brasil”, “Bolivia”,”Paraguay”,”Venezuela”], realizar lo siguiente:
#a. Imprimir la cantidad de elementos que tiene la lista.
#b. Imprimir el primer y último elemento.
#c. Imprimir el resto.
#d. Permitir que el usuario ingrese un país e imprimir el índice si el país se encuentra en la lista. Si no se encuentra, imprimir un mensaje advirtiendo al usuario.
#e. Permitir al usuario ingresar un número igual o menor a la cantidad de elementos de la lista. Quitar el elemento correspondiente de esa posición. PROGRAMACIÓN 1 - Trabajo Práctico Nº 3 1
#f. Imprimir la lista en orden inverso.
#g. Vaciar la lista.
#5. Escriba un programa Python que solicite al usuario el ingreso de números enteros. Cuando el usuario ingrese la palabra “fin” el programa deberá concluir con la carga de datos. Cada uno de los números ingresados por el usuario deberá ser almacenado en una lista. A continuación, realice las siguientes tareas:
#a. Determinar el máximo.
#b. Obtener segundo valor máximo. Es decir el que le sigue al máximo.
#c. Determinar el mínimo.
#d. Calcular la multiplicación de todos los números de la lista.
#e. Contar los valores pares e impares.
#f. Remover los elementos repetidos.
#6. Programe una aplicación de consola Python que brinde al usuario la posibilidad de a partir de una lista vacía:
#a. Agregar un elemento al final.
#b. Agregar un elemento al principio.
#c. Quitar un elemento al final.
#d. Quitar un elemento al principio.
#7. Escriba un programa Python que cuente con dos listas, la primera de ellas almacenará strings con tareas pendientes y la segunda almacenará strings con tareas terminadas. Permita al usuario:
#a. Agregar nuevas tareas pendientes.
#b. Marcar las tareas pendientes como terminadas. Al hacer esto, la tarea deberá pasar de la lista de pendientes a la de terminadas.
#Nota: posterior a cada operación deberá mostrar por pantalla el estado actual de ambas listas.