class Ordenar:
    def __init__(self, lista):
        self.lista = lista

    def borbuja(self):
        for i in range(len(self.lista)):
            for j in range(i+1, len(self.lista)):
                if self.lista[i] > self.lista[j]:
                    aux = self.lista[i]
                    self.lista[i] = self.lista[j]
                    self.lista[j] = aux

    def insertar(self,valor):
        self.borbuja()
        nuevalista=[]
        bandera = False
        for posicion,elemento in enumerate(self.lista):
            if elemento > valor:
                nuevalista.append(valor)
                bandera = True
                break
        if bandera == True:
            self.lista = self.lista[0:posicion] + nuevalista + self.lista[posicion:]
        else:
            self.lista.append(valor)
        return self.lista

    def insertar2(self,dato):
        self.lista.sort()
        self.borbuja()
        nuelista=[]
        bandera = False
        for posicion,elemento in enumerate(self.lista):
            if elemento > dato:
                bandera = True
                break
        if bandera:
            for i in range(posicion):
                nuelista.append(self.lista[i])
            nuelista.append(dato)
            for j in range(posicion,len(self.lista)):
                nuelista.append(self.lista[j])
            self.lista = nuelista
        else:
            self.lista.append(dato)
        return self.lista


orden = Ordenar([10,15,20,70,80])
# print(orden.insertar(90))
print(orden.insertar2(50))
