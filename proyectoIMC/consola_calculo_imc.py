import calculadora_indices as calc

def ejecutar_calcular_IMC() -> None:
    peso = float( input('Ingrese el peso de la persona (en kilogramos): ') )
    altura = float( input('Ingrese la altura de la persona (en metros): ') )
    imc = calc.calcular_IMC( peso, altura )
    print('Tú índice de masa corporal es de:', imc)

def inicar_aplicacion() -> None:
    print('En está funcion se va a calcular el índice de masa corporal de una persona')
    ejecutar_calcular_IMC()

inicar_aplicacion()