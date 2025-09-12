#Sección a (para ver en clase):
#1. Escribir un procedimiento recibir(). El mismo debe solicitar al usuario ingresar su nombre por consola e imprimir “Hola [nombre]”.

#def recibir():
#  nombre = input("ingrese su nombre: ")
#  print(f"Hola {nombre}!")
# 
#recibir()
  
#2. Escribir una función numero_no_contiene_digitos(numero, digitos_prohibidos), que retorne True si es que los dígitos que componen el número no se encuentran en una lista de dígitos prohibidos. Asumir que los valores pasados por parámetro son de un tipo válido.

#def numero_no_contiene_digitos(numero, digitos_prohibidos):
#  numberList = list(str(numero))
#  print(numberList)
#  if str(digitos_prohibidos) in numberList:
#    return True
#print(numero_no_contiene_digitos(15,1))

#3. Escribir una función invertir_palabras(entrada) que acepte una secuencia de palabras separadas por coma, la revierta, y la retorne. Suponiendo que la entrada provista al programa es la siguiente:
#el,día,está,soleado
#La salida esperada es:
#soleado,está,día,el

#palabras = "el,día,está,soleado"
#
#def invertir_palabras(entrada):
#  palabraList = entrada.split(",")
#  palabraList.reverse()
#  reverseList= ",".join(palabraList)
#  return reverseList
#  
#print(invertir_palabras(palabras))
  

#4. Escribir un procedimiento numeros_pares_elevados(entrada) que dado una lista de números eleve cada elemento par al cuadrado, los mueva a otra lista, e imprima dicha lista. Asumir que el parámetro es una lista de números positivos válida.

#lista= [1,5,6,45,8,2,7]
#
#def numeros_pares_elevados(entrada):
#  numList =[]
#  for i in range(len(entrada)):
#    if entrada[i] % 2 == 0:
#      num = entrada[i] ** 2
#      numList.append(num)
#  print(numList)
#  
#numeros_pares_elevados(lista)

#5. Escribir una función edad_valida(edad) que devuelva True si el valor pasado por parámetro es de tipo int, y si el mismo es mayor a 1 y menor a 120.

#def edad_valida(edad):
#  if type(edad) == int and edad > 1 and edad < 120:
#    return True
#  
#print(edad_valida(130))

#6. Reescribir la siguiente función eliminando la sentencia if/else y utilizando in en vez de or. Asumir que el parámetro es un valor válido.

#def es_fin_de_semana(dia):
#  if dia == 1 or dia == 7:
#    return True
#  else:
#    return False

#def es_fin_de_semana(dia):
#  return dia in [1,7]
#  
#print(es_fin_de_semana(6))

#7. Dado el siguiente script, escribir una función calcular_hipotenusa(cateto1, cateto2) para aplicar el teorema de pitágoras con el fin de mejorar la legibilidad del mismo. La función debe retornar el valor calculado para la hipotenusa. Incluir una validación para verificar que los catetos tienen longitud mayor a 0.

#cateto1 = 5
#cateto2 = 4
#hipotenusa = (cateto1 ** 2 + cateto2 **2) ** 0.5
#print(hipotenusa)
#cateto1 = 3
#cateto2 = 3
#hipotenusa = (cateto1 ** 2 + cateto2 **2) ** 0.5
#print(hipotenusa)
#cateto1 = 7
#cateto2 = 11.5
#hipotenusa = (cateto1 ** 2 + cateto2 **2) ** 0.5
#print(hipotenusa)

#def calcular_hipotenusa(cateto1, cateto2):
#  if (cateto1 > 0 and cateto2>0):
#    return (cateto1 ** 2 + cateto2 **2) ** 0.5
#
#print(calcular_hipotenusa(5,6))

#8. Extraer la función del ejercicio 7 a un archivo pitagoras.py, el cual debe ser importado para su utilización.

#from pitagoras import calcular_hipotenusa
#
#print(calcular_hipotenusa(5,6))

#9. Escribir un procedimiento suma(entero_positivo) que imprima la suma de los números enteros por los que hay que pasar hasta llegar al número pasado por parámetro (incluido el mismo). Asumir que el número pasado por parámetro es un número entero positivo. Utilizar recursividad para desarrollar la solución.

def suma(entero_positivo):
  if entero_positivo == 1:
    return 1
  else:
    total = entero_positivo + suma(entero_positivo - 1)
    return total
  
print(suma(5))



#10. Simplificar la siguiente expresión:
#(a or b) and False

