
help(str.split)

cursos = 'Java JavaScript Node Python Diseno'
lsita_cursos = cursos.split()
print(f'Lista de cursos: {lista_cursos}')
print ( type(lsita_cursos))

cursos_separados_coma = 'Java, Python, Node, JavaS, Spring'

lsita_cursos= cursos_separados_coma.split(',',2)
print(f'Lista de cursos: {lista_cursos}')
print (len(lsita_cursos))



