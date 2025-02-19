"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    min_max_values = []
    with open('files/input/data.csv', 'r') as file:
        data = {}
        for line in file:
            columns = line.strip().split('\t')
            values = columns[4].split(',')
            for value in values:
                key, val = value.split(':')
                if key in data:
                    data[key].append(int(val))
                else:
                    data[key] = [int(val)]
    
    for key, values in data.items():
        min_value = min(values)
        max_value = max(values)
        min_max_values.append((key, min_value, max_value))
    
    min_max_values.sort(key=lambda x: x[0]) 
    
    return min_max_values