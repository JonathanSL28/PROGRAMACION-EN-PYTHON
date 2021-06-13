class Datos:
    instancia = 0
    def __init__(self, texto ='Comienzo'):
        self.palabras = texto

    def Detalles(self):
        nombres = 'Jonathan Lavayen'
        edad, peso = 19, 60
        sexo = 'M'
        civil = True
        # TUPLAS
        usuario = ()
        usuario = ('Jonathan', 1234, 'Jlavayen@gmail.com', True)
        # usuario[3] = 'Simon Bolivar'
        # lISTAS
        materias = []
        materias = ['Programacion', '', 'POO']
        materias[1] = 'Python'
        materias.append('Go')
        # DICCIONARIOS
        docente = {}
        docente = {'nombre':'Daniel', 'edad':50, 'fac':'faci'}
        docente['carrera'] = 'cs'
        # presentacion con format
        print('Mi nombre es{} y tengo{} años'.format(nombres, edad))
        print(usuario, materias, docente)
        print(usuario,usuario[0], usuario[0:2],usuario[-1])
        print(materias,materias[2:],materias[:1],materias[::],materias[-2:])
        print(docente,docente['nombre'])

info = Datos()
info.Detalles()
print(info.palabras)
