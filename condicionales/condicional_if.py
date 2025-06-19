edad = input('Ingrese su edad: ')

if int(edad) >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Grupos Socio-Económicos de Chile
# AB: $7177530
# C1a: $3010391
# C1b: $2072853
# C2: $1500774
# C3: $1003426
# D: $640667
# E: $361583

sueldo_str = input('Ingrese su sueldo mensual: ')
sueldo = int(sueldo_str)

if sueldo <= 361583:
    print('Ud. pertenece al grupo E')
elif 361583 < sueldo <= 640667:
    print('Ud. pertenece al grupo D')
elif 640667 < sueldo <= 1003426:
    print('Ud. pertenece al grupo C3')
elif 1003426 < sueldo <= 1500774:
    print('Ud. pertenece al grupo C2')
elif 1500774 < sueldo <= 2072853:
    print('Ud. pertenece al grupo C1b')
elif 2072853 < sueldo <= 3010391:
    print('Ud. pertenece al grupo C1a')
elif 3010391 < sueldo:
    print('Ud. pertenece al grupo AB')
else:
    print('Valor ingresado NO corresponde')