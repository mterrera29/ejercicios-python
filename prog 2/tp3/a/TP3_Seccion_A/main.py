import item
import caja
import estanteria
import deposito

#Ejercicio 8
deposito1 = deposito.Deposito()

estanteria1 = estanteria.Estanteria()

estanteria2 = estanteria.Estanteria()

deposito1.agregar_estanteria(estanteria1)

deposito1.agregar_estanteria(estanteria2)

caja1 = caja.Caja(30, 40, 30, "cartón")
caja2 = caja.Caja(30, 40, 30, "cartón")
caja3 = caja.Caja(50, 40, 50, "cartón")
caja4 = caja.Caja(30, 40, 30, "cartón")
caja5 = caja.Caja(100, 20, 80, "madera")
caja6 = caja.Caja(50, 40, 50, "cartón")

estanteria1.agregar_caja(caja1)
estanteria1.agregar_caja(caja2)
estanteria1.agregar_caja(caja3)
estanteria2.agregar_caja(caja4)
estanteria2.agregar_caja(caja5)
estanteria2.agregar_caja(caja6)

item1 = item.Item("Caja de chocolate")
item2 = item.Item("Shampoo")
item3 = item.Item("Licuadora")
item4 = item.Item("Shampoo")
item5 = item.Item("Aspiradora")
item6 = item.Item("Cortina")
item7 = item.Item("Frasco de azucar")
item8 = item.Item("Frasco de yerba")
item9 = item.Item("Frasco de azucar")
item10 = item.Item("Jabón")
item11 = item.Item("Licuadora")
item12 = item.Item("Set de cubiertos")

caja1.agregar_item(item1)
caja1.agregar_item(item2)
caja2.agregar_item(item3)
caja2.agregar_item(item4)
caja3.agregar_item(item5)
caja3.agregar_item(item6)
caja4.agregar_item(item7)
caja4.agregar_item(item8)
caja5.agregar_item(item9)
caja5.agregar_item(item10)
caja6.agregar_item(item11)
caja6.agregar_item(item12)

#Ejercicio 9
print("Ejercicio 9")

print(str(deposito1))

#Ejercicio 10
print("Ejercicio 10")

estanteria1.remover_caja(caja1)
estanteria2.agregar_caja(caja1)

print(deposito1)