def mision_rescate ( carga_sable: int, energia_escudo: int ) -> None:
    if not ( (carga_sable >= 90) and (energia_escudo >= 100) ):
        print("Tu ataque no tiene efecto, el dragón te va a freir hasta quedar crujiente!")
    else:
        print("Has logrado arrugar al dragón. ¡Puedes rescatar a la hermosa princesa!")


# usando la ley de morgan not (x and y) == (not x) or (not y) y los opuestos lógicos
def mision_rescate_2 ( carga_sable: int, energia_escudo: int ) -> None:
    if (carga_sable < 90) or (energia_escudo < 100):
        print("Tu ataque no tiene efecto, el dragón te va a freir hasta quedar crujiente!")
    else:
        print("Has logrado arrugar al dragón. ¡Puedes rescatar a la hermosa princesa!")


# También se puede usar el orden del if y del else, si nos es más fácil de expresar o entender
def mision_rescate_3 ( carga_sable: int, energia_escudo: int ) -> None:
    if (carga_sable >= 90) and (energia_escudo >= 100):
        print("Has logrado arrugar al dragón. ¡Puedes rescatar a la hermosa princesa!")
    else:
        print("Tu ataque no tiene efecto, el dragón te va a freir hasta quedar crujiente!")