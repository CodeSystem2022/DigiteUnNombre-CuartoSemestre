# Dar formato a nu string

nombre = 'Ariel'
eadad = 28
mensaje_con_formato = 'Mi nombr es %$ y tengo %d años' % (nombre, edad)
print(mensaje_con_formato)


# creamos una tupla

persona = ('Carla', 'Gomez', 5000.00)
mensaje_con_formato = 'Hola %s %s . Tu sueldo es %.2f' # % persona # Aqui le pasamos el objeto que es tupla
#print(mensaje_con_formato % persona)

nombre = 'Juan'
edad = 19
sueldo = 3000
#mensaje_con_formato = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre, edad, sueldo)
#print(mensaje_con_formato)

#mensaje = 'Nombre {n} Edad {e} Sueldo {s:.2f}'.format(n=nombre,e=edad,s=sueldo)
#print(mensaje)

diccionario = {'nombre': 'Ivan', 'Edad': 35, 'Sueldo'; 8000.00}
mensaje = 'nombre {diccionario[nombre]} Edad {diccionario[Edad]}'.format(diccionario=diccionario)
print(mensaje)
