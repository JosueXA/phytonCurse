import calculadora_indices as calc

def ejecutar_calcular_calorias_en_reposo() -> None:
    peso = float( input('Ingrese el peso de la persona (en kilogramos): ') )
    altura = float( input('Ingrese la altura de la persona (en centímetros): ') )
    edad = int( input('Ingrese la edad de la persona (en años): ') )
    valor_genero = int( input('Ingrese el valor 5 en caso de ser hombre y -161 en caso de ser mujer: ') )
    calorias = calc.calcular_calorias_en_reposo( peso, altura, edad, valor_genero )
    print('Tú perdida de calorias en reposo es de:', calorias ,'cal')

def inicar_aplicacion() -> None:
    print('En está funcion se van a calcular las calorias que se pierden en estado de reposo')
    ejecutar_calcular_calorias_en_reposo()

inicar_aplicacion()