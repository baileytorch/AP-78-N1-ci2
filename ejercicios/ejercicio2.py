# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

contrasena = 'intro_progra'

while True:
    contrasena_usuario = input('Ingrese contraseña:')
    if contrasena_usuario == contrasena:
        print('Ingreso Correcto!')
        break        
    else:
        print('Contraseña incorrecta!')

# contrasena_usuario = ''
# while contrasena_usuario != contrasena:
#     contrasena_usuario = input('Ingrese contraseña:')
# else:
#     print('Ingreso Correcto!')