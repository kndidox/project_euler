"""
    005-Menor multiplo

    2520 es el menor numero que puede ser divido por cada numero del 1 al 10 sin dejar ningun residuo.

    Cual es el menor numero positivo que puede ser dividido por cada numero del 1 al 20 sin dejar residuo?
"""

bandera = True
dividendo = 20 # 0 / 1890 
while bandera:
    bandera_divisores = True
    for divisor in range (1,21): # Valor limite no se ejecuta dentro del ciclo
        if dividendo % divisor != 0:
            bandera_divisores = False
            break

    if bandera_divisores:
        bandera = False
    else:
        dividendo += 20

print("El menor numero divisible del 1 al 20 es: ", dividendo)

