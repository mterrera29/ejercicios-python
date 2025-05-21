"""
personaDic = {
    'nombre':'Franco',
    'apellido':'Ruis Dias',
    'fec_nac':'18/01/95'
}
personaDic = dict(nombre='Franco', apellido='Ruis Dias', fec_nac='18/01/95')
personaDic = dict([
    ('nombre', 'Franco'),
    ('apellido', 'Ruis Dias'),
    ('fec_nac', '18/01/95'),
])
"""

persona1= {
    'rol':'PROFESOR',
    'nombre':'Franco',
    'apellido':'Ruis Dias',
    'fec_nac':{
        'dia':18,
        'mes':1,
        'anio':1995
        },
    'materias':[
        {
            'nombre':'Prog1',
            'anio':'Primero'
        },
         {
            'nombre':'Desarrollo Movil',
            'anio':'Tercero'
        }]
}

persona2= {
    'rol':'ALUMNO',
    'nombre':'Francisco',
    'apellido':'Pancho',
    'fec_nac':{
        'dia':10,
        'mes':10,
        'anio':1999
    },
    'materias':[
        {
            'nombre':'Prog1',
            'anio':'Primero'
        },
         {
            'nombre':'Introd. Informatica',
            'anio':'Primero'
        }]
}   



listadoPersonas = [persona1, persona2]
listadoAlumnos = []
for persona in listadoPersonas:
    if persona['rol'] == 'ALUMNO':
        listadoAlumnos.append(persona)

#print(listadoAlumnos)
#print(listadoPersonas)