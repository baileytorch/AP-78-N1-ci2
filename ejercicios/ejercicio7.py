import ejercicio6

try:
    numero_1 = float(input('Ingrese primer númereo: '))
    numero_2 = float(input('Ingrese segundo número: '))
    operacion = input('Ingrese operación a realizar (+, -, * o /): ')

    ejercicio6.calculadora_basica(numero_1, numero_2, operacion)
    result = ejercicio6.calculadora_v2(numero_1, numero_2, operacion)
    print(f'{result}')
except:
    print('Valores NO corresponden')


def procesar_funciones(a, b, c):
    ejercicio6.calculadora_basica(a, b, c)
    resultado = ejercicio6.calculadora_v2(a, b, c)
    return resultado
