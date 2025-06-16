# Un MÉTODO es una función de programación que ejecuta una tarea específica

# El método DIR nos indica todos los métodos disponibles con el tipo de datos
# print(dir(str))
# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'

nombre = 'erick bailey'
asignatura = 'INTRODUCCION PROGRAMACION'

print(nombre.capitalize())
print(nombre.title())
print(nombre.upper())
print(asignatura.lower())
print(nombre.count('e'))
# FIND devuelve el ÍNDICE de la posición de la letra buscada
print(nombre.find('e'))
print(nombre.endswith('x'))
print(nombre.endswith('y'))
print(nombre.replace('bailey','torch'))