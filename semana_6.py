#1
#fecha = input("introduce una fecha con el siguiente formato dd/m/aaaa")
#dia = fecha[0:2]
#mes = fecha[3:5]
#año = fecha[6:11]
#
#def obtenerMes(m):
#  match m:
#    case "01":
#      return "Enero"
#    case "02":
#      return "Febrero"
#    case "03":
#      return "Marzo"
#    case "04":
#      return "Abril"
#    case "05":
#      return "Mayo"
#    case "06":
#      return "Junio"
#    case "07":
#      return "Julio"
#    case "08":
#      return "Agosto"
#    case "09":
#      return "Septiembre"
#    case "10":
#      return "Octubre"
#    case "11":
#      return "Noviembre"
#    case "12":
#      return "Diciembre"
#    case _:
#      return "Mes"
#    
#nombreMes = obtenerMes(mes)
#
#print(f"{dia} de {nombreMes} de {año}")

#2

#num = int(input("introduce un numero entre 1 y 12"))
#
#i = 1
#
#while i <= 10:
#  result = num * i
#  print(f"{num} x {i} = {result}")
#  i += 1

#3

#num = int(input("introduce un numero de amigos a invitar"))
#
#if num <= 10:
#  for i in range(0,num):
#    amigo = input("introduce el nombre de tu amigo: ")
#    print(f"✔ {amigo} invitado.")
#else:
#  print("Demasiada gente")

#4
##Inicializar total a 0, luego mientras total sea menor o igual a 50 pida al usuario que ingrese
#un número. Sume ese número al total e imprima el mensaje "El total es [total]". Deténgase
#cuando el total supere a 50.
total = 0

#if total <= 50:
#  while total < 50:
#    num = int(input("introduce un numero "))
#    total += num
#    print(f"El total es {total}")

#5
#Un número perfecto es un entero positivo, que es igual a a la suma de todos los enteros
#positivos (excluido el mismo) que son divisores del número. El primer número perfecto es
#6, ya que los divisores de 6 son 1, 2, 3, y 1 + 2 + 3 = 6.
#Para encontrar el máximo común divisor (mcd) de dos números se emplea el algoritmo de
#Euclides, que se puede describir así: Dados los enteros a y b (a > b), se divide a por b,
#obteniendo el cociente q1 y el resto r1. Si r1 != 0, se divide r por b1, obteniendo el cociente
#q2 y el resto r2. Si r2 != 0, se divide r1 por r2, para obtener q1 y r3 y así sucesivamente. Se
#continúa el proceso hasta que se obtiene un resto 0 . El resto anterior es entonces el mcd
#de los números a y b. Escribir un programa que calcule el mcd de dos números.