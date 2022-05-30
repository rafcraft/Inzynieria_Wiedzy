import numpy as np

def normalizacja(U):
    u = U/np.sqrt(np.sum(np.dot(U, U)))
    return u

def projektcja(U, V):
    a = (np.dot(V, U)/np.dot(U, U))
    for x in range(len(U)):
        U[x] = U[x] * a
    return U

def macierz_QR(macierzA, wektor_z_normalizowany, projekcjaV2, wektorV2):
    wektorE1 = normalizacja(wektor_z_normalizowany)
    u2 = [wektorV2[i] - projekcjaV2[i] for i in range(len(wektorV2))]
    wektorE2 = normalizacja(u2)
    QT = [wektorE1, wektorE2]
    macierzA = np.matrix(macierzA)
    macierzQ = np.matrix(QT)
    R = macierzQ * macierzA
    return R

A = [[1, 0],
     [1, 1],
     [0, 1]]

V1 = [A[x][0] for x in range(len(A))]
V2 = [A[x][1] for x in range(len(A))]

projekcjaU2 = projektcja(V1, V2)
print(macierz_QR(A, V1, projekcjaU2, V2))
