# Ejemplo de condicionales optimizando la forma en que se escribe el código
def mayor_v1( a: int, b: int, c: int, d: int ) -> int:
    if (a >= b) and (a >= c) and (a >= d):
        return a
    elif (b >= a) and (b >= c) and (b >= d):
        return b
    elif (c >= a) and (c >= b) and (c >= d):
        return c
    else:
        return d

def mayor_v2( a: int, b: int, c: int, d: int ) -> int:
    if (a >= b) and (a >= c) and (a >= d):
        respuesta = a
    elif (b >= a) and (b >= c) and (b >= d):
        respuesta = b
    elif (c >= a) and (c >= b) and (c >= d):
        respuesta = c
    else:
        respuesta = d

    return respuesta

def mayor_optimo( a: int, b: int, c: int, d: int ) -> int:
    mayor = a
    if ( b > mayor ):
        mayor = b
    if ( c > mayor ):
        mayor = c
    if ( d > mayor ):
        mayor = d

    return mayor

def es_positivo_de_un_solo_digito_v1( x: int ) -> bool:
    if x > 0:
        if x < 10:
            respuesta = True
        else:
            respuesta = False
    else:
        respuesta = False
    return respuesta

def es_positivo_de_un_solo_digito_v2( x: int ) -> bool:
    respuesta = False
    if x > 0 and x < 10:
        respuesta = True
    return respuesta

def es_positivo_de_un_solo_digito_v3( x: int ) -> bool:
    return x > 0 and x < 10

def puede_tener_credencial_conducir_v1(edad: int) -> bool:
    if not (edad >= 18):
        return False
    else:
        return True

def puede_tener_credencial_conducir_v2(edad: int) -> bool:
    if (edad < 16):
        return False
    else:
        return True

def puede_tener_credencial_conducir_v3(edad: int) -> bool:
    puede = True
    if (edad < 16):
        puede = False
    return puede

def puede_tener_credencial_conducir_v4(edad: int) -> bool:
    puede = False
    if (edad >= 16):
        puede = True
    return puede

def puede_tener_credencial_conducir_v5(edad: int) -> bool:
    return (edad >= 16)