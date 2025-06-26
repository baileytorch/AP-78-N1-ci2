# Solicitar al usuario ingresar 5 números y 
# calcular la suma de esos números

suma = 0
for i in range(5):
    numero = float(input('Ingrese número: '))
    suma += numero
print(suma)