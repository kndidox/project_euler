"""
    Dada una lista de valores:
    n = [2.3,15,20,30,50,80]
    Calcule el valor de:
    -La suma de todos los valores
    -El producto de todos los valores
"""

n = [2.3,15,20,30,50,80]

suma = 0
multi = 1

for i in n:
    print(i)
    suma += i
    multi *= i
    
print(suma)
print(multi)




