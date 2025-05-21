quiere_salir = False
listadoPersonas = []
while quiere_salir == False:
    nombre = input('Ingrese Nombre: ')
    apellido = input('Ingrese Apellido:')
    rol = input('Ingrese Rol: ')
    
    persona = {
        'nombre':nombre,
        'apellido':apellido,
        'rol':rol
    }
    
    listadoPersonas.append(persona)
    quiereSalir = input('Escriba SI si quiere salir, de lo contrario cualquier cosa: ')
    if quiereSalir == 'SI':
        quiere_salir = True


print(listadoPersonas)    