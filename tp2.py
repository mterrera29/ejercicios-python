
#1
#num1 = float(input("Ingresar un numero:"))
#num2 = float(input("Ingresar otro numero:"))
#suma = num1 + num2
#print(suma)
#num3 = float(input("Ingresar otro numero:"))
#operacion = num3/suma
#print(operacion)

#2
#num1 = int(input("Ingresar un numero:"))
#print(num1 % 2 == 0)
 
#3 
#text = input("Ingresar un texto:")
#numText = int(len(text))
#print(numText % 2 == 0)

#4
#tarifa_horaria = float(input("Ingresar la tarifa horaria:"))
#horas_trabajadas = float(input("Ingresar las horas trabajadas por día:"))
#salario = (tarifa_horaria * horas_trabajadas) *5
#print(f"El salario semanal es: {salario}$")

#5
#num1 = int(input("Ingresar un numero de tres digitos:"))
#num2 = int(input("Ingresar otro numero de tres digitos:"))
#resultado= num1 * num2
#unidad= int(str(num2)[-1])
#decena= int(str(num2)[-2])
#centena= int(str(num2)[-3])
#print(f"  {num1}\n* {num2}\n______\n{num1*unidad}\n{num1*decena}\n{num1*centena}\n{num1*num2}")

#6
#c1 =int(input("Ingresar un lado del triangulo:"))
#c2=int(input("Ingresar otro lado del triangulo:"))
#
#hipotenusa = (c2**2+c1**2)**0.5
#print(f"la hipotenusa es {hipotenusa}")

#7
#def esMayor (num1,num2):
#  if num1 > num2:
#    return"Es mayor"
#  else:
#    return"No es mayor"
#print(esMayor(9,5))

#8
#def promedio (num1,num2,num3):
#  operacion = (num1 + num2 +num3)/3
#  return operacion
#print(promedio(3,4,6))

#9

#def imprimirCaracteres (cant):
#  return "*"*cant
#print(imprimirCaracteres(20))

def imprimir_nombre(nombre):
    print(nombre)

imprimir_nombre('Programación 1 ' * 4)