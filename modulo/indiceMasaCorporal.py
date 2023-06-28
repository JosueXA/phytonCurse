def calcular_BMI(peso_lb: float, altura_inch: float) -> float:
    pesoKilogramos = peso_lb * 0.45
    alturaMetros = altura_inch * 0.025
    imc = pesoKilogramos / (alturaMetros ** 2)
    return round(imc, 2)