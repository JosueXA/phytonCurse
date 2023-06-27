"""
Una agencia de viajes necesita informar a sus clientes la hora de llegada de sus vuelos. Se conoce la hora de partida del vuelo 
(en horas, minutos y segundos) y la duración del vuelo (en horas, minutos y segundos).

Cree una función que retorne la hora de llegada del vuelo en una cadena con el formato “HH:mm:ss” donde HH es la hora, mm los 
minutos y ss los segundos de la hora de llegada del vuelo. 

La hora está dada en formato de 24 horas. Si alguno de los 3 números de la respuesta es menor a 10, sólo se necesita un dígito 
('7' en lugar de '07').


Su solución debe tener una función de acuerdo con la siguiente especificación:

Nombre de la función: calcular_horario_llegada

Si lo requiere, puede agregar funciones adicionales.
13, 45, 30 : 1, 30, 15
"""
def calcular_horario_llegada( hora_salida: int, minuto_salida: int, segundo_salida: int, duracion_horas: int, duracion_minutos: int, duracion_segundos: int) -> str:
    arribo_hora = hora_salida + duracion_horas
    arribo_minuto = minuto_salida + duracion_minutos
    arribo_segundo = segundo_salida + duracion_segundos
    if arribo_segundo >= 60:
        arribo_minuto += 1
        arribo_segundo %= 60
    if arribo_minuto >= 60:
        arribo_hora += 1
        arribo_minuto %= 60
    if arribo_hora >= 24:
        arribo_hora %= 24
    # Se crean los respectivas cadenas de texto de cada dígitos
    hora_str = str(arribo_hora)
    minuto_str = str(arribo_minuto)
    segundo_str = str(arribo_segundo)
    # Se agrega un 0 si solo es un dígito de la hora
    if len(hora_str) < 2:
      hora_str = "0" + hora_str
    if len(minuto_str) < 2:
      minuto_str = "0" + minuto_str
    if len(segundo_str) < 2:
      segundo_str = "0" + segundo_str

    cadena = hora_str + ":" + minuto_str + ":" + segundo_str
    return cadena

res = calcular_horario_llegada(22, 15, 30, 1, 30, 35)

print('La hora de arribo es:', res)
"""
def calcular_horario_llegada_condicion10( hora_salida: int, minuto_salida: int, segundo_salida: int, duracion_horas: int, duracion_minutos: int, duracion_segundos: int) -> str:
    arribo_hora = hora_salida + duracion_horas
    arribo_minuto = minuto_salida + duracion_minutos
    arribo_segundo = segundo_salida + duracion_segundos

    if arribo_segundo >= 60:
        arribo_minuto += 1
        arribo_segundo %= 60
        
    if arribo_minuto >= 60:
        arribo_hora += 1
        arribo_minuto %= 60
        
    if arribo_hora >= 24:
        arribo_hora %= 24
    
    if arribo_segundo < 10:
        arribo_segundo = 7

    if arribo_minuto < 10:
        arribo_minuto = 7

    if arribo_hora < 10:
        arribo_hora = 7
        
    cadena = str(arribo_hora) + ":" + str(arribo_minuto) + ":" + str(arribo_segundo)
    return cadena
"""
# def validarHoras( hora: int ) -> int:

