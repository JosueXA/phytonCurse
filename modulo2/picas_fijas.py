def picas_y_fijas ( numero_secreto: int, intento: int ) -> dict:
    """ Devuelve un diccionario que represente el resultado de la jugada si un jugador trata de
        adivinar el numero_secreto con el número intento
    
    Parámetros:
        numero_secreto: Número por adivinar
        intento: Número con el cual se intenta adivinar
    Retorno:
        pi_fi: Diccionario con las llaves "PICAS" y "FIJAS" que describen el resultado del intento
    """
    pi_fi = { "PICAS":  0, "FIJAS": 0 }

    cadena_numero_secreto = str( numero_secreto )
    cadena_intento = str( intento )

    print( cadena_numero_secreto )
    print( cadena_intento )

    for num_s in range( len(cadena_numero_secreto) ):
        
        print( cadena_numero_secreto[num_s] , cadena_intento[num_s] )
        print( cadena_numero_secreto[num_s] in cadena_intento )

        if cadena_numero_secreto[num_s] == cadena_intento[num_s]:
            pi_fi["FIJAS"] += 1
        elif cadena_numero_secreto[num_s] in cadena_intento:
            pi_fi["PICAS"] += 1
        
    return pi_fi
            



print(picas_y_fijas(1234, 1325))

