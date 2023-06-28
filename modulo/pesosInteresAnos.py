capital = float(input('Ingresa el capital inicial: '))
tasa = float(input('Ingresa la tasa anual: '))
tiempo = int(input('Ingresa el número de años: '))

valorFuturo = capital * (1+(tasa/100)) ** tiempo

valorRedondeado = round(valorFuturo, 2)

print('El valor futuro del monto inicial es de $ '+ str(valorRedondeado) +', transcurridos '+ str(tiempo) +' años y una tasa del '+ str(tasa) +'% anual')