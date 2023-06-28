def movimiento_robot ( orientacion_actual: str, giro_1: str, giro_2: str, giro_3: str ) -> str:
    """ Función que envía 3 comandos usando el control remoto, calcula la orientación final del robot

    Parámetros:
        orientacion_actual: Orientación actual del robot
        giro_1: Primer comando de giro
        giro_2: Segundo comando de giro
        giro_3: Tercer comando de giro
    Retorno:
        orientacion_final: Orientación final del robot
    """
    orientacion_1 = validar_giro( orientacion_actual, giro_1 )
    orientacion_2 = validar_giro( orientacion_1, giro_2 )
    orientacion_final = validar_giro( orientacion_2, giro_3 )
    
    return orientacion_final


def validar_giro( orientacion: str, giro: str ) -> str:
    """ Verifica el giro que realizo el robot

    Parámetros:
        orientacion: Orientacion del robot
        giro: El comando de giro
    Retorno:
        orientacion_f: El cambio de orientación que hizo con el giro
    """
    if (orientacion == "N" and giro == "L") or (orientacion == "S" and giro == "R") or (orientacion == "E" and giro == "H") or (orientacion == "W" and giro == "."):
        orientacion_f = "W"
    elif (orientacion == "E" and giro == "L") or (orientacion == "W" and giro == "R") or (orientacion == "S" and giro == "H") or (orientacion == "N" and giro == "."):
        orientacion_f = "N"
    elif (orientacion == "S" and giro == "L") or (orientacion == "N" and giro == "R") or (orientacion == "W" and giro == "H") or (orientacion == "E" and giro == "."):
        orientacion_f = "E"
    elif (orientacion == "W" and giro == "L") or (orientacion == "E" and giro == "R") or (orientacion == "N" and giro == "H") or (orientacion == "S" and giro == "."):
        orientacion_f = "S"
    return orientacion_f

print( movimiento_robot( 'N', 'L', 'H', 'R' ) )
