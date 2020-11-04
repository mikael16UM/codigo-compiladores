#!/usr/bin/env python
#-*-coding utf:-8-*-

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

def mueve (T, a, salida):
    for i in T:
        if (a == i.cost):
            salida.append(i.destiny)

def calculo_cerradura( lista, listaT, cerradura):

    #iniciar la pila y cerradura
    # cerradura es una lista vacía 
    pila = []
    for i in lista:
        pila.append(i.origin)
    cerradura = pila

    while (len(pila) != 0):
        a = pila.pop()
        for i in listaT:
            if (i.origin == a):
                if (i.cost == '@'):
                    if (existe (cerradura, i.destiny) == 0):
                        pila.append(i.destiny)
                        cerradura.append(i.destiny)

	
if __name__ == '__main__':
	import sys
	sys.exit (main(sys.argv))
