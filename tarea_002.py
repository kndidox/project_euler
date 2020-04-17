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
m = [
        [8,9,15],
        [-5,8,6],
        [-2,5,3]
    ]    
dp = 0
ds = 0
dif = 0

for f in range (len(m)):

   for c in range (len(m[f])):

        if f==c:
            dp = dp + m[f][c]

        if f + c == (len (m) - 1):
            ds = ds + m[f][c]

dif = ds - dp

print("La Sumatoria de la diagonal Principal es: ",dp)
print("La Sumatoria de la Diagonal Secundaria es: ",ds)  
print("La diferencia entre la DP y la DS es: ",dif) 
    
   