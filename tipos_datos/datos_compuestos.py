# Datos de tipo COMPUESTO o COMPLEJO
# Son colecciones de datos de tipo simple o compuesto

# LISTAS
# Una lista es una colección ORDENADA y MUTABLE de elementos de cualquier tipo de datos,
# los elementos se separan por comas.

lista_1 = ['cadenas de texto',49,True,34.89,[1,2,3,4,5]]
print(type(lista_1))
print(len(lista_1))
print(lista_1)
print(lista_1[0])

lista_1[1] = 'Aquiles Baeza'
print(lista_1)

# Agregar elementos a una lista
lista_1.append(False)
print(lista_1)

# Quitar elementos de una lista
# Quitamos el último elemento
lista_1.pop()
print(lista_1)

# Quitamos un elemento por su índice
lista_1.pop(4)
print(lista_1)

lista_1.insert(2,'test')
lista_1.insert(0,56)
print(lista_1)

# Vaciamos completamente la lista
lista_1.clear()
print(lista_1)
print('¿Dónde está la lista?')

# DICCIONARIOS
# Un diccionario es una colección ORDENADA y MUTABLE de PARES elementos de cualquier tipo de datos,
# los elementos se separan por comas.

diccionario_1 = {
    'nombre':'Erick',
    'apellido':'Bailey',
    'Profesor':True,
    'Edad':49,
    'Género':'Masculino'
}
print(type(diccionario_1))
print(len(diccionario_1))
print(diccionario_1)

# Accediendo a los datos mediante la CLAVE
print(diccionario_1['nombre'])
print(diccionario_1['apellido'])

# Elimando el último elemento
diccionario_1.popitem()

# Eliminar un elemento mediante su CLAVE
diccionario_1.pop('Edad')
print(diccionario_1)

# Agregar elementos añadiendo una CLAVE y un VALOR
diccionario_1['ciudad'] = 'Temuco'
diccionario_1['Edad'] = 35
print(diccionario_1)

print(diccionario_1.items())
print(diccionario_1.keys())
print(diccionario_1.values())

# Vaciar un diccionario
diccionario_1.clear()
print(diccionario_1)

# CONJUNTOS
# Un conjunto es una colección DESORDENADA y MUTABLE de elementos de cualquier tipo de datos,
# los elementos se separan por comas.
conjunto_1 = {'Erick Bailey',49,True}
conjunto_2 = {False,56.1}
print(type(conjunto_1))
print(len(conjunto_1))

# Agregando elementos a un conjunto
conjunto_1.add(False)
print(conjunto_1)

# Eliominando un elemento al azar del conjunto
conjunto_1.pop()

# Eliominando un elemento específico del conjunto
conjunto_1.remove(49)
print(conjunto_1)

# Agregamos un conjunto a otro mediante UPDATE
conjunto_1.update(conjunto_2)
print(conjunto_1)

# Averiguando si un conjunto es sub-conjunto de otro
print(conjunto_2.issubset(conjunto_1))

# TUPLAS
# Una tupla es una colección ORDENADA de elementos de cualquier tipo de datos,
# los elementos se separan por comas.
tupla_1 = ('Erick Bailey',49,True)
print(type(tupla_1))
print(len(tupla_1))
print(tupla_1.count(49))
print(tupla_1.index(49))