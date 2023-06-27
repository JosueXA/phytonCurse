import calculadora_indices as calc

def ejecutar_calcular_porcentaje_grasa() -> None:
    peso = float( input('Ingrese el peso de la persona (en kilogramos): ') )
    altura = float( input('Ingrese la altura de la persona (en metros): ') )
    edad = int( input('Ingrese la edad de la persona (en años): ') )
    valor_genero = float( input('Ingrese el valor 10.8 en caso de ser hombre y 0 en caso de ser mujer: ') )
    porcentaje_grasa = calc.calcular_porcentaje_grasa( peso, altura, edad, valor_genero )
    print('Tú porcentaje de grasa es de: '+ str(porcentaje_grasa) +'%')

def inicar_aplicacion() -> None:
    print('En está funcion se va a calcular el procentaje de grasa de una persona')
    ejecutar_calcular_porcentaje_grasa()

inicar_aplicacion()