class usoCondicion:
    c = 0
    def __init__(self, num1=0,num2=1):
        self.numero1 = num1
        self.numero2 = num2
        self.numero3 = num1

    def aplicacionIf(self):
        if self.numero1 == self.numero2:
            print('El numero: n1={} y el nmero n2={}, son iguales'.format(self.numero1,self.numero2))
        elif self.numero1 == self.numero3:
            print('El numero: n1={} y el numero n3={} , son iguales'.format(self.numero1,self.numero3))
        else:
            print("Los numeros son desiguales")

condi1 = usoCondicion()
print(condi1.numero1)
print(condi1.numero2)

condi2 = usoCondicion(10,20)
condi2.aplicacionIf()
print(condi2.numero1)