def crear_estudiante ( nom: str, cod: str, gen: str, carr: str, prom: float, ssc: float ) -> dict:
    dic_estudiante = {
        "nombre": nom,
        "código": cod,
        "género": gen,
        "carrera": carr,
        "promedio": prom,
        "ssc": ssc
    }

    return dic_estudiante

# Programa Principal
estudiante1 = crear_estudiante("Juan Peréz", "201824736", "masculino", "Biología", 3.78, 0.7 )
estudiante2 = crear_estudiante("Ana Gavalda", "201724736", "femenino", "Ciencias Políticas", 4.25, 3.5 )
estudiante3 = crear_estudiante("Bastien Bosa", "201815217", "masculino", "Economía", 3.21, 2.3 )
estudiante4 = crear_estudiante("Catalina Gómez", "2017154000", "femenino", "Arte", 3.8, 4 )

print("Los estudiantes son:\n","Estudiante 1:\n", estudiante1 ,"\nEstudiante 2:\n", estudiante2,"\nEstudiante 3:\n", estudiante3,"\nEstudiante 4:\n", estudiante4)

def mayor_promedio ( est1: dict, est2: dict, est3: dict, est4: dict ) -> dict:
    mayor = est1

    if ( est2["promedio"] >= mayor["promedio"] ):
        mayor = est2

    if ( est3["promedio"] >= mayor["promedio"] ):
        mayor = est3

    if ( est4["promedio"] >= mayor["promedio"] ):
        mayor = est3

    return mayor

mejor = mayor_promedio( estudiante1, estudiante2, estudiante3, estudiante4 )

print("El estudiante de mayor promedio es: " + mejor["nombre"] + " y su promedio es: " + str( mejor["promedio"] ))

def cuantas_mujeres ( est1: dict, est2: dict, est3: dict, est4: dict ) -> int:
    cuantas = 0

    if ( est1["género"] == "femenino" ):
        cuantas += 1
        
    if ( est2["género"] == "femenino" ):
        cuantas += 1

    if ( est3["género"] == "femenino" ):
        cuantas += 1

    if ( est4["género"] == "femenino" ):
        cuantas += 1
    
    return cuantas

cuantas = cuantas_mujeres( estudiante1, estudiante2, estudiante3, estudiante4 )

print("Entre los 4 estudiantes hay: ", cuantas , "mujeres")

def hay_mujer_pila ( est1: dict, est2: dict, est3: dict, est4: dict ) -> bool:
    hay = False

    if ( est1["género"] == "femenino" and est1["promedio"] >= 4 ):
        hay = True
    elif ( est2["género"] == "femenino" and est2["promedio"] >= 4 ):
        hay = True
    elif ( est3["género"] == "femenino" and est3["promedio"] >= 4 ):
        hay = True
    elif ( est3["género"] == "femenino" and est3["promedio"] >= 4 ):
        hay = True

    return hay

# Con variable sin ==
var_hay = hay_mujer_pila( estudiante1, estudiante2, estudiante3, estudiante4 )
if (var_hay):
    print("Si hay una mujer en la pila")
else:
    print("No hay una mujer en la pila")

# Sin variable  
if (hay_mujer_pila( estudiante1, estudiante2, estudiante3, estudiante4 ) == True):
    print("Si hay una mujer en la pila")
else:
    print("No hay una mujer en la pila")

# Sin variable y sin ==
if (hay_mujer_pila( estudiante1, estudiante2, estudiante3, estudiante4 )):
    print("Si hay una mujer en la pila")
else:
    print("No hay una mujer en la pila")