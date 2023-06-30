

def clasificar_regalo ( id: int ) -> str:
    """ Calcular, dado un identificador único de regalo, a que tipo de persona corresponde dicho regalo

    Parámetros:
        id: Identificador del regalo cuyo tipo de persona se quiere calcular
    
    Retorno:
        respuesta: Si el número es palíndromo e impar, retorna "girl"
                    Si el número es palíndromo y par, retorna "boy"
                    Si el número es par, pero no es palíndromo, retorna "man"
                    Si el número es impar, pero no es palíndromo, retorna "woman"

    """
    palindromo = validar_palindromo( str( id ) )
    if palindromo and id % 2 != 0:
        respuesta = "girl"
    elif palindromo and id % 2 == 0:
        respuesta = "boy"
    elif not palindromo and id % 2 == 0:
        respuesta = "man"
    elif not palindromo and id % 2 != 0:
        respuesta = "woman"
    
    return respuesta

# def palindromo( cadena: str ) -> bool:
    

def validar_palindromo ( cadena: str ) -> bool:
    """ Verificar si la cadena es un palíndromo
    
    Parámetros:
        cadena: Cadena de caracteres a evaluar

    Retorno:
        booleano: Si es un palíndromo retorna True
                  Si no es un palíndromo retorna False
    """
    inicio = 0
    fin = len( cadena ) - 1
    while cadena[inicio] == cadena[fin]:
        if inicio >= fin:
            return True
        inicio += 1
        fin -=1
    return False
