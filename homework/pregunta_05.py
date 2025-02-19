"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    min_max_values = []
    with open('files/input/data.csv', 'r') as file:
        data = {}
        for line in file:
            columns = line.strip().split('\t')
            letter = columns[0]
            value = int(columns[1])
            if letter in data:
                data[letter].append(value)
            else:
                data[letter] = [value]
    
    for letter, values in data.items():
        min_value = min(values)
        max_value = max(values)
        min_max_values.append((letter, max_value, min_value))
    
    min_max_values.sort(key=lambda x: x[0])
    
    return min_max_values
