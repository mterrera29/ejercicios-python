#1
#print("Hola Mundo! Esto es Python!")

#2
#nombre = input("Ingresa tu nombre:")
#print("Hola "+ nombre)

#3
#nombre3 = input("Ingresa tu nombre:")
#apellido3 = input("Ingresa tu apellido:")
#print("Hola "+ nombre3 +" "+ apellido3)

#4
#numero1 = int(input("Ingresa un número:"))
#numero2 = int(input("Ingresa otro número:"))
#result = numero1+numero2
#print("el resultado es",result)

#5
#numero1 = int(input("Ingresa un número:"))
#numero2 = int(input("Ingresa otro número:"))
#numero3 = int(input("Ingresa otro número:"))
#result= (numero1 +numero2)* numero3
#print("el resultado es",result)

#6
#totalCuenta = int(input("Total de la cuenta:"))
#totalComensales = int(input("Total de comensales:"))
#result= totalCuenta/totalComensales
#print("Cada persona debe pagar:","$",result )

#7
#numeroDeDias = int(input("Número de días:"))
#horas = numeroDeDias *24
#minutos = horas *60
#segundos= minutos *6010
#print("Cantidad de días:", numeroDeDias,", horas:",horas,", minutos:", minutos, ",segundos:", segundos)

#8
#base = float(input("Ingresar la base del triangulo:"))
#altura = float(input("Ingresar la altura del triangulo:"))
#superficie = (base*altura)/2
#print("La superficie del triángulo es:", superficie)

#9
#palabra = input("Ingresar una palabra:")
#palabra[::-1]
#print(palabra[::-1])

#10
#palabra = input("Ingresar una palabra:")
#palabra2 = palabra[::-1]
#
#if palabra == palabra2:
#  print(palabra, "es palíndromo.")
#else:
#  print(palabra, "no es palíndromo.")
  
#11
#palabra = input("Ingresar una palabra:")
#print(palabra[0:5])

#12
#palabra = input("Ingresar una fecha en formato dd/mm/aaaa: ")
#dia= palabra[0:2]
#mes=palabra[3:5]
#año=palabra[6:10]
#print(f"Día: {dia}, Mes: {mes} y Año: {año}.")

#13
#nombre = input("Ingresar su nombre:")
#apellido = input("Ingresar su apellido:")
#año = input("Ingresar su año de nacimiento:")
#usuario= nombre[0:1]+apellido
#contraseña= nombre[0:1]+apellido[0:1]+"."+año
#print(f"Sugerencia de usuario: {usuario}.\nSugerencia de contraseña: {contraseña}")

print(10 > 20 and 5 <=15 or 3**2 > 8)