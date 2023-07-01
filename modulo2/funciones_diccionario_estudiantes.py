def buscar_estudiante ( est1: dict, est2: dict, est3: dict, est4: dict, nom: str ) -> dict:
    buscado = None

    if est1['nombre'] == nom:
        buscado = est1
    elif est2['nombre'] == nom:
        buscado = est2
    elif est3['nombre'] == nom:
        buscado = est3
    elif est4['nombre'] == nom:
        buscado = est4
    
    return buscado

# Programa Principal
e_1 = { 'nombre': 'Lina', 'codigo': '2020101234', 'genero': 'femenino', 'carrera': 'Sistemas', 'promedio': 4.78, 'ssc': 2 }
e_2 = { 'nombre': 'Laura', 'codigo': '2020105678', 'genero': 'femenino', 'carrera': 'Civil', 'promedio': 4.21, 'ssc': 2 }
e_3 = { 'nombre': 'Felipe', 'codigo': '2020109012', 'genero': 'masculino', 'carrera': 'Sistemas', 'promedio': 4.9, 'ssc': 2 }
e_4 = { 'nombre': 'Carlos', 'codigo': '2020103456', 'genero': 'masculino', 'carrera': 'Economia', 'promedio': 3.89, 'ssc': 2 }

nombre = input('Ingrese el nombre del estudiante a buscar: ')

est_buscado = buscar_estudiante( e_1, e_2, e_3, e_4, nombre )

if est_buscado is None:
    print('El estudiante no existe')
else:
    print('El estudiante existe y su codigo es:', est_buscado['codigo'] )


def avanzar_semestre ( est1: dict, est2: dict, est3: dict, est4: dict ) -> None:
    est1['ssc'] += 1
    est2['ssc'] += 1
    est3['ssc'] += 1
    est4['ssc'] += 1

# Programa Principal
e_1 = { 'nombre': 'Lina', 'codigo': '2020101234', 'genero': 'femenino', 'carrera': 'Sistemas', 'promedio': 4.78, 'ssc': 4 }
e_2 = { 'nombre': 'Laura', 'codigo': '2020105678', 'genero': 'femenino', 'carrera': 'Civil', 'promedio': 4.21, 'ssc': 1 }
e_3 = { 'nombre': 'Felipe', 'codigo': '2020109012', 'genero': 'masculino', 'carrera': 'Sistemas', 'promedio': 4.9, 'ssc': 2 }
e_4 = { 'nombre': 'Carlos', 'codigo': '2020103456', 'genero': 'masculino', 'carrera': 'Economia', 'promedio': 3.89, 'ssc': 3 }

print('Semester estudiante 1:', e_1['ssc'])
print('Semester estudiante 2:', e_2['ssc'])
print('Semester estudiante 3:', e_3['ssc'])
print('Semester estudiante 4:', e_4['ssc'])

avanzar_semestre( e_1, e_2, e_3, e_4 )

print('Nuevo semester estudiante 1:', e_1['ssc'])
print('Nuevo semester estudiante 2:', e_2['ssc'])
print('Nuevo semester estudiante 3:', e_3['ssc'])
print('Nuevo semester estudiante 4:', e_4['ssc'])

def quienes_en_riesgo ( est1: dict, est2: dict, est3: dict, est4: dict ) -> dict:
    en_riesgo = {}

    if est1['promedio'] < 3.4:
        en_riesgo[est1['codigo']] = est1['promedio']
    if est2['promedio'] < 3.4:
        en_riesgo[est2['codigo']] = est2['promedio']
    if est3['promedio'] < 3.4:
        en_riesgo[est3['codigo']] = est3['promedio']
    if est4['promedio'] < 3.4:
        en_riesgo[est4['codigo']] = est4['promedio']

    return en_riesgo

# Programa Principal
e_1 = { 'nombre': 'Lina', 'codigo': '2020101234', 'genero': 'femenino', 'carrera': 'Sistemas', 'promedio': 4.78, 'ssc': 2 }
e_2 = { 'nombre': 'Laura', 'codigo': '2020105678', 'genero': 'femenino', 'carrera': 'Civil', 'promedio': 3.29, 'ssc': 2 }
e_3 = { 'nombre': 'Felipe', 'codigo': '2020109012', 'genero': 'masculino', 'carrera': 'Sistemas', 'promedio': 4.9, 'ssc': 2 }
e_4 = { 'nombre': 'Carlos', 'codigo': '2020103456', 'genero': 'masculino', 'carrera': 'Economia', 'promedio': 3.2, 'ssc': 2 }

riesgo = quienes_en_riesgo( e_1, e_2, e_3, e_4 )

print( riesgo )
