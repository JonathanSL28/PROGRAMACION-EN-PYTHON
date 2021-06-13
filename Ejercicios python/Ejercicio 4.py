class Estructuras:
    def __init__(self, n=5):
        self.numero = n

    def AplicacionWhile(self):
        vocal = input('Ingrese vocal: ').lower()
        while vocal not in ('a','e','i','o','u'):
            vocal = input('Ingrese vocal: ').lower()
        print('Perfecto!.')

ciclo1 = Estructuras()
ciclo1.AplicacionWhile()