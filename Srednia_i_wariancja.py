import numpy as np
import math as m
file = open("australian.dat", "r")

listaDecyzji = []

for line in file:
    listaStr = line.split(' ')
    ab = lambda e: float(e)
    listaNum = list(map(ab, listaStr))
    listaDecyzji.append(listaNum)
file.close()

def srednia(lista):
    suma = 0
    tmp = []
    for i in range(len(lista)):
        tmp.append(1)
    suma += np.dot(lista, tmp)
    return suma/len(lista)

def wariancja(lista, sredniaa):
    vector = []
    tmp2 = []
    for i in range(len(lista)):
        vector.append(sredniaa)
    for y in range(len(lista)):
        tmp2.append(lista[y] - vector[y])
    wynik = np.dot(tmp2, tmp2)
    return wynik/len(lista)


def odchylenie(lista, sredniaa):
    return m.sqrt(wariancja(lista, sredniaa))

x = np.array([2, 5, 7, 8])

print("Średnia", srednia(x))
print("Warjancja", wariancja(x, srednia(x)))
print("Odchylenie", odchylenie(x, srednia(x)))
