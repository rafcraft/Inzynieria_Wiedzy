import numpy as np

def regresja_liniowa(regresliniowa_x, regresliniowa_y):
    n = np.size(regresliniowa_x)
    m_x = np.mean(regresliniowa_x)
    m_y = np.mean(regresliniowa_y)
    SS_xy = np.sum(regresliniowa_y * regresliniowa_x) - n * m_y * m_x
    SS_xx = np.sum(regresliniowa_x * regresliniowa_x) - n * m_x * m_x
    b1 = SS_xy / SS_xx
    b0 = m_y - b1 * m_x
    return b0, b1,

x = np.array([2, 5, 7, 8])
y = np.array([1, 2, 3, 3])

print(regresja_liniowa(x, y))
