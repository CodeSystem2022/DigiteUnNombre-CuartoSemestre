

help(str.join)
tupla_str =('Hola', 'Alumnos', 'Tecnicatura','Universitaria')
mensaje = ''.join(tupla_str)
print (f' Mensaje: {mensaje}') 


lista_cursos = ['Java','Py', 'Angular', 'Spring']
mensaje = ' ,'.join(lista_cursos)
print(f'Mensaje: {mensaje}')

cadena = 'Hola Mundo'
mensaje = '.'.join(cadena)
print(f'Mensaje: {mensaje}')

diccionario = {'nombre' : 'Juan', 'apellido': 'Perez', 'edad': '18'}

llaves = '-'.join(diccionario.keys())

valores = '-'.join(diccionario.values())
print(f'Llaves: {llaves}, type: {type(llaves)}')
print(f'valores: {valores}, Type: {type(valores)}')

