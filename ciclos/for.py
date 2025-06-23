# Recorrer una lista con FOR
animales = ['gato','perro','canario','panda','capibara']

# print(animales)

for elemento in animales:
    print(f'Mi animal es: {elemento}')

usuarios = ['Aquiles Baeza','Wendy Sulca','Delfin Quispe']

contador = 0
for nombre in usuarios:
    contador = contador + 1
    print(f'Usuario {contador}: {nombre}')

for i in range(len(usuarios)):
    print(f'Usuario {i + 1}: {usuarios[i]}')

# Recorrer un string con FOR
cadena = "Introducción Programación"
for letra in cadena:
    print(letra.upper())