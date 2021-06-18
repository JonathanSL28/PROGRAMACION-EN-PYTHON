class For:
    def __init__(self):
        pass

    #ciclo repetitivo de incrementos o decrementos se ejecuta por verdadero
    def usoFor(self):
        datos=["Jonathan",20,True,"Lavayen"]
        numeross=(6,10.6,0,75)
        docente={"nombre":"Jonathan", "edad":20,"fac":"dificil"}
        listanotas=[(30,40),(20,40),(50,40)]
        #range([inicio=0],limite,[incremento/decremento]. Genera un rang de valores desde un valor inicial a un valor dinal
        #se ejecuta desde inicio hasta el limite
        for i in range(9):
            print("i={}".format(i))
        for i in range(5,18):
            print("i={}".format(i))
        for i in range(4,20,2):
            print("i={}".format(i),end=" ")
        for i in range(21,2,-3):
            print("i={}".format(i))

        longitud=len(datos)
        for i in range(longitud):
            print(datos[i])
        #
        for j in range(longitud-1,-1,-1):
            print(datos[j])

        for i, valor in enumerate(datos):
            print(i,valor)
        #
        print("\n Diccionario de notas")
        for clave,valor in docente.items():
            print(clave,":",valor, end=" ")

        listanota=[(10,90),[80,60,50],(50,40,20,10,5)]
        acu=0
        con=0
        prom=0
        prom1 = 0
        for notas in listanota:
            print(notas)
            acu1 = 0
            con1 = 0
            for nota in notas:
                print(nota)
                con+=1
                acu=acu+nota
                prom=acu/con
                acu1=acu1+nota
                con1=con1+1
                prom1 = acu1 / con1
            print("acumulado:",acu1,"notas:",con1)
            print("La notas por grupos son:{}, son:{} de notas y su promedio es de:{}".format(acu1,con1,prom1))
        print("")
        print("El total de nota es:{}, son:{} notas, y un promedio final de:{}".format(acu,con,prom))

        listaalumnos=[{"nombre":"Carlos","final":100},{"nombre":"Nathaly","final":40},{"nombre":"Lady","final":90}]
        acu=0
        con=0
        for alumnos in listaalumnos:
            print(alumnos)
            for clave,valor in alumnos.items():
                print(clave,":",valor, end="  ")
                if clave=="final":
                    acu=acu+valor
            con=con+1
        pro=acu/con
        print(pro)

        frase="Hola como estas querida mia"
        vocales=[]
        for car in frase:
            if car in ("a","e","i","o","u"):
                vocales.append(car)
        print(vocales)


objFor=For()
objFor.usoFor()
