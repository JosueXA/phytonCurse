###############################################################
# Primera versión
"""
numero = int( input( 'Dígite el número de 10 cifras: ' ) )

conteo = {}

digito = numero % 10

if digito in conteo:
    conteo[digito] += 1
else:
    conteo[digito] = 1

numero = numero // 10

digito = numero % 10

if digito in conteo:
    conteo[digito] += 1
else:
    conteo[digito] = 1

numero = numero // 10

digito = numero % 10

if digito in conteo:
    conteo[digito] += 1
else:
    conteo[digito] = 1

numero = numero // 10

digito = numero % 10

if digito in conteo:
    conteo[digito] += 1
else:
    conteo[digito] = 1

numero = numero // 10

digito = numero % 10

if digito in conteo:
    conteo[digito] += 1
else:
    conteo[digito] = 1

numero = numero // 10

digito = numero % 10

if digito in conteo:
    conteo[digito] += 1
else:
    conteo[digito] = 1

numero = numero // 10

digito = numero % 10

if digito in conteo:
    conteo[digito] += 1
else:
    conteo[digito] = 1

numero = numero // 10

digito = numero % 10

if digito in conteo:
    conteo[digito] += 1
else:
    conteo[digito] = 1

numero = numero // 10

digito = numero % 10

if digito in conteo:
    conteo[digito] += 1
else:
    conteo[digito] = 1

numero = numero // 10

digito = numero % 10

if digito in conteo:
    conteo[digito] += 1
else:
    conteo[digito] = 1

numero = numero // 10

print( conteo )
"""
###############################################################
# Segunda versión
"""
def contar( num: int, diccionario: dict ) -> dict:
    digito = num % 10

    if digito in diccionario:
        diccionario[digito] +=1
    else:
        diccionario[digito] = 1
    
    return diccionario

# Programa principal
numero = int( input( 'Dígite el número de 10 cifras: ' ) )

conteo = {}

# Repetición 1
conteo = contar( numero, conteo )

numero = numero // 10
# Repetición 2
conteo = contar( numero, conteo )

numero = numero // 10
# Repetición 3
conteo = contar( numero, conteo )

numero = numero // 10
# Repetición 4
conteo = contar( numero, conteo )

numero = numero // 10
# Repetición 5
conteo = contar( numero, conteo )

numero = numero // 10
# Repetición 6
conteo = contar( numero, conteo )

numero = numero // 10
# Repetición 7
conteo = contar( numero, conteo )

numero = numero // 10
# Repetición 8
conteo = contar( numero, conteo )

numero = numero // 10
# Repetición 9
conteo = contar( numero, conteo )

numero = numero // 10
# Repetición 10
conteo = contar( numero, conteo )
"""

###############################################################
# Tercera versión
"""
def contar( num: int, diccionario: dict ) -> int:
    digito = num % 10

    if digito in diccionario:
        diccionario[digito] +=1
    else:
        diccionario[digito] = 1
    
    return num // 10

# Programa principal
numero = int( input( 'Dígite el número de 10 cifras: ' ) )

conteo = {}

numero = contar( numero, conteo )
numero = contar( numero, conteo )
numero = contar( numero, conteo )
numero = contar( numero, conteo )
numero = contar( numero, conteo )
numero = contar( numero, conteo )
numero = contar( numero, conteo )
numero = contar( numero, conteo )
numero = contar( numero, conteo )
numero = contar( numero, conteo )

print( conteo )
"""

###############################################################
# Cuarta versión
def contar( num: int, diccionario: dict ) -> int:
    digito = num % 10

    diccionario[digito] = diccionario.get(digito, 0) + 1
    
    return num // 10

# Programa principal
numero = int( input( 'Dígite el número de 10 cifras: ' ) )

conteo = {}

numero = contar( numero, conteo )
numero = contar( numero, conteo )
numero = contar( numero, conteo )
numero = contar( numero, conteo )
numero = contar( numero, conteo )
numero = contar( numero, conteo )
numero = contar( numero, conteo )
numero = contar( numero, conteo )
numero = contar( numero, conteo )
numero = contar( numero, conteo )

print( conteo )
