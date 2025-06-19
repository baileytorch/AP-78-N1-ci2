diccionario_1 = {
    1:'Nombre',
    2:'Apellido',
    3:49
}

diccionario_3 = {
    'Nombre':'Erick',
    'Apellido':'Bailey',
    'Edad':49
}

# print(dir(diccionario))

# 'copy': Copia la colección en otra variable
print()
diccionario_2 = diccionario_1.copy()
print(f'Copiando diccionarios mediante método COPY, imprimimos diccionario_2: {diccionario_2}')

# 'clear': Elimina todos los elementos de la colección
print()
diccionario_2.clear()
print(f'Imrimiendo diccionario_2 después de usar método CLEAR(): {diccionario_2}')

# 'fromkeys': Crea un nuevo diccionario recibiendo una colección para claves y una colección para valores
print()
x = ['clave 1','clave 2','clave 3']
y = 'valor'
nuevo_diccionario = dict.fromkeys(x, y)
print(f'Creando un nuevo diccionario con método FROMKEYS(): {nuevo_diccionario}')

# 'get': Retorna el valor de una clave específica
print()
print(f'Imprimiendo el valor del elemento 3: {diccionario_1.get(3)}')

# 'keys': Devuelve una lista con las claves del diccionario
print()
print(f'Claves de diccionario_1: {diccionario_1.keys()}')

# 'values': Devuelve una lista con los valores del diccionario
print()
print(f'Valores de diccionario_1: {diccionario_1.values()}')

# 'pop': Elimina un elemento especificando la clave
print()
diccionario_1.pop(3)
print(f'Imprimiendo el diccionario al eliminar el elemento de clave 3: {diccionario_1}')

print()
diccionario_3.pop('Edad')
print(f'Imprimiendo el diccionario al eliminar el elemento de clave Edad: {diccionario_3}')


# 'popitem': Elimina el último elemento incluyendo su clave y su valor
print()
diccionario_3.popitem()
print(f'Eliminar el último elemento mediante el método POPITEM(): {diccionario_3}')

# 'update': Actualiza un elemento indicando su clave
print()
diccionario_1.update({3:40})
print(f'Modificando el elemento de clave 3 con el método UPDATE(): {diccionario_1}')

diccionario_1.update({4:'Hombre'})
print(f'Agregar un elemento de clave 4 con el método UPDATE(): {diccionario_1}')

# 'items': Permite recorrer cada uno de los elementos de la colección