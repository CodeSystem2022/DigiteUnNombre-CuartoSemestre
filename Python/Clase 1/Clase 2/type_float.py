#Pfrofundizamos en el tipo float

a= 3.0
print(f'a: {a:.2f}')

#Constructro floar -> puede recibir enterios y de tipo stringht

a= float(10) #Tipo entero
a= float('10')
print(f'a:{a:.2f}')

#Notacion exponencial (valores engativos o positivos)

a = 3e5
print (f'a: {a:2f}')

a = 3e-5
print (f'a: {a:.5f}')

#Cualquier calculo que incluye float, todo cambia a float !

a = 4.0 + 5
print(a)
print(type(a))







