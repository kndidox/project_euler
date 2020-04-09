""" #Resuelto
    001 - Multiplos de 3 y 5

    Si listamos todos los numeros naturales menores a 10 que son multiplos de 3 o 5, obtenemos que son 3,5,6 y 9.
    La suma de todos esos multiplos es 23.

    Encuentre la suma de todos los multiplos de 3 o 5 menores a 1000
"""

acum = 0
for i in range(0,1000):
    if i % 3 == 0:
        print(i, " Es divisible entre 3")
        acum = acum + i
    elif i % 5 == 0:
        acum = acum + i
        print(i, " Es divisible entre 5")

print("La suma de los multiplos de 3 o 5 menores a 1000 es: ",acum)