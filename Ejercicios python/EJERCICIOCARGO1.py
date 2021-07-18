class Cargos:
    serie = 0

    def __init__(self, desc='Sin cargo'):
        Cargos.serie = Cargos.serie + 1
        self.codigo = Cargos.serie
        self.descripcion = desc

if __name__ == '__main__':
    carg1 = Cargos()
    print(carg1.codigo, carg1.descripcion)
    carg2 = Cargos('Analista')
    print(carg2.codigo, carg2.descripcion)
    carg3 = Cargos()
    carg3.descripcion = 'Director'
    print(carg3.codigo, carg3.descripcion)
    # print(Cargo.serie)