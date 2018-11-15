# Autor: Alex Serrano Durán
# Descripción: Este programa desempeña una serie de programas usando listas.


def extraerPares(lista):
    listaPares = []
    for dato in lista:
        if dato % 2 == 0:
            listaPares.append(dato)
    return listaPares


def extraerMayoresPrevio(lista):
    listaMayoresPrevio = []
    for k in range(1, len(lista)):
        if lista [k] > lista [k-1]:
            listaMayoresPrevio.append(lista[k])
    return listaMayoresPrevio


def intercambiarParejas(lista):
    listaIntercambiada = []
    if len(lista) % 2 == 0:
        for k in range(1, len(lista), 2):
            listaIntercambiada.append(lista[k])
            listaIntercambiada.append(lista[k-1])
    else:
        for k in range(1, len(lista), 2):
            listaIntercambiada.append(lista[k])
            listaIntercambiada.append(lista[k-1])
        listaIntercambiada.append(lista[len(lista)-1])
    return listaIntercambiada


def intercambiarMM(lista):
    if len(lista) > 0:
        menor = min(lista)
        mayor = max(lista)
        indiceMayor = lista.index(max(lista))
        indiceMenor = lista.index(min(lista))
        lista[indiceMayor] = menor
        lista[indiceMenor] = mayor
        return lista
    return lista


def promediarCentro(lista):
    listaNueva = []
    for dato in lista:
        listaNueva.append(dato)
    listaNueva.sort()
    if len(listaNueva) > 2:
        del listaNueva[len(lista)-1]
        del listaNueva[0]
        if len(listaNueva) != 0:
            promedio = sum(listaNueva)//len(listaNueva)
            return promedio
    else:
        return 0


def calcularEstadistica(lista):
    if len(lista) > 0:
        promedio = sum(lista)/len(lista)
        suma = 0
        for dato in lista:
            valor = (dato-promedio)**2
            suma += valor
        desviacion = (suma/(len(lista)-1))**.5
        return (promedio, desviacion)
    return (0,0)


lista=[]
