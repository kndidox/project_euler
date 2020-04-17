"""
(Sistema de reservaciones de una aerolínea) Una pequeña aerolínea acaba de comprar una computadora para su nuevo
sistema de reservaciones automatizado. Se le ha pedido a usted que desarrolle el nuevo sistema. Usted va a escribir una aplica-
ción para asignar asientos en cada vuelo del único avión de la aerolínea (capacidad: 10 asientos).
Su programa debe mostrar el siguiente menú de alternativas: Por favor escriba 1 para "Primera Clase" y Por favor
escriba 2 para "Económico" . Si la persona escribe 1, su programa debe asignarle un asiento en la sección de primera clase
(asientos 1 a 5). Si la persona escribe 2 , su programa debe asignarle un asiento en la sección económica (asientos 6 a 10). Su
programa deberá entonces imprimir un pase de abordaje, indicando el número de asiento de la persona y si se encuentra en la
sección de primera clase o económica del avión.
Use una lista unidimensional para representar la tabla de asientos del avión. Inicialice todos los elementos de la lista con
0 para indicar que todos los asientos están vacíos. A medida que se asigne cada asiento, establezca los elementos correspondien-
tes de la lista en 1 para indicar que ese asiento ya no está disponible.
Desde luego que su programa nunca deberá asignar un asiento que ya haya sido asignado. Cuando esté llena la sección de
primera clase, su programa deberá preguntar a la persona si acepta ser colocada en la sección económica (y viceversa). Si la per-
sona acepta, haga la asignación de asiento apropiada. Si no acepta, imprima el mensaje "El próximo vuelo sale en 3 horas" .
"""