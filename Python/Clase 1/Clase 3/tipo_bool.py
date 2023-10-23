#Bool contiene los valores true y false
# Los tipos numricos, es false para el 0, true para los demas valores

valor = 0
resultado = bool(valor)
print (f'valor: {valor}, Resultado: {resultado}' )

valor = 0.1
resultado= bool(valor)
print(f'valor: {valor}, Resultado: {resultado}' )

# Tipo String -> Flase '' , True demas valores
valor = ''
resultado= bool(valor)
print(f'valor: {valor}, Resultado: {resultado}' )

valor = 'Hola'
resultado= bool(valor)
print(f'valor: {valor}, Resultado: {resultado}' )

#Tipo de colecciones -> False para colecciones vacias
#Tipo de colecciones -> True para todas las demas

valor = []
resultado= bool(valor)
print(f'valor: {valor}, Resultado: {resultado}' )

valor = [2, 3, 4]
resultado= bool(valor)
print(f'valor: {valor}, Resultado: {resultado}' )

#Tupla

valor = ()
resultado= bool(valor)
print(f'valor: {valor}, Resultado: {resultado}' )

valor = (5,)
resultado= bool(valor)
print(f'valor: {valor}, Resultado: {resultado}' )

#Diccionario

valor = {}
resultado= bool(valor)
print(f'valor: {valor}, Resultado: {resultado}' )

valor = {'Nombre': 'Juan', 'Apellido': 'Perez'}
resultado= bool(valor)
print(f'valor: {valor}, Resultado: {resultado}' )

#Sentencias de control con bool

if 'hola':
    pritn('Regresa verdadero')
else:
    print('Regresa falso')

#Ciclos

variable = 3
while variable:
    print ('Regresa verdadero')
    break
else:
    print ('Regresa falso')
