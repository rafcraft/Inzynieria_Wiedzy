import numpy as np

def normalizacja(U):
    u = U/np.sqrt(np.sum(np.dot(U, U)))
    u2 = np.round_(u, decimals=3)
    return u2

def wektor_ortogonalny(macierzA, macierzB):
    suma = np.dot(macierzA, macierzB)
    suma2 = np.round_(suma, decimals=3)
    return suma2

def normalizacja_macierzy(U):
    dlugosc = len(U)
    xyz = [[0 for i in range(dlugosc)] for j in range(dlugosc)]
    for x in range(0, dlugosc):
        xyz[x] = normalizacja(U[x])
    return np.array(xyz)

def spr_wektor():
    return 0

B = [[1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, -1, -1, -1, -1],
     [1, 1, -1, -1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, -1, -1],
     [1, -1, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, -1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, -1, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, -1]]

Wektor = [8, 6, 2, 3, 4, 6, 6, 5]

B = np.array(B)
B1 = np.array(B)
print(wektor_ortogonalny(B, B1.T))
print("\n", normalizacja_macierzy(B))
B2 = normalizacja_macierzy(B)
print("\n", wektor_ortogonalny(B2, B2.T))

print("\n", np.dot(B, Wektor))
