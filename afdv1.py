#!/usr/bin/env python
#-*-coding utf:-8-*-

class subconjunto :
    def __init__ (self, lista, marca):
        self.lista = lista
        self.marca = marca
    def show (self):
        print (self.lista, self.marca)

class tranSub :
    def __init__ (self, origen, destino, costo):
        self.origen = origen
        self.destino = destino
        self.costo  = costo

class transicion:
    def __init__ (self, origin, destiny, cost):
        self.origin = origin
        self.destiny = destiny
        self.cost = cost
    def show (self):
        print (self.origin, self.destiny, self.cost) 

def main (args):

    a = transicion('1','2','a')
    #a.__init__('1','2','a')
    a.show()
    return 0

def existe (lista, elemento):
    bandera = 0
    for i in lista :
        if (i == elemento):
            bandera = 1
    return bandera

def mueve (T, a,listaT,  salida):
    

    temp = []

    for j in range (0, len(T)-1):
        for i in listaT:
            if (T[j] == i.origin):
                temp.append(i)

    for i in temp:
        if (a == i.cost):
            salida.append(i.destiny)

def marcados (Estados):
    bandera = 1
    for i in Estados:
        if (i.marca == 0):
            bandera = 0
    return bandera

def pertenece (lista, estados):
    
    bandera = 0
    for i in estados:
        if ( i.lista == lista):
            bandera = 1
    return bandera

def calculo_cerradura( lista, listaT, cerradura):

    #iniciar la pila y cerradura
    # cerradura es una lista vacía 
    pila = lista
    cerradura = pila

    while (len(pila) != 0):
        a = pila.pop()
        for i in listaT:
            if (i.origin == a):
                if (i.cost == '@'):
                    if (existe (cerradura, i.destiny) == 0):
                        pila.append(i.destiny)
                        cerradura.append(i.destiny)

def calculo_subconjunto (listaT, alfabeto, resultado):
    a = []
    a.append (listaT[0].origin) 
    cerradura = []
    U = []
    calculo_cerradura (a, listaT, cerradura)
    Estados = []
    v = subconjunto (cerradura, 0)
    Estados.append (v)
    Estados[0].lista.sort()
    i = 0

    while (marcados(Estados) != 1):
        Estados[i].marca = 1

        for j in alfabeto:
            temp = []
            mueve (Estados[i].lista, j, listaT, temp)
            calculo_cerradura (temp, listaT, U)
            U.sort()

            if (pertenece (U, Estados) == 0):
                temp2 = subconjunto(U, 0)
                Estados.append(temp2)
            aux = tranSub(Estados[i].lista, j, temp2)
            resultado.append(aux)
            i = i+1

if __name__ == '__main__':
	import sys
	sys.exit (main(sys.argv))
