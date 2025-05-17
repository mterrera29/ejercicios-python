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

num1=int(input("ingrese un numero entero positivo "))
i = 0
impares = ""

while i <= num1:
  if i %2 == 0:
    i = i+1
  else:
    impares = impares + str(i)+","
    i = i+1 
    
cuentaAtras = ""

x= num1
while x >= 0:
  cuentaAtras = cuentaAtras + str(x)+","
  x= x-1 
    
print(impares)
print(cuentaAtras)