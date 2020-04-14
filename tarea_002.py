"""
    data una matriz:
    m = [
        [8,9,15],
        [-5,8,6],
        [-2,5,3]
    ]

    Calcule la diferencia entre la suma de la diagonal principal y la diagonal secundaria.
    diagonal ppal = esq superior izq a esq inferior der
    diagonal sec = esq superior der a esq inferior izq

    tips: el metodo len(lista) devuelve el tamano de una lista
    ej: len(m) = 3

    tip2: 
        - cx == cy --> valor diag principal
        - cx + cy == len(lista) - 1 --> valor diag secundaria

    tip3: dos ciclos, uno para las filas y otro para las columnas. comparas las coordenas y haces tus calculos.

"""