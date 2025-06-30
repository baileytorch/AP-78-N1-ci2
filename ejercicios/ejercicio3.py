# Solicitar al usuario ingresar 5 números y 
# calcular la suma de esos números

suma = 0
numeros = []
for indice in range(5):
    # Suma manual de los valores ingresados
    numero = 0
    try:
        numero = float(input('Ingrese número: '))
        suma += numero
        # Usar método sum() para sumar los elementos de la lista
        numeros.append(numero)
    except ValueError:
        print('Valor ingresado NO corresponde')
        suma += 0
        numeros.append(0)
    except:
        print('Qué pasó con la aplicación??!!')

# Imprimo la suma manual
print(suma)
# Imprimo sum()
print(f"La suma de {numeros} = {sum(numeros)}")