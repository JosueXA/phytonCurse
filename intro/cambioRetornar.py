"""
  Considere el software que se ejecuta en una máquina expendedora. Una de las tareas que debe realizar es determinar cuánto cambio
  debe entregarle al cliente luego de que paga. Escriba una función que recibe la cantidad de dinero (en pesos) a dar como cambio
  al cliente y retorne un mensaje con la cantidad de monedas de cada denominación que deben ser entregadas, teniendo en cuenta que
  el cambio se debe otorgar con la menor cantidad de monedas posible.

  La máquina cuenta con monedas de 500, 200, 100 y 50 pesos, y el cambio total se entregará con monedas de estas denominaciones.
  El mensaje retornado DEBE seguir el siguiente formato: “A,B,C,D” (sin espacios intermedios) donde A, B, C y D son la cantidad 
  de monedas de 500, 200, 100 y 50, respectivamente.


  Su solución debe tener una función de acuerdo con la siguiente especificación:

  Nombre de la función: calcular_cambio

  Si lo requiere, puede agregar funciones adicionales.

"""

def calcular_cambio( cambio: int ) -> str:

    # if cambio >= 500:
    #     a = cambio // 500
    #     cambio = cambio - a * 500
    # else:
    #     a = 0
    
        
    # if cambio >= 200:
    #     b = cambio // 200
    #     cambio = cambio - b * 200
    # else:
    #     b = 0


    # if cambio >= 100:
    #     c = cambio // 100
    #     cambio = cambio - c * 100
    # else:
    #     c = 0


    # if cambio >= 50:
    #     d = cambio // 50
    #     cambio = cambio - d * 50
    # else:
    #     d = 0
    [a, restante] = tipo_moneda( cambio, 500 )
    [b, restante] = tipo_moneda( restante, 200 )
    [c, restante] = tipo_moneda( restante, 100 )
    [d, restante] = tipo_moneda( restante, 50 )

    return str(a) + "," + str(b) + "," + str(c) + "," + str(d)

def tipo_moneda( cambio: int, moneda: int ) -> int:
    if cambio >= moneda:
        res = cambio // moneda
        cambio = cambio - res * moneda
    else:
        res = 0
    return res, cambio

res = calcular_cambio(450)

print(res)
