"""
Entradas
    Compañía --> str --> "ALAS" o "VOLAR"
    Edad --> int 
    Si es temporada alta --> True de lo contrario False --> bool
    Se es estudiante --> True de lo contrario False --> bool

Salidas
    Precio del pasaje --> entero

Consideraciones y restricciones
    "ALAS" incrementa 30% en temporada alta
    "VOLAR" incrementa 20% en temporada alta
    50% de descuento para menores de edad
    "VOLAR" tiene recargo de $100000 para mayores de 60 años
    "ALAS" tiene descuento de 10% para estudiantes mayores de edad, en temporada baja
    Tarifa básica de 5 millones

"""

def calcular_precio_pasaje ( temporada_alta: bool, compania: str, edad: int, estudiante: bool ) -> int:
    
    precio = 5000000
    variaciones = 0
    seguro = False

    if compania == "ALAS":
        if temporada_alta:
            variaciones += 0.3
        else:
            if edad >= 18 and estudiante:
                variaciones -= 0.1
    elif compania == "VOLAR":
        if temporada_alta:
            variaciones += 0.2
        if edad > 60:
            seguro = True

    if edad < 18:
        variaciones -= 0.5
    
    precio *= (1 + variaciones)

    if seguro:
        precio += 100000

    return round(precio)

# Programa principal
temp = bool(int(input('¿Es temporada alta? Ingrese 1 para SI o 0 para NO: ')))
compania = input('Ingrese la compañía por la que viajará: ')
edad = int(input('Ingrese la edad de la persona: '))
est = bool(int(input('¿Es estudiante? Ingrese 1 para SI o 0 para NO: ')))

tarifa = calcular_precio_pasaje(temp, compania, edad, est)

print('La tarifa del pasaje es de $'+ str(tarifa) + ' COP')