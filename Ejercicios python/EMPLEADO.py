
from EJERCICIOCARGO1 import Cargos

class Empleado:
    serie = 0
    def __init__(self, nomb,cedu, suel, carg):
        self.codigo = self.generar()
        self.nombre = nomb
        self.cedula = cedu
        self.sueldo = suel
        self.cargo = carg

    def mostrar(self):
        print('Codigo:{} ; Nombre:{}  ; Cargo:{}-{}'.format(self.codigo, self.nombre, self.cargo.codigo, self.cargo.descripcion))

    def generar(self):
        Empleado.serie = Empleado.serie + 1
        return Empleado.serie


carg1 = Cargos('Docente')
empl = Empleado('Daniel', '1234', 200, carg1)
empl.mostrar()
carg2 = Cargos('Analista')
empl2 = Empleado('Anna', '14643', 700, carg2)
empl2.mostrar()