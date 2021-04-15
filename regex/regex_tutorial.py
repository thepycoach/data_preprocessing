import re

texto = '''Hola Mundo.
Me gusta Python!!!!!
Mi primer numero de la suerte es 987-654-321
Mi segundo numero de la suerte es 876-543-210
Mi tercero numero de la suerte es 765-432-100
Mi cuarto numero de la suerte es 123-456-123-123-456
'''

# buscar el primer emparejamiento
print(re.search(r'\d', texto))
# flags
print(re.search(r'^hola', texto, flags=re.I)) #ignorar minuscula/mayuscula

# buscar todos los emparejamientos
print(re.findall(r'\d', texto))

# Casos comunes
# 1 Encontrar puntuación
print(re.findall(r'[^\w\s]', texto))

# 2 Validar una fecha
texto = '''
13-04-2021
2021-13-04
2021-04-13
'''
print(re.findall(r'\d{2}-\d{2}-\d{4}', texto))

# 3 Validar un usuario
# condiciones: 4-14 y solo numeros o letras

texto = '''
usuario10
abc
10
'''

print(re.findall(r'[a-z0-9]{4,14}', texto))

