# Escriba un programa que pida dos números y 
# que conteste cuál es el menor y cuál el mayor o que escriba que son iguales.

def comparar_numeros(num1,num2):
    if num1 > num2:
        print(f'{num1} > {num2}')
    elif num2 > num1:
        print(f'{num2} > {num1}')
    else:
        print('Sus números son iguales')

try:
    num1 = float(input('Ingrese primer número: '))
    num2 = float(input('Ingrese segundo número: '))
    comparar_numeros(num1,num2)
except:
    print('Valor ingresado NO corresponde')