# print(dir(int))
# 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes'
numero = 56
numero_2 = 22.5789456
print(numero.is_integer())
print(numero_2.is_integer())

# print(dir(float))
# 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real'

numeros = [0,8,6,9,7,5,3,2,1]
print(f'El número mayor es: {max(numeros)}')
print(f'El número menor es: {min(numeros)}')
print(f'Redondear un decimal con método ROUND(): {round(numero_2,3)}')