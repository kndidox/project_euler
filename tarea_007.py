"""
Escriba un programa para simular el tiro de dos dados. El programa debe utilizar rand para tirar el primer dado, y de
nuevo para tirar el segundo dado. Después debe calcularse la suma de los dos valores. [Nota: cada dado puede mostrar un valor
entero del 1 al 6, por lo que la suma de los valores variará del 2 al 12, siendo 7 la suma más frecuente, mientras que 2 y 12 serán
las sumas menos frecuentes]. Su programa debe tirar los dados 36,000 veces. Utilice un arreglo unidimensional para registrar el número de veces que aparezca cada una de las
posibles sumas. Imprima los resultados en formato tabular. Determine además si los totales son razonables (es decir, hay seis
formas de tirar un 7, por lo que aproximadamente una sexta parte de los tiros deben ser 7).

tips:
Debes importar la libreria random que te permite generar numeros pseudoaleatorios:

import random

print(random.randint(3, 9)) # Genera un numero aleatorio entre 3 y 9
"""