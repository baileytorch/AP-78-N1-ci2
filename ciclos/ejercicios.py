# Solicitar un número al usuario para imprimir una tabla de multiplicar desde 1 hasta 10 de ese número

numero_str = input('Ingrese un número para crear su tabla de multiplicar: ')
numero_int = int(numero_str)

# Resolvemos con un ciclo FOR
print(f'Tabla del {numero_str} mediante ciclo FOR')
for i in range(1,11):
    print(f'{numero_int} * {i} = {numero_int * i}')

# Resolvemos con un ciclo WHILE
print(f'Tabla del {numero_str} mediante ciclo WHILE')