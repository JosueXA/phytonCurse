# Ejemplo diccionarios
directorio = {"Alicia": "321 456 29 73", "Bastien": "300 248 37 00", "Armando": "316 754 89 38"}
print( directorio )
print( directorio["Bastien"] )

# Adicion de datos a un diccionario
adicion_directorio = { **directorio } # Operador spread en python (**)
adicion_directorio["Juan"] = "311 286 25 27"
adicion_directorio["Luis"] = "316 423 38 12"
adicion_directorio["Maria"] = "315 476 39 02"
print( adicion_directorio )

# Las llaves o key pueden ser de cualquier valor 
agenda_día = {}
agenda_día[6] = "Empieza el día"
agenda_día[8] = "Desayuno con Clara"
agenda_día[9.5] = "Clase de IP"
agenda_día[11] = "Clase de cálculo"
agenda_día[13] = "Almuerzo"
agenda_día[15] = "Natación"
agenda_día[16] = "Repaso de química"
agenda_día[19.5] = "Visita a los abuelos"
print( agenda_día )

cuentas_mercado = {}
cuentas_mercado["Leche"] = 2500
cuentas_mercado["Pan"] = 1500
cuentas_mercado["Huevos"] = 6000
cuentas_mercado["Naranjas"] = 11500
cuentas_mercado["Queso"] = 7300
print( cuentas_mercado )

# Modificación de un dato en el diccionario por medio de la llave
modificacion_directorio = { **adicion_directorio }
modificacion_directorio["Luis"] = "Perdió su teléfono"
print( modificacion_directorio )

# Operadores in y not in
print( "Juan" in modificacion_directorio )
print( "Constanza" in modificacion_directorio )
print( "Pan" in cuentas_mercado )
print( "Jamón" in cuentas_mercado )
print( 6 in agenda_día )
print( 7.5 in agenda_día )

# Ejemplo de get() para diccionarios
inventario = {'manzanas': 430, 'naranjas': 525, 'peras': 217}
print( inventario )
print(inventario.get( 'manzanas', 'esa fruta no existe en el inventario' ))
print(inventario.get( 'arándanos', 'esa fruta no existe en el inventario' ))

# Operador len() también sirve para contar el tamaño de un diccionario
print( len(agenda_día) )
print( len(cuentas_mercado) )

# Método copy()
opuestos = {"arriba": "abajo", "derecha": "torcida", "si": "no", "claro": "obscuro"}
alias = opuestos
print( alias )
copia = opuestos.copy()
print( copia )

alias["derecha"] = "izquierda"
print( opuestos )
print( alias )
print( copia )

copia["claro"] = "espeso"
print( opuestos )
print( alias )
print( copia )

nuevo_inventario = { "bananos": 312, **inventario }
print( nuevo_inventario )
del nuevo_inventario["bananos"]
print( nuevo_inventario )
