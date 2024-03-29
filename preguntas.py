"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    x = open("data.csv", "r").readlines()
    x = [z.replace("\n", "") for z in x]
    x = [data.split("\t") for data in x]
    
    return sum([int(data[1]) for data in x])

def itemgetter(*items):
    if len(items) == 1:
        item = items[0]
        def g(obj):
            return obj[item]
    else:
        def g(obj):
            return tuple(obj[item] for item in items)
    return g

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    x = open("data.csv", "r").readlines()
    x = [z.replace("\n", "") for z in x]
    x = [data.split("\t") for data in x]
    x = [data[0] for data in x]
    x = [(letra,1) for letra in x]
    x = sorted(x,key=itemgetter(0))
    tuples = []
    previous_key = None
    acum = 0
    i = 0
    while(True):
        key, value = x[i]
        if previous_key is None:
            previous_key = key
        if key != previous_key:
            tuples.append((previous_key,acum))
            previous_key = key
            acum = value
        else:
            acum += value
        i += 1
        if i == len(x):
            tuples.append((previous_key,acum))
            break
    return(tuples)


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    x = open("data.csv", "r").readlines()
    x = [z.replace("\n", "") for z in x]
    x = [data.split("\t") for data in x]
    x = [(data[0],int(data[1])) for data in x]
    x = sorted(x,key=itemgetter(0))
    tuples = []
    previous_key = None
    a = 0
    i = 0
    while(True):
        key, value = x[i]
        if previous_key is None:
            previous_key = key
        if key != previous_key:
            tuples.append((previous_key, a))
            previous_key = key
            a = value
        else:
            a += value
        i += 1
        if i == len(x):
            tuples.append((previous_key, a))
            break
    return tuples



def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    x = open("data.csv", "r").readlines()
    x = [z.replace("\n", "") for z in x]
    x = [data.split("\t") for data in x]
    x = [data[2] for data in x]
    x = [data.split("-") for data in x]
    x = [(data[1],1) for data in x]
    x = sorted(x,key=itemgetter(0))
    tuples = []
    previous_key = None
    a = 0
    i = 0
    while(True):
        key, value = x[i]
        if previous_key is None:
            previous_key = key
        if key != previous_key:
            tuples.append((previous_key, a))
            previous_key = key
            a = value
        else:
            a += value
        i += 1
        if i == len(x):
            tuples.append((previous_key, a))
            break
    return tuples



def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    x = open("data.csv", "r").readlines()
    x = [z.replace("\n", "") for z in x]
    x = [data.split("\t") for data in x]
    x = [(data[0],int(data[1])) for data in x]
    x = sorted(x,key=itemgetter(0))
    tuples = []
    previous_key = None
    i = 0
    nums = []
    while(True):
        key, value = x[i]
        if previous_key is None:
            previous_key = key
        if key != previous_key:
            minimo = min(nums)
            maximo = max(nums)
            tuples.append((previous_key, maximo, minimo))
            previous_key = key
            nums = []
            nums.append(value)
        else:
            nums.append(value)
        i += 1
        if i == len(x):
            minimo = min(nums)
            maximo = max(nums)
            tuples.append((previous_key, maximo, minimo))
            break
    return tuples


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    x = open("data.csv", "r").readlines()
    x = [z.replace("\n", "") for z in x]
    x = [data.split("\t") for data in x]
    x = [data[4].split(",") for data in x]
    valores = []
    for diccionario in x:
        [valores.append(valor) for valor in diccionario]
    x = [(valor.split(":")[0],int(valor.split(":")[1])) for valor in valores]
    x = sorted(x,key=itemgetter(0))
    tuples = []
    previous_key = None
    i = 0
    nums = []
    while(True):
        key, value = x[i]
        if previous_key is None:
            previous_key = key
        if key != previous_key:
            minimo = min(nums)
            maximo = max(nums)
            tuples.append((previous_key, minimo, maximo))
            previous_key = key
            nums = []
            nums.append(value)
        else:
            nums.append(value)
        i += 1
        if i == len(x):
            minimo = min(nums)
            maximo = max(nums)
            tuples.append((previous_key, minimo, maximo))
            break
    return tuples



def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    x = open("data.csv", "r").readlines()
    x = [z.replace("\n", "") for z in x]
    x = [data.split("\t") for data in x]
    x = [(int(data[1]),data[0]) for data in x]
    x = sorted(x,key=itemgetter(0))
    tuples = []
    previous_key = None
    i = 0
    letras = []
    while(True):
        key, value = x[i]
        if previous_key is None:
            previous_key = key
        if key != previous_key:
            tuples.append((previous_key, letras))
            previous_key = key
            letras = []
            letras.append(value)
        else:
            letras.append(value)
        i += 1
        if i == len(x):
            tuples.append((previous_key, letras))
            break
    return tuples


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    x = open("data.csv", "r").readlines()
    x = [z.replace("\n", "") for z in x]
    x = [data.split("\t") for data in x]
    x = [(int(data[1]),data[0]) for data in x]
    x = sorted(x,key=itemgetter(0))
    tuples = []
    previous_key = None
    i = 0
    letras = []
    while(True):
        key, value = x[i]
        if previous_key is None:
            previous_key = key
        if key != previous_key:
            tuples.append((previous_key,sorted(set(letras))))
            previous_key = key
            letras = []
            letras.append(value)
        else:
            letras.append(value)
        i += 1
        if i == len(x):
            tuples.append((previous_key,sorted(set(letras))))
            break
    return tuples




def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    x = open("data.csv", "r").readlines()
    x = [z.replace("\n", "") for z in x]
    x = [data.split("\t") for data in x]
    x = [data[4].split(",") for data in x]
    valores = []
    for diccionario in x:
        [valores.append(valor) for valor in diccionario]
    x = [(valor.split(":")[0],1) for valor in valores]
    x = sorted(x,key=itemgetter(0))
    valores = {}
    previous_key = None
    a = 0
    i = 0
    while(True):
        key, value = x[i]
        if previous_key is None:
            previous_key = key
        if key != previous_key:
            valores[previous_key] = a
            previous_key = key
            a = value
        else:
            a += value
        i += 1
        if i == len(x):
            valores[previous_key] = a
            break
    return valores


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    x = open("data.csv", "r").readlines()
    x = [z.replace("\n", "") for z in x]
    x = [data.split("\t") for data in x]
    return [(data[0],len(data[3].split(",")),len(data[4].split(","))) for data in x]



def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    x = open("data.csv", "r").readlines()
    x = [z.replace("\n", "") for z in x]
    x = [data.split("\t") for data in x]
    x = [(data[3].split(","),int(data[1])) for data in x]
    valores = []
    for letras,valor in x:
        [valores.append((str(letra),valor)) for letra in letras]
    x = sorted(valores,key=itemgetter(0))
    valores = {}
    previous_key = None
    a = 0
    i = 0
    while(True):
        key, value = x[i]
        if previous_key is None:
            previous_key = key
        if key != previous_key:
            valores[previous_key] = a
            previous_key = key
            a = value
        else:
            a += value
        i += 1
        if i == len(x):
            valores[previous_key] = a
            break
    return valores


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    x = open("data.csv", "r").readlines()
    x = [z.replace("\n", "") for z in x]
    x = [data.split("\t") for data in x]
    valores = [data[4].split(",") for data in x]
    valores2 = []
    for diccionario in valores:
        valores2.append([int(valor.split(":")[1]) for valor in diccionario])
    valores2 = [sum(valores) for valores in valores2]
    x = [(data[0],valores) for data,valores in zip(x,valores2)]
    x = sorted(x,key=itemgetter(0))
    valores = {}
    previous_key = None
    a = 0
    i = 0
    while(True):
        key, value = x[i]
        if previous_key is None:
            previous_key = key
        if key != previous_key:
            valores[previous_key] = a
            previous_key = key
            a = value
        else:
            a += value
        i += 1
        if i == len(x):
            valores[previous_key] = a
            break
    return valores
