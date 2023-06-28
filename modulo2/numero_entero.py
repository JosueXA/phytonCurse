def rango_numero( x: int ) -> int:
    if x < 0:
        return -1
    elif x < 1000:
        return 0
    elif x <= 10000:
        return 1
    else:
        return 2

def rango_numero_v2( x: int ) -> int:
    if x < 0:
        respuesta = -1
    elif x < 1000:
        respuesta = 0
    elif x <= 10000:
        respuesta = 1
    else:
        respuesta = 2

    return respuesta