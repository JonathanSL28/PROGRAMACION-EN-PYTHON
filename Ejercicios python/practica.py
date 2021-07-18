class Logica:
    def __init__(self, lista=None):
        self.__lista = lista
    @property
    def lista(self):
        return self.__lista
    @lista.setter
    def lista(self, nuelista):
        self.__lista = nuelista
    def parImpar(self, numero):
        residuo = numero % 2
        if residuo == 0:
            print('El {} es par'.format(numero))
        else:
            print('El {} es impar'.format(numero))
    def perfecto(self, numero):
        acu = 0
        for cont in range(1,numero):
            resi = numero % cont
            if resi == 0:
                acu += cont
        if acu == numero:
            print('El {} es perfecto'.format(numero))
        else:
            print('El {} no es perfecto'.format(numero))

class Ejercicio(Logica):
    def __init__(self, lista, numeros):
        super().__init__(lista)
        self.info = numeros

    def suma(self, n1,n2):
        return n1 + n2

    def par_Impar(self, numero):
        super().parImpar(numero)
        return numero % 2

# PRESENTACIONES
'''Print de la clase padre'''
ejer = Logica([2,5,6])
ejer.lista=[4,7]
print(ejer.lista)
'''Pint del metodo parImpar')'''
ejer1 = Logica()
num = int(input('Ingrese numero: '))
ejer1.parImpar(num)
'''Print metodo perfecto'''''
ejer1.perfecto(6)
'''Print de la clase hija'''
log2 = Ejercicio([4,7,8],9)
if log2.par_Impar(6) == 0:
    print('Par')
else:
    print('Impar')
print(log2.suma(6,8))
print(log2.lista)