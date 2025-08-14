x = (0 or "casa" and 8)
print(x)

lista=["a","b","juan","ejemplo"]

print(lista[0])

var1 = 9
var1 = str(var1)
print(
type(var1))
print('Mi', 'nombre', 'es', 'Nicolas', sep='#')

num = 968.19893842
print('%.2f' % num)

variable = [1,2,3,4,5]
for i in range(len(variable)):
    variable[i] += 1
print(variable)

valores = []
for numero in range(200, 211):
    numero_texto = str(numero)
    if (int(numero_texto[0])%2==0) and (int(numero_texto[1])%2==0) and (int(numero_texto[2])%2==0):
        valores.append(numero_texto)
print(", ".join(valores))


numeros=[]
for numero in range(0, 51):
    if (numero % 7 == 0) and (numero * 5 == 0):
        numeros.append(str(numero))
print(", ".join(numeros))

n = 8
diccionario = dict()
for i in range(1, n + 1):
    diccionario[i] = i * i
print(diccionario)