# función que calcula el perímetro de un triángulo rectángulo recibe dos argumentos de tipo float
def perimetro_triangulo(cateto1: float, cateto2: float)->float:
    hipotenusa = calcular_hip(cateto1, cateto2)    
    return cateto1 + cateto2 + hipotenusa


def calcular_hip(cateto1: float, cateto2: float)->float:
    suma_cuadrados = (cateto1 ** 2) + (cateto2 ** 2)
    hipotenusa = pow(suma_cuadrados, 0.5)
    return hipotenusa


cadena_cat_1 = input("Indique la longitud del primer cateto: ")
cadena_cat_2 = input("Indique la longitud del segundo cateto: ")
cat_1 = float(cadena_cat_1)
cat_2 = float(cadena_cat_2)

perimetro = perimetro_triangulo(cat_1, cat_2)

print("El perímetro de un triángulo rectángulo que tenga catetos de longitud",
      cat_1, "y", cat_2, "es", perimetro)


# Si cadena_cat_1 no es un int o float realiza una condición para evaluar el tipo de dato




# ¿Cuál es el objetivo del programa?
# Calcular el perímtero de un triangulo rectangulo 

# ¿Qué información tendrá que suministrar el usuario que ejecute el programa?
# El valor de los catetos del triangulo rectangulo

# ¿Cuál es el objetivo de cada bloque?
# El bloque de la función calcular_hip es calcular la hipotenusa del triangulo rectangulo
# El bloque de la función perimetro_triangulo es calcular el perimetro del triangulo rectangulo

# ¿Qué es lo que primero se ejecuta?
# El bloque de la función perimetro_triangulo

# ¿Cuál es la diferencia entre lo que está escrito en español y lo que está escrito en inglés?
# 
