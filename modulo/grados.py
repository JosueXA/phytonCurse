def convierteGradosFahrenheit(grados:float) -> float:
    gradosF = 1.8 * grados + 32
    return gradosF

registroGrados = input('Ingrese los grados Celsius: ')
gradosC = float(registroGrados)

resultadoF = convierteGradosFahrenheit(gradosC)

print('Los ', gradosC ,' grados Celsius son ', resultadoF ,' grados Fahrenheit' )
