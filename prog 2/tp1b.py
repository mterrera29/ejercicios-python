#Sección b (para entregar):
#1. Escribir un procedimiento realizar_calculo(). El mismo debe solicitar al usuario seleccionar por consola la operación matemática deseada (opciones: suma, resta, multiplicación, y división). Luego, debe solicitar que se ingresen 2 números. Por último, debe imprimir el resultado. Asumir que los valores ingresados son del tipo de datos correcto.


#def realizar_calculo():
#  seleccionar_operacion = input("Seleccionar una operación matemática:\n" 
#    "1. suma\n"
#    "2. resta\n"
#    "3. multiplicación\n"
#    "4. división\n"
#    )
#  num1= int(input("Ingresar un número: "))
#  num2= int(input("Ingresar otro número: "))
#  
#  match seleccionar_operacion:
#    case "1":
#      return num1 + num2
#    case "2":
#      return num1 - num2
#    case "3":
#      return num1 * num2
#    case "4":
#      return num1 / num2
#
#print(realizar_calculo())
  

#2. Escribir una función numero_en_orden_ascendente (numero) que retorne True si los dígitos del número están ordenados de menor a mayor, y False en caso contrario.

#def numero_en_orden_ascendente(numero):
#  numberList = list(str(numero))
#  for i in range(len(numberList) - 1):
#      if numberList[i] >= numberList[i+1]:
#          return False
#  return True
#  
#print(numero_en_orden_ascendente(1234))

#3. Escribir una función numeros_impares_juntos(entrada) que dada una lista de números concatene los números impares en un string, separados por coma, y lo retorne.

#def numeros_impares_juntos(entrada):
#  lista_impares = ""
#  for i in range(len(entrada)):
#    if entrada[i] %2 == 0:
#      continue
#    else:
#      lista_impares += str(entrada[i])+","
#  return lista_impares
#
#print(numeros_impares_juntos([1,2,3,4,5,6]))


#4. Escribir un procedimiento lista_elementos_en_comun(lista1, lista2) que imprima los elementos en común que tienen las listas sin repetirlos.

#def lista_elementos_en_comun(lista1, lista2):
#  lista_comun = []
#  for i in range(len(lista1)):
#    for e in range(len(lista2)):
#      if lista1[i] == lista2[e] and lista1[i] not in lista_comun:
#        lista_comun.append(lista1[i])
#  for i in range(len(lista_comun)):
#    print(lista_comun[i-1])
#        
#lista_elementos_en_comun([1,2,2,2,3,3,3,4,5,"h","l"],[3,"h","l","a",4,5,5,5,6,7,8])

#5. Escribir una función clave_valida(clave) que devuelva True en caso de superar las siguientes validaciones sobre la clave proporcionada por el usuario:
#a. Longitud entre 6 y 20 caracteres.
#b. Debe contener al menos un número.
#c. No puede contener espacios.

#def clave_valida(clave):
#  if(len(clave) < 20 and len(clave)> 6 and any(char.isdigit() for char in clave) and " " not in clave  ):
#    return True
#  return False
#
#print(clave_valida("hola_123"))

#6. Reescribir la siguiente función eliminando la sentencia if/else:
#def persona_mayor_de_edad(edad):
#if edad >= 18:
#return True
#else:
#return False

#def persona_mayor_de_edad(edad):
#  return edad >= 18
#
#print(persona_mayor_de_edad(20))
  
#7. Dado el siguiente script, escriba un procedimiento declarar_comida_favorita(nombre_persona, nombre_comida) con el fin de mejorar la legibilidad del mismo.
#nombre = "Pablo"
#comida_favorita = "pollo frito"
#print("La comida favorita de " + nombre + " se llama: " + comida_favorita)
#nombre = "Pedro"
#comida_favorita = "canelones"
#print("La comida favorita de " + nombre + " se llama: " + comida_favorita)
#nombre = "Juan" Página 3
#comida_favorita = "pizza"
#print("La comida favorita de " + nombre + " se llama: " + comida_favorita)

def declarar_comida_favorita(nombre_persona, nombre_comida):
  print(f"La comida favorita de {nombre_persona} se llama: {nombre_comida} ")

#8. Extraer el procedimiento del ejercicio 7 a un archivo impresiones.py, el cual debe ser importado para su utilización.
#9. Escribir un procedimiento cuenta_regresiva(entero_positivo) que imprima números enteros empezando por el valor pasado por parámetro y llegando hasta 0. Asumir que el número pasado por parámetro es un número entero positivo. Utilizar recursividad para desarrollar la solución.
#10. Simplificar la siguiente expresión:
#(a and b) or True