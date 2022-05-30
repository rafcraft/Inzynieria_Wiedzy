import math
import numpy as np

lista = []
with open("australian.dat", "r") as plik:
    for i in plik:
        tmp = i.split(" ")
        a = list(map(lambda n: float(n), tmp))
        lista.append(a)
    print(lista)
    print("\n")

def Euklides(lista):
    wynik = 0
    for x in range(len(lista)-1):
        for y in range(len(lista)-1):
            wynik += (lista[x] - lista[x])**2
            return math.sqrt(wynik)
print(Euklides(lista))

plik.close()

#PRACA DOMOWA
# Y= LISTA[0]
# D(X,Y), GDZIE X NALERZY DO LISTY BEZ 0'EGO INDEKSU
# {0:5,4, 1:8}
# OBLICZANIA WYNACZNIKA MACIERZY Z MACIERZY KWADRATOWEJ

A = np.array([[10, 5], [6, 7]])
A3 = np.array([[10, 2, 2], [2, 5, 8], [1, 1, 1]])

def wyznacznik(x):
    det = np.linalg.det(x)
    return det

def wyznacznikV2(x):
    temp = len(x)
    if temp == 2:
        return "Wyznacznik macierzy 2x2: ", (x[0][0] * x[1][1]) - (x[0][1] * x[1][0])
    if temp == 3:
        return "Wyznacznik macierzy 3x3: ", ((x[0][0] * x[1][1] * x[2][2] + x[1][0] * x[2][1] * x[0][2] + x[2][0] * x[0][1] * x[1][2]) -
                                             (x[0][2] * x[1][1] * x[2][0] + x[1][2] * x[2][1] * x[0][0] + x[2][2] * x[0][1] * x[1][0]))
    else:
        print("Macierz musi być kwadratowa!")

print("Macierz 2x2", int(wyznacznik(A)))
print("Macierz 3x3", int(wyznacznik(A3)))

print(wyznacznikV2(A))
print(wyznacznikV2(A3))
