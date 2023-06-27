# Definición de funciones para el modulo
def calcular_IMC( peso: float, altura: float ) -> float:
    """ Calcula el índice corporal de una persona
    Parámetros:
        peso: Peso de la persona en Kilogramos
        altura: Altura de la persona en metros
    Retrono:
        imc: Índice de masa corporal de la persona
    """
    imc = peso / ( altura ** 2 )
    return round( imc, 2 )

def calcular_porcentaje_grasa( peso: float, altura: float, edad: int, valor_genero: float ) -> float:
    """ Calcula el porcentaje de grasa de una persona
    Parámetros
        peso: Peso de la persona en kilogramos
        altura: Altura de la persona en metros
        edad: Edad de la persona en años
        valor_genero: Valor que varía según el género de la persona: en caso de ser masculino debe
                      ser 10.8 y en caso de ser femenino debe ser 0.
    Retorno
        porcentaje_grasa: El porcentaje de grasa que tiene el cuerpo de una persona
    """
    imc = calcular_IMC( peso, altura )
    porcentaje_grasa = 1.2 * imc + 0.23 * edad - 5.4 - valor_genero
    return round( porcentaje_grasa, 2 )

def calcular_calorias_en_reposo( peso: float, altura: float, edad: int, valor_genero: int ) -> float:
    """ Calcula la cantidad de calorías que una persona quema estando en reposo (esto es su tasa
        metabólica basal)
    Parámetros
        peso: Peso de la persona en kilogramos
        altura: Altura de la persona en centímetros
        edad: Edad de la persona en años
        valor_genero: Valor que varía según el género de la persona: en caso de ser masculino debe
                      ser 5 y en caso de ser femenino debe ser -161
    Retorno
        calorias_reposo: La cantidad de calorías que la persona quema en reposo
    """
    calorias_reposo = ( 10 * peso ) + ( 6.25 * altura ) - ( 5 * edad ) + valor_genero
    return round( calorias_reposo, 2 )

def calcular_calorias_en_actividad(peso: float, altura: float, edad: int, valor_genero: int, valor_actividad: float ) -> float:
    """ Calcula la cantidad de calorías que una persona quema al realizar algún tipo de actividad 
        física (esto es, su tasa metabólica basal según actividad física),
    Parámetros
        peso: Peso de la persona en kilogramos
        altura: Altura de la persona en centímetros
        edad: Edad de la persona en años
        valor_genero: Valor que varía según el género de la persona: en caso de ser masculino debe
                      ser 5 y en caso de ser femenino debe ser -161
        valor_actividad: Valor que depende de la actividad física semanal:
                          1.2: poco o ningún ejercicio
                          1.375: ejercicio ligero (1-3 días a la semana)
                          1.55: ejercicio moderado (3-5 días a la semana)
                          1.725: deportista (6-7 días a la semana)
                          1.9: atleta (entrenamientos mañana y tarde)
    Retorno
        calorias_actividad: La cantidad de calorías que la persona quema, al realizar algún tipo de
                            actividad física semanalmente
    """
    calorias_reposo = calcular_calorias_en_reposo( peso, altura, edad, valor_genero )
    calorias_actividad = calorias_reposo * valor_actividad
    return round( calorias_actividad, 2 )

def consumo_calorias_recomendado_para_adelgazar( peso: float, altura: float, edad: int, valor_genero: int ) -> str:
    """ Calcula el rango de calorías recomendado, que debe consumir una persona diariamente en caso 
        de que desee adelgazar
    Parámetros
        peso: Peso de la persona en kilogramos
        altura: Altura de la persona en centímetros
        edad: Edad de la persona en años
        valor_genero: Valor que varía según el género de la persona: en caso de ser masculino debe
                      ser 5 y en caso de ser femenino debe ser -161
    Retorno
        calorias_para_adelgazar: Una cadena indicando el rango de calorias que una perosna debe
                                  consumir si desea adelgazar
    """
    calorias_reposo = calcular_calorias_en_reposo( peso, altura, edad, valor_genero )
    minimo_calorias = round( calorias_reposo - ( calorias_reposo * 0.20 ), 2 )
    maximo_calorias = round( calorias_reposo - ( calorias_reposo * 0.15 ), 2 )
    cadena = "Para adelgazar es recomendado que consumas entre: " + str(minimo_calorias) + " y " + str(maximo_calorias) + " calorías al día."
    return cadena

print( consumo_calorias_recomendado_para_adelgazar( 58, 169, 21, -161 ) )

