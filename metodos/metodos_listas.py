lista_1 = [1,2,3,4,5,True,False,'Lista 1']

# print(dir(lista))
print()
print(f'Imprimiendo lista_1: {lista_1}')

# 'append': Agrega un nuevo elemento a la colección
lista_1.append(10)
print()
print(f'Usando el método APPEND() agrego el elemento 10, imprimo lista_1: {lista_1}')

# 'copy': Copia la colección en otra variable
lista_2 = lista_1.copy()
print()
print(f'Copiando la lista con COPY() desde lista_1 a lista_2, imprimo lista_2: {lista_2}')

# 'clear': Elimina todos los elementos de la colección
lista_2.clear()
print()
print(f'Limpiando lista_2 con CLEAR(), imprimo lista_2: {lista_2}')

# 'count': Cuenta la cantidad de elementos de la colección buscando un elemento específico
print()
print(f'Contanto elementos = 1 de lista_1: {lista_1.count(1)}')

# 'len': Abreviatura de LENGHT, largo en inglés, cuenta la cantidad de elementos de la colección
print()
print(f'Cantidad de elementos de lista_1: {len(lista_1)}')

# 'extend': Permite agregar un elemento de otra colección al final de este misma
lista_2 = ['Hola','Bienvenido','Amigo']
lista_1.extend(lista_2)
print()
print(f'Agregando los elementos de lista_2 a lista_1 mediante método EXTEND(), imprimiendo lista_1: {lista_1}')

# 'index': Entrega el índice de un determinado elemento, se busca por texto
print()
print(f'Imprimiendo el índice del elemento Hola mediante método INDEX(): {lista_1.index('Hola')}')

# 'insert': Inserta un elemento en una posición específica, indicar el índice
print()
nuevo_elemento = 'Elemento Nuevo'
lista_1.insert(0,nuevo_elemento)
print(f'Agregando un elemento al principio de la lista con el índice 0 mediante el método INSERT(): {lista_1}')

# 'pop': Elimina el último elemento, o un elemento específico si se indica el índice
print()
lista_1.pop(0)
print(f'Eliminando el primer elemento mediante el índice 0 con el método POP(): {lista_1}')

# 'remove': Elimina el primer elemento coincidente con un string de búsqueda
print()
lista_1.remove(False)
print(f'Eliminando el elemento FALSE mediante el método REMOVE(): {lista_1}')

# 'reverse': Revierte el orden de la colección
print()
lista_1.reverse()
print(f'Invirtiendo el orden de los elementos con REVERSE(): {lista_1}')

# 'sort': Si es una colección de string, ordena alfabéticamente, si es una colección de números ordena de menor a mayor.
# Ambos ordenes pueden cambiarse al indicarlo.
print()
lista_3 = [5,4,8,2,0,9]
lista_3.sort()
print(f'Ordenando la lista de menor a mayor con SORT(): {lista_3}')
lista_3.sort(reverse=True)
print(f'Ordenando la lista de mayor a menor con SORT(REVERSE=TRUE): {lista_3}')