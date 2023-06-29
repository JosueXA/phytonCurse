def conteo_de_materias ( nombre_materia_1: str, nombre_materia_2: str, nombre_materia_3: str ) -> int:
    materia_1 = "programacion"
    materia_2 = "matematica"
    materia_3 = "filosofia"
    materia_4 = "literatura"
    materias_favoritas = 0

    if (nombre_materia_1.find(materia_1) != -1) or (nombre_materia_1.find(materia_2) != -1) or (nombre_materia_1.find(materia_3) != -1) or (nombre_materia_1.find(materia_4) != -1):
        materias_favoritas += 1
    if (nombre_materia_2.find(materia_1) != -1) or (nombre_materia_2.find(materia_2) != -1) or (nombre_materia_2.find(materia_3) != -1) or (nombre_materia_2.find(materia_4) != -1):
        materias_favoritas += 1
    if (nombre_materia_3.find(materia_1) != -1) or (nombre_materia_3.find(materia_2) != -1) or (nombre_materia_3.find(materia_3) != -1) or (nombre_materia_3.find(materia_4) != -1):
        materias_favoritas += 1

    return materias_favoritas

# Optimizar código ... 