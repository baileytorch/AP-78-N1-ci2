# Escribir un programa que pida al usuario dos números y muestre por pantalla su suma, su resta, 
# su multiplicación y su división. 
# Si el divisor es cero el programa debe mostrar un error.

import math

print('Ejercicio 1')
numero_1 = float(input('Ingrese primer número: '))
numero_2 = float(input('Ingrese segundo número: '))

print(f'Suma: {numero_1} + {numero_2} = {numero_1 + numero_2}')
print(f'Resta: {numero_1} - {numero_2} = {numero_1 - numero_2}')
print(f'Multiplicación: {numero_1} x {numero_2} = {numero_1 * numero_2}')

if numero_2 != 0:
    print(f'División: {numero_1} / {numero_2} = {numero_1 / numero_2}')
else:
    print('No se puede dividir por 0!!!')