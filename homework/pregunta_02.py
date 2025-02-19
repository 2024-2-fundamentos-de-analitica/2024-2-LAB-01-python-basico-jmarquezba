"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    counts = {}
    with open('files/input/data.csv', 'r') as file:
        for line in file:
            columns = line.strip().split('\t')
            letter = columns[0]
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1
    
    rpta = sorted([(letter, count) for letter, count in counts.items()])

    return rpta
