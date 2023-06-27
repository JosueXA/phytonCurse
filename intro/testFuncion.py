import math 

# def funcion_1()->str:
#     return "Hola mi amigo "

# def funcion_2( palabra: str ) -> str:
#     return funcion_1() + str(palabra)

# resultado = print( funcion_2( "Juan" ) )
# print( "El resultado de mi función es: "+ str(resultado) )

# calcular el IMC de una persona argumentos peso y altura retorna el resultado
# def calcular_imc( peso: float, altura: float ) -> float:
#     imc = peso / ((altura)**2)
#     return imc

# peso = float(input('Ingres su peso en kg: '))
# altura = float(input('Ingrese su altura en m: '))
# # indice = calcular_imc( peso, altura )
# print( "Su IMC es: ", round( calcular_imc( peso, altura ), 2 ) )

# # Calcula la velocidad de un objeto cuando toca el suelo a partir de la altura

# def vel_en_caida_libre( altura: float ) -> float:
#     vel_final = math.sqrt( 2 * 9.8 * altura )
#     return round( vel_final, 2 )

# res = vel_en_caida_libre( 20.5 )
# print( "La velocidad final es:", res )

# Calcula la edad de una persona a partir de su fecha de nacmiento y la fecha actual

def calcular_edad( dia_nacio: int, mes_nacio: int, anio_nacio: int, dia_actual: int, mes_actual: int, anio_actual: int ) -> str:
    anio = anio_actual - anio_nacio
    mes = mes_actual - mes_nacio
    dia = dia_actual - dia_nacio
    if mes < 0:
        anio = anio - 1
        mes = 12 + mes
    if dia < 0:
        mes = mes - 1
        dia = 30 + dia
    
    cadena = str(anio) + "," + str(mes) + "," + str(dia)
    return cadena

res = calcular_edad(20, 11, 1986, 16, 10 , 1987)
print( "Su edad es: ", res )