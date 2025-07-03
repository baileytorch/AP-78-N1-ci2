# Crear una función que permita convertir temperatura de una escala a otra
# El valor de temperatura, la escala inicial y la final serán definidas por el usuario.

# Celsius a Fahrenheit	    (95*°C)+32 ‍
# Farenheit a Celsius	    59*(°F−32)
# Celsius a Kelvin	        °C+273 ‍
# Kelvin a Celsius	        K−273
# Fahrenheit a Kelvin       (59*(°F−32))+273
# Kelvin a Fahrenheit       ((K-273)*95)+32

def celsius_fahrenheit(temperatura):
    try:
        resultado = 9/5 * temperatura + 32
        return resultado
    except:
        print('Valor ingresado NO corresponde...')

def fahrenheit_celsius(temperatura):
    try:
        resultado = 5/9 * temperatura - 32
        return resultado
    except:
        print('Valor ingresado NO corresponde...')

def celsius_kelvin(temperatura):
    try:
        resultado = temperatura + 273.15
        return resultado
    except:
        print('Valor ingresado NO corresponde...')

def kelvin_celsius(temperatura):
    try:
        resultado = temperatura - 273.15
        return resultado
    except:
        print('Valor ingresado NO corresponde...')

def fahrenheit_kelvin(temperatura):
    try:
        celsius = fahrenheit_celsius(temperatura)
        resultado = celsius_kelvin(celsius)
        return resultado
    except:        
        print('Valor ingresado NO corresponde...')

def kelvin_fahrenheit(temperatura):
    try:
        celsius = kelvin_celsius(temperatura)
        resultado = celsius_fahrenheit(celsius)
        return resultado
    except:
        print('Valor ingresado NO corresponde...')

def menu_conversiones():
        print('1.- Kelvin')
        print('2.- Celsius')
        print('3.- Fahrenheit')

def seleccionar_escala():
    menu_conversiones()
    escala = ''
    escala = input('Seleccione su opción [1-3]: ')
    if escala == '1' or escala == '2' or escala == '3':
        return escala
    else:
        print('Opción incorrecta... Volviendo al principio...')
        return ''

def interfaz_usuario():
    print('=================================')
    print('Sistema Conversor de Temperaturas')
    print('=================================')
    print()
    while True:
        print()
        print('¿Desde qué escala de temperatura desea convertir?')
        escala_inicial = seleccionar_escala()
        if escala_inicial == '':
            continue

        print()
        print('¿A qué escala de temperatura desea convertir?')
        escala_final = seleccionar_escala()
        if escala_final == '':
            continue

        if escala_inicial == escala_final:
            print('Opción Incorrecta, intente nuevamente')
            continue

        temperatura_usuario = input('Ingrese temperatura a convertir: ')
        try:
            resultado = 0
            inicio = ''
            final = ''
            if temperatura_usuario != None:
                temperatura = float(temperatura_usuario)
                if escala_inicial == '1' and escala_final == '2':
                    inicio = 'K'
                    final = '°C'
                    resultado = kelvin_celsius(temperatura)
                elif escala_inicial == '1' and escala_final == '3':
                    inicio = 'K'
                    final = '°F'
                    resultado = kelvin_fahrenheit(temperatura)                    
                elif escala_inicial == '2' and escala_final == '1':
                    inicio = '°C'
                    final = 'K'
                    resultado = celsius_kelvin(temperatura)                    
                elif escala_inicial == '2' and escala_final == '3':
                    inicio = '°C'
                    final = '°F'
                    resultado = celsius_fahrenheit(temperatura)                    
                elif escala_inicial == '3' and escala_final == '1':
                    inicio = '°F'
                    final = 'K'
                    resultado = fahrenheit_kelvin(temperatura)                    
                elif escala_inicial == '3' and escala_final == '2':
                    inicio = '°F'
                    final = '°C'
                    resultado = fahrenheit_celsius(temperatura)
                else:
                    print('Opciones deben ser distintas... Intente nuevamente')
            if resultado != 0:
                print(f'{temperatura_usuario}{inicio} = {resultado}{final}')
                print()
            continuar = input('¿Desea convertir otra temperatura [S-N]? ')
            if continuar.lower() == 'no' or continuar.lower() == 'n':
                print('saliendo...')
                break
        except:
            print('Valor ingresado NO corresponde...')

interfaz_usuario()