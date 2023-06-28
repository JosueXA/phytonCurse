import math

def area_triangulo(s1: float, s2: float, s3: float) -> float:
    s = subperimtetro(s1, s2, s3)
    a = (s * (s - s1) * (s - s2) * (s - s3))
    area = raizCuadrada(a)
    numRedondeado = round(area,1)
    return numRedondeado


def subperimtetro(s1: float, s2: float, s3: float) -> float:
    sub = (s1 + s2 + s3) / 2
    return sub

def raizCuadrada(num: float) -> float:
    raiz = math.sqrt(num)
    return raiz

s1 = float(input('Ingresa el primer lado del triangulo: '))
s2 = float(input('Ingresa el segundo lado del triangulo: '))
s3 = float(input('Ingresa el tercer lado del triangulo: '))

resultado = area_triangulo(s1, s2, s3)

print('El area del triangulo es '+ str(resultado) +', dados los lados del trinagulo '+ str(s1) +', '+ str(s2) +' y '+ str(s3)  )