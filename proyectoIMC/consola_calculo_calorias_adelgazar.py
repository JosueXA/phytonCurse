import calculadora_indices as calc

def ejecutar_consumo_calorias_recomendado_para_adelgazar() -> None:
    peso = float( input('Ingrese el peso de la persona (en kilogramos): ') )
    altura = float( input('Ingrese la altura de la persona (en centímetros): ') )
    edad = int( input('Ingrese la edad de la persona (en años): ') )
    valor_genero = int( input('Ingrese el valor 5 en caso de ser hombre y -161 en caso de ser mujer: ') )
    calorias_adelgazar = calc.consumo_calorias_recomendado_para_adelgazar( peso, altura, edad, valor_genero )
    print( calorias_adelgazar )

def inicar_aplicacion() -> None:
    print('En está funcion se van a calcular la cantidad que una persona debe consumir a diario, en caso de que desee adelgazar')
    ejecutar_consumo_calorias_recomendado_para_adelgazar()

inicar_aplicacion()