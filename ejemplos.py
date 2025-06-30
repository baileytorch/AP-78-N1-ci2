try:
    a=int(input('Ingrese numerador: '))
    b=int(input('Ingrese denominador: '))
    division = a/b
    print(division)
except ZeroDivisionError:
    print('No se puede dividir por 0.')
except ValueError:
    print('Valor ingresado NO corresponde.')
except:
    print('Error inesperado...')