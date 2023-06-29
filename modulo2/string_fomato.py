n1 = "Simon José Antonio"
n2 = "de la Sanstísima Trinidad"
n3 = "Bolívar y Palacios"

print("Pi con tres decimales es {0:.3f}".format(3.1415926))
print("123456789 123456789 123456789 123456789 123456789 123456789")
print("|||{0:<25}|||{1:^25}|||{2:>25}|||nació en {3}".format(n1,n2,n3,1783))

carta="""
Querido {0} {2}.
{0}, Tengo una propuesta financiera muy interesante para hacerle!
Si usted deposita $10 millones de dólares en mi cuenta bancaria, puedo
duplicar su dinero ...
"""

print(carta.format("Julio", "Mario", "Santodomingo"))
print(carta.format("Luis Carlos", "Sarmiento", "Angulo"))