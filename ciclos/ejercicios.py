# Solicitar un número al usuario para imprimir una tabla de multiplicar desde 1 hasta 10 de ese número

numero_str = input('Ingrese un número para crear su tabla de multiplicar: ')
numero_int = int(numero_str)

# Resolvemos con un ciclo FOR
print(f'Tabla del {numero_str} mediante ciclo FOR')
for i in range(1,11):
    print(f'{numero_int} x {i} = {numero_int * i}')

# Resolvemos con un ciclo WHILE
print(f'Tabla del {numero_str} mediante ciclo WHILE')
numero = 1
while numero <= 10:
    print(f'{numero_int} x {numero} = {numero_int * numero}')
    numero += 1

# Escriba un programa que muestre las tablas de multiplicar del 1 al 10
# Ciclo 1 recorro los elementos desde 1 a 10
# Ciclo 2, interno del ciclo 1, recorro otra colección de elementos del 1 al 10
# Dentro del ciclo 2 hago la multiplicación de los números

print()
print('Las Tablas de Multiplicar con ciclo FOR')

for numero in range(1,11):
    print()
    print(f'Tabla del {numero}')
    print('==============')
    for num in range(1,11):
        print(f'{numero} x {num} = {numero * num}')

print()
print('Las Tablas de Multiplicar con ciclo WHILE')

numero = 1
while numero <= 10:
    print()
    print(f'Tabla del {numero}')
    print('==============')
    num = 1
    while num <= 10:
        print(f'{numero} x {num} = {numero * num}')
        num += 1
    numero += 1