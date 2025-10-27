from empresa import Empresa
from empleado import Empleado
from producto import Producto

# Ejercicio 10

la_solucion_sa = Empresa("La Solución S.A.")

juan_perez = Empleado("Juan", "Pérez")
jose_marmol = Empleado("José", "Marmol")
pedro_picapiedras = Empleado("Pedro", "Picapiedras")

la_solucion_sa.altaEmpleado(juan_perez)
la_solucion_sa.altaEmpleado(jose_marmol)
la_solucion_sa.altaEmpleado(pedro_picapiedras)

solucion_magica = Producto("Solución Mágica")
solucion_ardua = Producto("Solución Ardua")

la_solucion_sa.agregarProducto(solucion_magica)
la_solucion_sa.agregarProducto(solucion_ardua)


la_innovacion_srl = Empresa("La Innovación S.R.L.")

jose_rodriguez = Empleado("José", "Rodríguez")
miguel_fernandez = Empleado("Miguel", "Fernández")
john_mclane = Empleado("John", "McLane")

la_innovacion_srl.altaEmpleado(jose_rodriguez)
la_innovacion_srl.altaEmpleado(miguel_fernandez)
la_innovacion_srl.altaEmpleado(john_mclane)

servicio_facil = Producto("Servicio Fácil")
servicio_dificil = Producto("Servicio Difícil")

la_innovacion_srl.agregarProducto(servicio_facil)
la_innovacion_srl.agregarProducto(servicio_dificil)


la_solucion_sa.bajaEmpleado(juan_perez)
la_solucion_sa.bajaEmpleado(jose_marmol)

la_innovacion_srl.bajaEmpleado(jose_rodriguez)
la_innovacion_srl.bajaEmpleado(miguel_fernandez)

print(str(la_solucion_sa))
print(str(la_innovacion_srl))