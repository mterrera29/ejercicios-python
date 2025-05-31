import math

#1. Que al pasarle una cadena <nombre> nos muestre por pantalla el saludo ¡Hola <nombre>!.

#num=(input("introduce tu nombre: "))
#def saludar(nom):
#  print(f"Hola {nom}!")
#  
#saludar(num)



#2. Que reciba un número entero positivo y una potencia a elevar y que nos devuelva el
#resultado.

#100numero=int(input("introduce un numero positivo: "))
#100potencia=int(input("introduce su potencia: "))
#100
#100def funcion(num, pot):
#100  if num < 0:
#100    print("el número debe ser positivo")
#100    return
#100  resultado= numero ** potencia
#100  print(resultado)
#100  
#100funcion(numero,potencia)

#3. Que nos calcule el total de una factura tras aplicarle el IVA. La función debe recibir la
#cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca
#la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

#totalFactura=int(input("introduce el total de la factura: "))
#IVA=int(input("introduce porcentaje de IVA: "))
#
#def funcion(total, impuestos =21):
#  if (impuestos == 21):
#    resultado= total * (21 /100)
#    print(total +resultado)
#  else:
#    resultado= total * (impuestos /100)
#    print(total +resultado)
#  
#funcion(totalFactura)

#4. Que dada la base y altura de un triángulo nos calcule su área.

#base=int(input("introduce el total de la factura: "))
#altura=int(input("introduce el total de la factura: "))
#def area(base, altura):
#  areaTriangulo = base*altura
#  print(f"el area del triangulo es {areaTriangulo}")
#  
#area(base,altura)
  
#5. Que dado tres números ingresados por el usuario nos devuelva el promedio.

#num1=int(input("introduce un num: "))
#num2=int(input("introduce un num: "))
#num3=int(input("introduce un num: "))
#def promedio(num1, num2, num3):
#  promedio = (num1+num2+num3)/3
#  print(f"el promedio es {promedio}")
#  
#promedio(num1, num2, num3)

#En esta segunda parte deberán utilizar estructuras de control condicionales (y en lo posible y dado el
#caso funciones) para escribir programas que lleven a cabo lo siguiente:
#6. Que pida al usuario una palabra y la muestre por pantalla 10 veces.

#palabra=input("ingrese una palabra: ")
#def repetirPalabra(palabra):
#  print(palabra*10)
#  
#repetirPalabra(palabra)

#7. Que imprima todos los números entre el 100 y el 199.
#num = 100
#while num <= 199:
#  print(num)
#  num = num+1
#

#8. Pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
#edad=int(input("ingrese su edad: "))
#
#if edad >= 18:
#  print("es mayor")
#else:
#  print("es menor")

#9. Que el usuario ingrese dos números y muestre cuál de los dos es menor. Considerar el caso
#en que ambos números son iguales.
#num1=int(input("ingrese un numero: "))
#num2=int(input("ingrese otro numero: "))
#
#if num1 > num2:
#  print(f"{num2} es menor")
#elif num1 < num2:
#  print(f"{num1} es menor")
#else:
#  print("son iguales")

#10. Que el usuario ingrese un número entero positivo y muestre por pantalla lo siguiente:
#a. Todos los números impares desde 1 hasta ese número separados por comas.
#b. La cuenta atrás desde ese número hasta cero separados por comas.
#c. Que indique si es primo o no.
#d. Por último, su factorial.

#num1=int(input("ingrese un numero entero positivo "))
#i = 0
#impares = ""
#
#while i <= num1:
#  if i %2 == 0:
#    i = i+1
#  else:
#    impares = impares + str(i)+","
#    i = i+1 
#    
#cuentaAtras = ""
#
#x= num1
#while x >= 0:
#  cuentaAtras = cuentaAtras + str(x)+","
#  x= x-1 
#
#def es_primo(n):
#  if num1 < 2:
#    return "no es primo"
#  for i in range(2, int(math.sqrt(n)) + 1):
#    if n % i == 0:
#      return "no es primo" 
#  return "es primo"
#
#def factorial(n):
#  resultado = 1
#  for i in range(1, n +1):
#    print(i)
#    resultado = resultado * i
#  print(resultado)
#    
#print(impares)
#print(cuentaAtras)
#print(es_primo(num1))
#factorial(num1)

#11. Que solicite al usuario ingresar una frase. Luego, que imprima la cantidad de vocales que se
#encuentran en dicha frase.

#frase=input("ingresar una frase ")
#
#def contar_vocales(fras):
#  cantidad= 0
#  vocales = "aeiou"
#  for i in range(len(fras)):
#    for x in range(len(vocales)):
#      if fras[i] == vocales[x]:
#       cantidad+= 1
#  print(f"la cantidad de vocales de la palabra es {cantidad}")
#
#contar_vocales(frase)

#12. Pedir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro
#mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día
#frase=input("ingresar un día de la semana: ")
#
#dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
#saludos_semana = ["que arranques muy bien la semana", "que comienzes muy bien el día", "ya estas a mitad de semana!", "vamos que amañana es viernes a aguantar hoy!", "hoy es VIERNESSS", "hoy se pica", "a descansar como lo hizo Dios"]
#
#def saludo(mensaje):
#  if mensaje.lower() in dias_semana:
#    for i in range(len(dias_semana)):
#      if mensaje.lower() == dias_semana[i]:
#        print(saludos_semana[i])
#  else:
#    print("no ingresaste un día de semana")
#    
#saludo(frase)

#ingresado no es ninguno de esos, imprimir otro mensaje.
#13. Que resuelva el siguiente problema: los alumnos de un curso se han dividido en dos grupos
#A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un
#nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el
#resto. Escribir un programa que pregunte al usuario su nombre y sexo y muestre por pantalla
#el grupo que le corresponde.

#nombre_alumno=input("ingresar un nombre ")
#sexo_alumno=input("ingresar sexo ")
#
#def definir_grupo(nombre, sexo):
#  grupo_a= False
#  if sexo == "mujer":
#    if nombre[0] < "m" :
#      grupo_a= True
#  if sexo == "hombre":
#    if nombre[0] > "n" :
#      grupo_a= True
#  if grupo_a:
#    return print("perteneces al grupo A")
#  else:
#    return print("perteneces al grupo B")
#
#definir_grupo(nombre_alumno, sexo_alumno)
  
  
#14. Que pida un año y que escriba si es bisiesto o no. Les recordamos que los años bisiestos son
#múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. Algunos
#ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900
#no es bisiesto.

#anio=int(input("ingresar un año: "))
#
#def bisiesto(an):
#  if (an % 4 == 0 and an % 100 != 0) or (an % 400 == 0):
#    print("es bisiesto")
#  else:
#    print("no es bisiesto")
#bisiesto(anio)

#15. Que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”. Se debe
#validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter,
#informarle que no se puede procesar el dato.

#letra=input("ingresar una letra: ")
#vocales = "aeiou"
#
#def es_vocal(let):
#  if(len(let)>1):
#    print("debes ingresar un solo caracter")
#  else:
#    if(let in vocales):
#      print("es vocal")
#    else:
#      print("no es vocal")
#
#es_vocal(letra)
#

#tuplex = (4, 6, 2, 8, 3, 1)
#
#tuplex = tuplex[:5] + (15, 20, 25) + tuplex[:5] 
#
#print(tuplex)

prueba_deportiva={'Jorge':500,'Diana':600,'Rodrigo':800,'Julia':750,'Liliana':900}
print(prueba_deportiva.keys())