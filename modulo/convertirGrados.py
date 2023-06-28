# Función que convierte grados celsius a grados fahrenheit

def fahrenheit_a_centigrados( grados_f: float ) -> float:
    grados_cent = ( grados_f - 32 ) * ( 5/9 )
    return grados_cent

print('Convierte grados Fahrenheit a grados Celsius')

gradosF = float(input('Ingrese los grados Fahrenheit a convertir: '))

gradosC = fahrenheit_a_centigrados(gradosF)

print('El resultados de convertir', str(gradosF) ,'grados Fahrenheit es:', str(gradosC) ,'grados Celsius')


# Función que convierte grados fahrenheit a grados celsius
def centigrados_a_fahrenheit( grados_c: float ) -> float:
    grados_f = ( grados_c * 9/5 ) + 32
    return grados_f

print('Convierte grados Celsius a grados Fahrenheit')

gradosC = float(input('Ingrese los grados Celsius a convertir: '))

gradosF = centigrados_a_fahrenheit(gradosC)

print('El resultados de convertir', str(gradosC) ,'grados Celsius es:', str(gradosF) ,'grados Fahrenheit')

# Función que convierte radianes a grados
def radianes_a_grados( radianes: float ) -> float:
    pi = 3.14159
    return ( 360 * radianes ) / ( 2 * pi )

print('Convierte radianes a grados')

radianes = float(input('Ingrese los radianes a convertir: '))

grados = radianes_a_grados(radianes)

print('El resultados de convertir', str(radianes) ,'radianes son:', str(grados) ,'grados')

# Función que convierte grados a radianes
def grados_a_radiantes( grados: float ) -> float:
    pi = 3.14159
    rad = ( 2 * pi * grados ) / 360
    return rad

print('Convierte grados a radianes')

grados = float(input('Ingrese los grados a convertir: '))

radianes = grados_a_radiantes(grados)

print('El resultados de convertir', str(grados) ,'radianes son:', str(radianes) ,'grados')

# Función invertir un número de 4 dígitos 
def invertir_numero( numero: int ) -> int:
    unidades = numero % 10
    numero //= 10
    decenas = numero % 10
    numero //= 10
    centenas = numero % 10
    numero //= 10
    millares = numero % 10

    # inverso = (unidades * 1000 ) + ( decenas * 100 ) + ( centenas * 10 ) + millares
    inverso = str(unidades) + str(decenas) + str(centenas) + str(millares)
    return inverso

print('Invierte un número de 4 dígitos')

num = int(input('Ingrese un número de 4 dígitos: '))

num_invertido = invertir_numero(num)

print('El resultados del número', str(num) ,'invertido es:', str(num_invertido))