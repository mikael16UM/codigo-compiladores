#!/usr/bin/env python
#-*-coding utf:-8-*-

class estados:
    def __init__ (self, origen, derivada):
        self.origen = origen
        self.derivada = derivada

class NoTerminales:
    def __init__ (self, origen, primeros):
        self.origen =  origen
        self.primeros =  primeros
        #self.siguientes =  siguientes

def posicion (x, listaEstados):
    #regresa la posicion donde están las reglas de derivacion
    for i in range (0, len(listaEstados)):
        if (listaEstados[i].origen == x):
            return i

def copiar_derivadas (indice, listaEstados):
    lista = []
    for i in listaEstados[indice].derivada:
        lista.append (i)
    return lista

def primeros (listaEstados, listaNT, Lresultados):
    indice = 0
    while (indice < len(listaNT)):
        Lprimeros = []
        letra = listaNT[indice]
        aux = calcular_primeros(letra, listaEstados, listaNT)
        #aux = [0]
        Lprimeros.append (aux)
        aux2 = NoTerminales (letra, Lprimeros)
        Lresultados.append (aux2)
        indice = indice + 1

def no_terminal (letra, lista):
    bandera = 0
    for i in lista:
        if(i == letra):
            bandera = 1

    return bandera

def calcular_primeros (x, listaEstados, listaNT):
    ent = []
    indice = posicion(x, listaEstados)

    while (indice < len(listaEstados) and listaEstados[indice].origen == x):
        lista = copiar_derivadas (indice, listaEstados)

        for i in range (0, len (lista)):
            if (lista[i] in listaNT):
               # print(x, lista[i])
                if (lista[i] ==  x):
                    break
                else:
                    ent = calcular_primeros (lista[i], listaEstados, listaNT)
                    break
            else:
                ent.append(lista[i])
                break
        indice = indice +1
    return ent

def convertir_a_estados (lista, diccionario):

    for i in diccionario:
        laux = diccionario[i]
        origen = laux[0]
        derivada = []
        for j in range (1, len(laux)):
            derivada.append(laux[j])
        aux = estados (origen, derivada)
        lista.append(aux)


def trabajar (Reglas, listaNT):
    Lresultados = []
    listaEstados = []
    convertir_a_estados (listaEstados, Reglas)
    primeros(listaEstados, listaNT, Lresultados)

    for i in listaEstados:
        print (i.origen, " -> ", i.derivada)

    for i in Lresultados:
        print ("primeros de ", i.origen, ": ", i.primeros)


def main ():
    Reglas={'1':['S','S',';','S'],'2':['S','id',':=','E'],'3':['S','print','(','L',')'],'4':['E','id'],'5':['E','num'],'6':['E','E','+','E'],'7':['E','(','S',',','E',')'],'8':['L','E'],'9':['L','L',',','E']}  
    listaNT=('S','E','L')
    #listaNT=['E','T','F']
    #Reglas={'1':["E","E","+","T"],'2':["E","T"],'3':["T","T","*","F"],'4':["T","F"],'5':["F","(","E",")"],'6':["F","id"]}
    #listaNT=['D','L','T']
    #Reglas={'1':['D','T',"id","L",";"],'2':['L',',','id','L'],'3':['L','@'],'4':["T","float"],'5':["T","int"]}    
    trabajar (Reglas, listaNT)


if __name__ == '__main__':
	main()